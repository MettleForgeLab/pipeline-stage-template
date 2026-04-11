#!/usr/bin/env python3
"""
lens.py

Minimal runnable lens template.

This module demonstrates the canonical shape of a DataDiddler lens:
- parse CLI arguments
- validate input path existence
- create output directory
- write at least one output file
- return 0 on success

It does not implement domain logic.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict


def write_ndjson_line(path: Path, row: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(prog="lens-template", add_help=True)
    ap.add_argument("--in", dest="input_path", required=True, help="Input file path")
    ap.add_argument("--out-dir", required=True, help="Output directory")
    args = ap.parse_args()

    input_path = Path(args.input_path).resolve()
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        raise SystemExit(f"Input path does not exist: {input_path}")

    output_path = out_dir / "lens_output.ndjson"
    write_ndjson_line(
        output_path,
        {
            "source_path": str(input_path),
            "status": "ok",
            "template": True,
        },
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())