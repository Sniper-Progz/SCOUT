"""Guardrails against accidental IVY coupling."""

from __future__ import annotations

import ast
from pathlib import Path


def test_no_python_import_references_ivy_source() -> None:
    root = Path("src")
    forbidden = {"ivy"}

    for path in root.rglob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    assert alias.name.split(".", 1)[0].lower() not in forbidden
            elif isinstance(node, ast.ImportFrom) and node.module is not None:
                assert node.module.split(".", 1)[0].lower() not in forbidden
