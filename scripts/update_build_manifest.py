#!/usr/bin/env python3
"""Create or verify checksums for the files shared by every distribution."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "metadata" / "build_manifest.csv"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def rows() -> list[dict[str, object]]:
    paths = sorted((ROOT / "data" / "parquet").glob("*.parquet"))
    paths.extend(
        sorted(
            path
            for path in (ROOT / "metadata").glob("*")
            if path.is_file() and path != MANIFEST
        )
    )
    return [
        {
            "relative_path": path.relative_to(ROOT).as_posix(),
            "size_bytes": path.stat().st_size,
            "sha256": digest(path),
        }
        for path in paths
    ]


def render(records: list[dict[str, object]]) -> str:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(
        stream, fieldnames=("relative_path", "size_bytes", "sha256"), lineterminator="\n"
    )
    writer.writeheader()
    writer.writerows(records)
    return stream.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render(rows())
    if args.check:
        actual = MANIFEST.read_text(encoding="utf-8")
        if actual != expected:
            raise SystemExit("metadata/build_manifest.csv is stale")
        print("Build manifest: PASS")
        return
    MANIFEST.write_text(expected, encoding="utf-8")
    print(f"Wrote {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
