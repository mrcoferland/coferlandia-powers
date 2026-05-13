#!/usr/bin/env python3
"""Export a markdown report into dist/ or another output directory."""
from __future__ import annotations

import argparse
import shutil
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a markdown report.")
    parser.add_argument("input", help="Input markdown report path")
    parser.add_argument("--out-dir", default="dist", help="Output directory, default: dist")
    parser.add_argument("--timestamp", action="store_true", help="Prefix exported filename with UTC timestamp")
    args = parser.parse_args()

    src = Path(args.input)
    if not src.exists() or not src.is_file():
        parser.error(f"input file does not exist: {src}")
    if src.suffix.lower() not in {".md", ".markdown"}:
        parser.error("input file must be markdown")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    name = src.name
    if args.timestamp:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        name = f"{stamp}-{name}"
    dst = out_dir / name
    shutil.copy2(src, dst)
    print(f"Exported {src} -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
