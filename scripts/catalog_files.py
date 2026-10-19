"""Catalog schemas, safe paths and deterministic generated content."""
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def relative_name(value):
    if not isinstance(value, str) or not value:
        raise ValueError("resource path must be a nonempty string")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError("resource path must be portable and relative")
    if not path.parts or any(not re.fullmatch(r"[A-Za-z0-9._-]+", part) for part in path.parts):
        raise ValueError("invalid portable resource path: " + value)
    return path.as_posix()


def no_links(path):
    path = Path(path).absolute()
    for part in [*reversed(path.parents), path]:
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        flags = getattr(info, "st_file_attributes", 0)
        if stat.S_ISLNK(info.st_mode) or flags & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400):
            raise ValueError("linked or redirected path is not allowed: " + str(part))


def safe_path(root, relative):
    value = relative_name(relative)
    target = Path(root).absolute().joinpath(*PurePosixPath(value).parts)
    no_links(target)
    if not target.resolve().is_relative_to(Path(root).resolve()):
        raise ValueError("resource outside expected root")
    return target


def existing_files(folder, exclude_dirs=()):
    folder = Path(folder)
    no_links(folder)
    result = set()
    if not folder.exists():
        return result
    def failed(error):
        raise error
    for directory, dirs, names in os.walk(folder, followlinks=False, onerror=failed):
        dirs[:] = [name for name in dirs if name not in exclude_dirs]
        names = [name for name in names if name not in exclude_dirs]
        for name in dirs + names:
            no_links(Path(directory) / name)
        for name in names:
            path = Path(directory) / name
            if not path.is_file():
                raise ValueError("nonregular resource: " + str(path))
            result.add(path.relative_to(folder).as_posix())
    return result


def expected_files(row):
    result = {"SKILL.md", "LICENSE", "agents/openai.yaml"}
    for ref in row["references"]:
        path = relative_name("references/" + ref)
        if path in result:
            raise ValueError("duplicate reference path")
        result.add(path)
    for source, target in row["resources"].items():
        relative_name(source)
        target = relative_name(target)
        if target.split("/")[0] not in {"assets", "scripts"} or target in result:
            raise ValueError("conflicting resource destination: " + target)
        result.add(target)
    for name in result:
        if any(parent.as_posix() in result for parent in PurePosixPath(name).parents if parent.as_posix() != "."):
            raise ValueError("file/directory declaration conflict: " + name)
    return result


def load_catalog(root):
    doc = read_json(safe_path(root, "catalog.json"))
    if not isinstance(doc, dict) or doc.get("schema") != 1 or not isinstance(doc.get("skills"), list):
        raise ValueError("unsupported catalog schema")
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", str(doc.get("version", ""))):
        raise ValueError("catalog requires a semantic version")
    names = set()
    for row in doc["skills"]:
        if not isinstance(row, dict):
            raise ValueError("skill must be an object")
        name = row.get("name", "")
        if not isinstance(name, str) or len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in names:
            raise ValueError("invalid or duplicate skill name")
        names.add(name)
        for field in ("title", "description", "goal", "gate", "outputs"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(name + ": invalid " + field)
        if len(row["description"]) > 1024:
            raise ValueError(name + ": description too long")
        for field in ("steps", "references"):
            if not isinstance(row.get(field), list) or not row[field] or not all(isinstance(x, str) and x.strip() for x in row[field]):
                raise ValueError(name + ": invalid " + field)
        if len(set(row["references"])) != len(row["references"]) or not isinstance(row.get("resources"), dict):
            raise ValueError(name + ": invalid resources/references")
        conditions = row.get("reference_conditions", {})
        if not isinstance(conditions, dict) or any(
            key not in row["references"] or not isinstance(value, str) or not value.strip()
            for key, value in conditions.items()
        ):
            raise ValueError(name + ": invalid conditional references")
        expected_files(row)
    if not names:
        raise ValueError("catalog cannot be empty")
    return doc


def render_skill(row):
    steps = "\n".join(f"{index}. {value}" for index, value in enumerate(row["steps"], 1))
    conditions = row.get("reference_conditions", {})
    references = "\n".join(
        f"- [{value}](references/{value})：" + conditions.get(value, "触发本技能时读取的基础指南。")
        for value in row["references"]
    )
    resources = "\n".join(f"- [{PurePosixPath(target).name}]({target})：按指南使用；模板按真实项目填写。" for target in row["resources"].values())
    return f"""---
name: {row['name']}
description: {json.dumps(row['description'], ensure_ascii=False)}
license: MIT
---

# {row['title']}

{row['goal']}

## 前置条件与边界

{row['gate']} 遵从当前用户、适用项目规则与宿主权限；不因技能存在扩大任务或外部写入授权，已有授权继续执行。

进入已有项目时读取当前项目规则与既有内部规范，承接已完成的梳理、技能采纳和验证决定。后续启用本技能也先核对这些记录；发现冲突先收敛到同一规范入口，不另起脱节流程。

## 执行

{steps}

## 必须得到的结果

{row['outputs']} 没有证据的项目标为未核实，不补写完成结论。

## 按需资料

{references}
{resources}

本目录可独立复制；缺少其他技能时按本技能前置条件调查/产出，不绕过门禁。组合清单仅描述条件和顺序，不是执行引擎。工具调用使用宿主实际能力，不假定平台专用API。
"""


def render_ui(row):
    values = {
        "display_name": row["title"],
        "short_description": row["title"] + "：按任务边界完成对应能力，保留项目规则、真实证据与可组合流程",
        "default_prompt": "使用 $" + row["name"] + " 完成当前任务，并遵守前置条件和证据要求。",
    }
    return "interface:\n" + "".join("  " + key + ": " + json.dumps(value, ensure_ascii=False) + "\n" for key, value in values.items())


def expected_contents(root, row):
    contents = {
        "SKILL.md": render_skill(row).encode("utf-8"),
        "agents/openai.yaml": render_ui(row).encode("utf-8"),
        "LICENSE": safe_path(root, "LICENSE").read_bytes(),
    }
    for ref in row["references"]:
        contents["references/" + ref] = safe_path(root, "guides/" + ref).read_bytes()
    for source, target in row["resources"].items():
        contents[target] = safe_path(root, source).read_bytes()
    return contents


def check_skill(root, row):
    folder = safe_path(root, "skills/" + row["name"])
    if existing_files(folder) != expected_files(row):
        raise ValueError(row["name"] + ": missing or undeclared files")
    for relative, content in expected_contents(root, row).items():
        if safe_path(folder, relative).read_bytes() != content:
            raise ValueError(row["name"] + ": generated content is stale: " + relative)


def load_bundle(root, name, catalog):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("invalid bundle name")
    doc = read_json(safe_path(root, "bundles/" + name + ".json"))
    if not isinstance(doc, dict) or doc.get("schema") != 2 or doc.get("name") != name:
        raise ValueError("unsupported or mismatched bundle schema")
    if doc.get("kind") != "documented-composition-not-native-executable-workflow" or doc.get("project_mode") not in {"existing", "new", "determine"} or not isinstance(doc.get("execution"), str) or not doc["execution"].strip():
        raise ValueError(name + ": invalid composition metadata")
    known = {row["name"] for row in catalog["skills"]}
    for field in ("skills", "optional"):
        values = doc.get(field)
        if not isinstance(values, list) or not all(isinstance(x, str) for x in values) or len(values) != len(set(values)) or not set(values) <= known:
            raise ValueError(name + ": invalid " + field)
    if set(doc["skills"]) & set(doc["optional"]):
        raise ValueError(name + ": duplicate optional skill")
    stages = doc.get("stages")
    conditions = doc.get("conditions")
    if not isinstance(stages, list) or not stages or not isinstance(conditions, dict) or not all(isinstance(k, str) and k and isinstance(v, str) and v.strip() for k, v in conditions.items()):
        raise ValueError(name + ": missing stage conditions")
    union, ids = [], set()
    test_index = None
    for index, stage in enumerate(stages):
        if not isinstance(stage, dict) or not isinstance(stage.get("id"), str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", stage["id"]) or stage["id"] in ids:
            raise ValueError(name + ": invalid stage id")
        ids.add(stage["id"])
        members = stage.get("skills")
        if not isinstance(members, list) or not members or not all(isinstance(x, str) for x in members) or len(members) != len(set(members)) or not set(members) <= known:
            raise ValueError(name + ": invalid stage skills")
        if stage.get("when") not in conditions:
            raise ValueError(name + ": undefined stage condition")
        constraints = stage.get("implementation_constraints", [])
        if not isinstance(constraints, list) or not all(isinstance(x, str) for x in constraints) or len(constraints) != len(set(constraints)) or not set(constraints) <= set(doc["skills"]):
            raise ValueError(name + ": invalid implementation constraints")
        if "aw-test-strategy" in members:
            test_index = index
        if set(members) & {"aw-frontend-implementation", "aw-backend-implementation", "aw-scoped-tdd"}:
            if test_index is None or test_index >= index:
                raise ValueError(name + ": implementation precedes test strategy")
        union.extend(members)
    if list(dict.fromkeys(union)) != doc["skills"]:
        raise ValueError(name + ": stage/catalog selection differs")
    return doc
