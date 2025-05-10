#!/usr/bin/env python3
"""
Merge multiple BrainMap Sleuth-exported .txt files into one,
skipping redundant reference headers after the first file.

Usage:
    python scripts/merge_brainmap_coordinates.py
"""

from pathlib import Path

# === Path definitions ===
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'data' / 'BrainMap'
DST = SRC / 'fmir_all.txt'

# === Merge logic ===
def merge_txt_files(source_folder: Path, output_file: Path):
    files = sorted(source_folder.glob('*.txt'))
    if not files:
        print("⚠ No .txt files found in", source_folder)
        return

    with open(output_file, 'w', encoding='utf-8') as out:
        first = True
        for file in files:
            lines = file.read_text(encoding='utf-8', errors='ignore').splitlines()
            for line in lines:
                if line.startswith('// Reference') and not first:
                    continue
                out.write(line + '\n')
            first = False

    print(f"✓ FINISH → Merged {len(files)} files into {output_file}")

# === Run ===
if __name__ == "__main__":
    merge_txt_files(SRC, DST)