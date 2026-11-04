#!/usr/bin/env python3
"""hcp-1012: number substitution, 25-letter alphabet without J, A=7 ... Z=31 (position + 6).
Run from repo root:  python3 -I ciphers/hcp-1012/work/decode.py
"""
import hashlib, os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
    "source/picture-large.jpg": "413d2a022d2c867982941e9d9021c2c3eff8fd6d8722b99e62c36dd31bcbdc44",
    "source/address-large.jpg": "fba06d4a62b4448405f193dec5c25b0528901f66d0c36f27f69991bc130556d4",
    "work/hires/cpc_-11-12_DE_Hof_DE_Selb__pic.jpg": "4953507314e90a4994b43646676eda6672f5d138d7255b1088cee871703d437f",
    "work/hires/cpc_-11-12_DE_Hof_DE_Selb__adr.jpg": "60aa0e4663b6d7b9d64668e766b5ec2d4cc23441fc1c9a4d5342a9ccfdf9560b",
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    print(("OK  " if got == h else "BAD ") + p)
    ok &= got == h
if not ok:
    sys.exit("source hash mismatch")

ALPHA = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # no J
KEY = {i + 7: ch for i, ch in enumerate(ALPHA)}  # A=7 ... Z=31

def word(tok):
    if tok.startswith("[") and tok.endswith("]"):
        return tok[1:-1]
    out = []
    for part in tok.split("."):
        m = re.fullmatch(r"\{(.+)\}", part)
        u = re.fullmatch(r"(\d+)\^", part)  # cipher number with an umlaut mark above it
        if m:
            out.append(m.group(1))
        elif u:
            out.append({"a": "ä", "o": "ö", "u": "ü"}[KEY[int(u.group(1))].lower()])
        else:
            out.append(KEY[int(part)].lower())
    return "".join(out)

print()
for line in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    print(" ".join(t if t in ",.!" else word(t) for t in line.split()))
