#!/usr/bin/env python3
"""hcp-1381: checks source hashes, decodes transcription.json with Caesar -1. Run from repo root."""
import hashlib, json, sys
from pathlib import Path
base = Path("ciphers/hcp-1381")
H = {"source/picture-large.jpg":"5e7561399632324c40ca8625380aa63383bfb93b0ba94926a8db7fab3b330fcd",
     "source/address-large.jpg":"cbb754e248c08cac45f2210de111be665e991c41b4935cfda1f1b00383a007c0",
     "work/hires/pc_hcp_62_pic.JPG":"5f58e2692b2e66c8992c6d6ef4f18fc6662bea733eebde0c3165a63457db26e5",
     "work/hires/pc_hcp_62_adr.JPG":"70c5daa28e78c6f5a0b946f7cb229f5b47420d294c69f30b6f3c71dee1dc4859"}
for f, h in H.items():
    if hashlib.sha256((base/f).read_bytes()).hexdigest() != h:
        sys.exit("HASH MISMATCH " + f)
print("source hashes OK")
def sh(s, k):
    return "".join(chr((ord(c.lower())-97+k) % 26 + 97) if c.isalpha() else c for c in s)
t = json.loads((base/"work/transcription.json").read_text())
n = lit = 0
print("[plain]", t["plain_heading"])
for line in t["lines"]:
    out = []
    for tok, keep in line:
        if keep:
            out.append("[" + tok + "]"); lit += sum(c.isalpha() for c in tok)
        else:
            p = sh(tok, -1); assert sh(p, 1) == tok.lower()
            out.append(p.upper()); n += sum(c.isalpha() for c in tok)
    print(" ".join(out))
print("[plain]", t["plain_date"])
print(f"enciphered letters decoded: {n}; literal abbreviation letters: {lit}")
