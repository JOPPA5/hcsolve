#!/usr/bin/env python3
"""hcp-1486: verify source hashes, then read the reversed-writing transcription.
Run from repo root:  python3 -I ciphers/hcp-1486/work/decode.py"""
import hashlib, pathlib, re, sys
D = pathlib.Path(__file__).resolve().parent.parent
H = {"source/address-large.jpg": "f83abcfa7b846b38c74401af837b9cd2401f6edfad4890d396d84b29549aac63",
     "source/picture-large.jpg": "29fc5eb81850b6de42a82abf5d27ec5ea8f982359b774feca1636fc1fb76d2a9",
     "source/metadata.md": "f0d9aae19a0fe0cd8c69a373018c5cdcdd8c315ed4e6b91fb3f63caed3b7614e"}
for f, h in H.items():
    got = hashlib.sha256((D / f).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f"HASH MISMATCH {f}")
print("source hashes OK")
FIXED = {"X": "a", "A": "a", "W": "w", "N": "n", "L": "l", "S": "S", "F": "f", "D": "D", "U": "u"}
def tok(line):
    return re.findall(r"\[[A-Z](?::[A-Za-z])?\]|[a-z]|\|", line)
def val(t):
    if t.startswith("["):
        k = t[1:-1]
        return k.split(":")[1] if ":" in k else FIXED[k]
    return t
out = []
for raw in (D / "work/transcription.txt").read_text().splitlines():
    m = re.match(r"L(\d): (.*)", raw)
    if not m:
        continue
    toks = [t for t in tok(m.group(2))][::-1]          # read right-to-left; dots dropped
    words = "".join(" " if t == "|" else val(t) for t in toks).split()
    print(f"L{m.group(1)}: {' '.join(words)}")
    out += words
print("\nRunning text:", " ".join(out), "| S.W.A.K. Will")
