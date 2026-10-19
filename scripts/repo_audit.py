"""Inventory and freshness gate. Records do not prove that code was understood."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import stat
import sys

DEPENDENCIES={'.git','node_modules','.venv','venv','__pycache__','.mypy_cache','.pytest_cache'}
SENSITIVE={'.env','test.env','.npmrc','.pypirc','credentials','id_rsa','id_ed25519'}
SECRET_SUFFIXES={'.pem','.p12','.pfx','.key','.jks'}

def redirected(path):
    info=path.lstat()
    return path.is_symlink() or bool(getattr(info,'st_file_attributes',0)&getattr(stat,'FILE_ATTRIBUTE_REPARSE_POINT',0x400))

def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def reject_links(path):
    path=Path(path).absolute()
    for parent in [*reversed(path.parents),path]:
        try:
            if redirected(parent):raise ValueError('output/ledger path cannot be redirected')
        except FileNotFoundError:
            continue

def path_key(path):
    return os.path.normcase(str(Path(path).resolve()))

def collect(root,excluded,artifacts):
    records=[]
    def walk_error(exc):
        path=Path(exc.filename or root)
        try:relative=path.relative_to(root).as_posix()
        except ValueError:relative='.'
        records.append({'path':relative,'kind':'blocked-read','reason':type(exc).__name__})
    for directory,dirs,files in os.walk(root,followlinks=False,onerror=walk_error):
        base=Path(directory)
        for name in sorted(list(dirs)):
            p=base/name;rel=p.relative_to(root).as_posix()
            reason=excluded.get(rel)
            if redirected(p):
                records.append({'path':rel,'kind':'blocked-link','reason':'directory redirection; inspect separately'})
                dirs.remove(name)
            elif name in DEPENDENCIES or reason:
                records.append({'path':rel,'kind':'excluded-directory','reason':reason or 'dependency, VCS metadata or cache; owning generators/config still require review'})
                dirs.remove(name)
        for name in sorted(files):
            p=base/name;rel=p.relative_to(root).as_posix()
            try:
                if redirected(p):
                    records.append({'path':rel,'kind':'blocked-link','reason':'file redirection; inspect separately'});continue
                if path_key(p) in artifacts:
                    continue
                info=p.stat()
                if not stat.S_ISREG(info.st_mode):
                    records.append({'path':rel,'kind':'blocked-special','reason':'not a regular file'});continue
                secret=name in SENSITIVE or name.startswith('.env.') or p.suffix.lower() in SECRET_SUFFIXES
                item={'path':rel,'bytes':info.st_size}
                if secret:
                    item.update(kind='sensitive-metadata',mtime_ns=info.st_mtime_ns)
                else:
                    h=hashlib.sha256()
                    with p.open('rb') as stream:
                        for block in iter(lambda:stream.read(1024*1024),b''):h.update(block)
                    item.update(kind='file',sha256=h.hexdigest())
                records.append(item)
            except OSError as exc:
                records.append({'path':rel,'kind':'blocked-read','reason':type(exc).__name__})
    return sorted(records,key=lambda x:x['path'])

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    scan=sub.add_parser('scan')
    scan.add_argument('--root',type=Path,required=True)
    scan.add_argument('--out',type=Path,required=True)
    scan.add_argument('--ledger',type=Path,required=True,help='explicit future reading-ledger path, excluded from its own inventory')
    scan.add_argument('--exclude',action='append',default=[],help='exact relative directory=observable reason; repeatable')
    verify=sub.add_parser('check')
    verify.add_argument('--inventory',type=Path,required=True)
    verify.add_argument('--ledger',type=Path,required=True)
    args=parser.parse_args()
    try:
        if args.command=='scan':
            root=args.root.resolve(strict=True)
            if not root.is_dir():raise ValueError('root must be a directory')
            excluded={}
            for value in args.exclude:
                path,sep,reason=value.partition('=')
                candidate=Path(path)
                if not sep or not reason.strip() or candidate.is_absolute() or '..' in candidate.parts:raise ValueError('exclude must be relative-directory=reason')
                excluded[candidate.as_posix()]=reason
            reject_links(args.out)
            reject_links(args.ledger)
            artifacts={path_key(args.out),path_key(args.ledger)}
            if path_key(args.out)==path_key(args.ledger):raise ValueError('inventory and reading ledger must differ')
            if args.out.exists():raise ValueError('inventory exists; choose a new snapshot path to preserve prior evidence')
            records=collect(root,excluded,artifacts)
            doc={'schema':1,'created_at':datetime.now(timezone.utc).isoformat(),'root':str(root),'excluded':excluded,'artifact_paths':sorted(artifacts),'files':records}
            args.out.parent.mkdir(parents=True,exist_ok=True)
            args.out.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            print(json.dumps({'inventory_written':True,'entries':len(records),'blocked':sum(x['kind'].startswith('blocked') for x in records),'reading_complete':False}))
            return 0
        inventory=load(args.inventory);ledger=load(args.ledger)
        if not isinstance(inventory,dict) or not isinstance(ledger,dict):raise ValueError('inventory and ledger must be objects')
        if inventory.get('schema')!=1 or ledger.get('schema')!=1:raise ValueError('unsupported schema')
        if not isinstance(inventory.get('files'),list) or not isinstance(inventory.get('excluded'),dict) or not isinstance(inventory.get('artifact_paths'),list):raise ValueError('invalid inventory structure')
        if not isinstance(inventory.get('root'),str) or not all(isinstance(k,str) and isinstance(v,str) for k,v in inventory['excluded'].items()) or not all(isinstance(p,str) for p in inventory['artifact_paths']):raise ValueError('invalid inventory paths')
        if not Path(inventory['root']).is_dir():raise ValueError('original repository root is unavailable')
        seen=set()
        for entry in inventory['files']:
            if not isinstance(entry,dict) or not isinstance(entry.get('path'),str) or not isinstance(entry.get('kind'),str):raise ValueError('invalid inventory entry')
            path=Path(entry['path'])
            if path.is_absolute() or '..' in path.parts or entry['path'] in seen:raise ValueError('invalid or duplicate inventory path')
            seen.add(entry['path'])
            if entry['kind'] not in {'file','sensitive-metadata','excluded-directory','blocked-link','blocked-special','blocked-read'}:raise ValueError('unsupported inventory entry kind')
        rows=ledger.get('files')
        if not isinstance(rows,list):raise ValueError('ledger files must be a list of per-file reading records')
        by_path={}
        for row in rows:
            if not isinstance(row,dict) or not isinstance(row.get('path'),str):raise ValueError('each ledger record needs a path')
            if row['path'] in by_path:raise ValueError('duplicate ledger record')
            by_path[row['path']]=row
        snapshot=inventory['files']
        current=collect(Path(inventory['root']),inventory['excluded'],{path_key(p) for p in inventory['artifact_paths']})
        problems=[]
        if current!=snapshot:problems.append('repository_changed: rescan and review every added/changed/removed entry')
        for entry in snapshot:
            path=entry['path'];row=by_path.get(path,{})
            if entry['kind'].startswith('blocked'):
                problems.append(path+': unresolved inaccessible or redirected entry');continue
            expected='excluded' if entry['kind']=='excluded-directory' else 'reviewed'
            if row.get('status')!=expected or not isinstance(row.get('summary'),str) or not row['summary'].strip() or not isinstance(row.get('evidence'),str) or not row['evidence'].strip():
                problems.append(path+': missing per-entry reading summary/evidence/status');continue
            if row.get('fingerprint')!=entry.get('sha256',str(entry.get('mtime_ns','excluded'))):
                problems.append(path+': stale reading fingerprint')
        extra=set(by_path)-{x['path'] for x in snapshot}
        if extra:problems.append('ledger contains unknown paths')
        print(json.dumps({'gate_passed':not problems,'problems':problems,'note':'A complete ledger is self-reported evidence, not proof of semantic understanding.'},ensure_ascii=False,indent=2))
        return 0 if not problems else 2
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print('audit error: '+str(exc),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
