#!/usr/bin/env python3
"""hcp-1505: reversed numeric alphabet (1=Z ... 26=A). Run from repo root:
python3 -I ciphers/hcp-1505/work/decode2.py"""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, h in json.loads((p / "work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p / "source" / name).read_bytes()).hexdigest() == h, name
print("source hashes OK")
key = {n: chr(91 - n) for n in range(1, 27)}
lines = []
n = rest = 0
for line in (p / "work/transcription-v2.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    words = []
    for w in line.split(" / "):
        s = ""
        for t in w.split("."):
            n += 1
            if t.endswith("r"):
                rest += 1
                s += key[int(t[:-1])].lower()  # lower case = restored sign
            else:
                s += key[int(t)]
        words.append(s)
    lines.append(" ".join(words))
print("--- literal decryption (lower case = restored) ---")
print("\n".join(lines))
lit = " ".join(lines).upper()
# Sender's slip: R written as 18 (its forward position, = I in this key) in LETTER, TOMORROW
norm = lit.replace("LETTEI", "LETTER").replace("TOMOIIOW", "TOMORROW")
print("--- normalised (sender's R->18 slip corrected) ---")
print(norm)
print(f"signs: {n}, restored: {rest}")
