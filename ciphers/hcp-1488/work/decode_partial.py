#!/usr/bin/env python3
"""Run from repo root: python3 -I ciphers/hcp-1488/work/decode_partial.py
Checks source hashes, then ROT13-decodes the partial line transcription."""
from pathlib import Path
import codecs, hashlib, json, re
p = Path(__file__).resolve().parents[1]
for name, h in json.loads((p/"work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p/"source"/name).read_bytes()).hexdigest() == h, name
print("source hashes OK")
n = 0
for line in (p/"work/transcription-partial.txt").read_text().splitlines():
    if not line.startswith("L"): continue
    tag, ct = line.split(": ", 1)
    parts = re.split(r"(\[[^\]]*\])", ct)
    pt = "".join(x if x.startswith("[") else codecs.decode(x, "rot_13") for x in parts)
    n += sum(c.isalpha() for x in parts if not x.startswith("[") for c in x)
    print(f"{tag:4} {ct:32} -> {pt}")
print("letters decoded:", n, "| lines 4-5 incomplete: PARTIAL")
