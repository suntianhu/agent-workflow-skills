"""Explicit-path time calibration; no network, installation, or task execution."""
import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import statistics
import sys


def minutes(value):
    result = float(value)
    if not math.isfinite(result) or result < 0:
        raise argparse.ArgumentTypeError('分钟必须为有限非负数')
    return result


def positive(value):
    result = minutes(value)
    if result <= 0:
        raise argparse.ArgumentTypeError('必须大于零')
    return result


def read_history(path):
    if path is None or not path.exists():
        return []
    rows = []
    for number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, dict) or row.get('schema') != 1:
            raise ValueError(f'历史第 {number} 行的格式或版本不支持')
        if not isinstance(row.get('kind'), str) or not row['kind'].strip():
            raise ValueError(f'历史第 {number} 行缺少任务类别')
        for key in ('raw_work_minutes', 'actual_work_minutes', 'checks_minutes', 'review_minutes', 'local_elapsed_minutes', 'external_wait_minutes', 'user_wait_minutes'):
            value = row.get(key)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                raise ValueError(f'历史第 {number} 行字段 {key} 无效')
        if row['raw_work_minutes'] <= 0 or row['actual_work_minutes'] <= 0:
            raise ValueError(f'历史第 {number} 行的实现分钟必须大于零')
        rows.append(row)
    return rows


def forecast(args):
    rows = [r for r in read_history(args.history) if r['kind'] == args.kind][-10:]
    ratios = [r['actual_work_minutes'] / r['raw_work_minutes'] for r in rows]
    measured = len(ratios) >= 3
    factor = statistics.median(ratios) if measured else (args.prior if args.prior is not None else 1.0)
    fixed = args.checks + args.review
    likely = args.work * factor + fixed
    if measured:
        ordered = sorted(ratios)
        low_factor = ordered[math.floor((len(ordered) - 1) * 0.2)]
        high_factor = ordered[math.ceil((len(ordered) - 1) * 0.8)]
        spread_method = '最近同类样本的20%至80%顺序统计范围；不是概率保证'
    else:
        low_factor, high_factor = factor * 0.8, factor * 1.3
        spread_method = '先验的0.8至1.3倍启发式范围；不是实测置信区间'
    return {
        'kind': args.kind,
        'raw_work_minutes': args.work,
        'calibration_factor': round(factor, 4),
        'basis': 'recent_same_kind_median' if measured else ('explicit_prior_only' if args.prior is not None else 'default_uncalibrated'),
        'comparable_samples': len(rows),
        'local_minutes': {'low': round(args.work * low_factor + fixed, 1), 'likely': round(likely, 1), 'high': round(args.work * high_factor + fixed, 1)},
        'checks_minutes': args.checks,
        'review_minutes': args.review,
        'range_method': spread_method,
        'unknowns': args.unknown,
        'external_completion': '未估算，须根据真实权限与外部响应单独报告',
        'note': '仅对校准前的剩余实现时间应用系数。检查与审查按非重叠墙钟输入；未知阶段未计入，结果不代表完整承诺。',
    }


def record(args):
    # Validate old records before appending; never silently discard bad history.
    read_history(args.history)
    row = {
        'schema': 1, 'recorded_at': datetime.now(timezone.utc).isoformat(),
        'kind': args.kind, 'raw_work_minutes': args.raw_work,
        'actual_work_minutes': args.actual_work, 'checks_minutes': args.checks,
        'review_minutes': args.review, 'local_elapsed_minutes': args.local_elapsed,
        'external_wait_minutes': args.external_wait, 'user_wait_minutes': args.user_wait,
    }
    args.history.parent.mkdir(parents=True, exist_ok=True)
    with args.history.open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(row, ensure_ascii=False, allow_nan=False) + '\n')
    return {'recorded': True, 'history': str(args.history.resolve()), 'row': row}


def main():
    parser = argparse.ArgumentParser(description='按同类实现实耗校准剩余时间；不会运行任务或修改默认配置。')
    sub = parser.add_subparsers(dest='command', required=True)
    plan = sub.add_parser('forecast', help='只读估算；不写日志')
    plan.add_argument('--kind', required=True, help='同类且同环境的类别名')
    plan.add_argument('--work', required=True, type=minutes, help='校准前的剩余实现分钟')
    plan.add_argument('--checks', required=True, type=minutes, help='预计检查/行为验证的非重叠分钟')
    plan.add_argument('--review', required=True, type=minutes, help='预计审查/清理的非重叠分钟')
    plan.add_argument('--history', type=Path)
    plan.add_argument('--prior', type=positive, default=None, help='不足3个样本时的主观先验；省略时为未校准1.0，仅当前用户明确反馈估时约两倍时可暂用0.5')
    plan.add_argument('--unknown', action='append', default=[], help='未计入的未知阶段，可重复')
    save = sub.add_parser('record', help='只追加到明确指定的JSONL路径；不得伪造样本')
    save.add_argument('--kind', required=True)
    save.add_argument('--history', type=Path, required=True)
    save.add_argument('--raw-work', type=positive, required=True, help='当时校准前的实现预估')
    save.add_argument('--actual-work', type=positive, required=True)
    save.add_argument('--checks', type=minutes, required=True)
    save.add_argument('--review', type=minutes, required=True)
    save.add_argument('--local-elapsed', type=minutes, required=True, help='实际本地墙钟，重叠时不等于各阶段之和')
    save.add_argument('--external-wait', type=minutes, default=0)
    save.add_argument('--user-wait', type=minutes, default=0)
    args = parser.parse_args()
    if not args.kind.strip():
        parser.error('任务类别不能为空')
    try:
        result = forecast(args) if args.command == 'forecast' else record(args)
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (OSError, ValueError) as exc:
        print(f'估时工具失败：{exc}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
