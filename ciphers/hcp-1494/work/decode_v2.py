#!/usr/bin/env python3
"""hcp-1494: decode transcription-v2.txt with key.json; verify source hashes.
Run from repo root: python3 -I ciphers/hcp-1494/work/decode_v2.py"""
from pathlib import Path
import json, hashlib
p = Path(__file__).resolve().parents[1]
key = json.loads((p / "work/key.json").read_text())
for name, h in json.loads((p / "work/source-sha256.json").read_text()).items():
    got = hashlib.sha256((p / "source" / name).read_bytes()).hexdigest()
    assert got == h, f"hash mismatch: {name}"

def tok(t):
    """return (literal, normalised) for one token"""
    intended = None
    if ">" in t:
        t, intended = t.split(">", 1)
    alts = [key[x] for x in t.split("|")]
    lit = alts[0] if len(alts) == 1 else "[" + "|".join(alts) + "]"
    norm = alts[0] if intended is None else intended
    return lit, norm

n = slips = alts = 0
L, N = [], []
for line in (p / "work/transcription-v2.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    lw, nw = [], []
    for w in line.split(" / "):
        if w.startswith("{") or w.startswith("<"):
            s = w[1:-1] if w.startswith("{") else w
            lw.append(s); nw.append(s if w.startswith("{") else ""); continue
        a = b = ""
        for t in w.split():
            n += 1
            slips += ">" in t
            alts += "|" in t.split(">")[0]
            x, y = tok(t); a += x; b += y
        lw.append(a); nw.append(b)
    L.append(" ".join(lw)); N.append(" ".join(x for x in nw if x))
print("== literal (sign by sign) ==")
print("\n".join(L))
print("\n== normalised plaintext ==")
print("\n".join(N))
print(f"\ncipher signs: {n}; with alternative readings: {alts}; writer slips/extra signs: {slips}")
print("source hashes OK (manual transcription, not OCR)")
