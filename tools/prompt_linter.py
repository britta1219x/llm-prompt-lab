#!/usr/bin/env python3
"""A tiny, dependency-free checker for prompt Markdown files."""

from pathlib import Path
import sys

REQUIRED_SECTIONS = ("# 角色", "# 工作方式", "# 约束", "# 输入")


def lint(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues = []
    if not text.startswith("---\n"):
        issues.append("缺少 YAML 元数据块")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            issues.append(f"缺少章节：{section}")
    if "{{" not in text:
        issues.append("没有输入变量，例如 {{text}}")
    return issues


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "prompts")
    files = sorted(root.rglob("*.md"))
    if not files:
        print(f"未找到 Markdown 提示词：{root}")
        return 1

    failed = False
    for file in files:
        issues = lint(file)
        if issues:
            failed = True
            print(f"FAIL  {file}")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"PASS  {file}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
