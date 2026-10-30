#!/usr/bin/env python3
"""HCP 1379: check source hashes, decode with Caesar -1, verify the inverse. Run from repo root: python3 -I ciphers/hcp-1379/work/decode.py"""
import datetime, hashlib, json, pathlib, sys
D = pathlib.Path(sys.argv[0]).resolve().parent.parent
H = {"source/picture-large.jpg": "702c0e99aa906c7e9ddee907ef46bb99e49ed9712aedd8b030b4a9946c9716b9",
     "source/address-large.jpg": "108001b2acd0b5df56fdec3af501168f28f3f15d725adeae145028dc6ff51c6b",
     "work/hires/pc_hcp_60_pic.JPG": "f062cfe891761813ced5aae4acb1cd1d871e2ce053d9119db9126e307da5c9ae",
     "work/hires/pc_hcp_60_adr.JPG": "3cd08cdb3b7c165cedec267dfe44894a307f9faedbfe38b67e262ac163b211cc"}
for p, h in H.items():
    assert hashlib.sha256((D / p).read_bytes()).hexdigest() == h, p
print("source hashes OK:", len(H))
def shift(s, k):
    return "".join(chr((ord(c.upper()) - 65 + k) % 26 + 65) if c.isalpha() else c for c in s)
T = json.loads((D / "work/transcription.json").read_text())
n = 0
for line in T["lines"]:
    plain = [shift(w, -1) for w in line]
    for w, p in zip(line, plain):
        assert shift(p, 1) == w.upper()
        n += sum(c.isalpha() for c in w)
    print(" ".join(line).ljust(26), "|", " ".join(plain))
print("enciphered letters decoded:", n)
print("plain heading (not enciphered):", T["heading_plain"], "| 1907-04-09 is a", datetime.date(1907, 4, 9).strftime("%A"))
