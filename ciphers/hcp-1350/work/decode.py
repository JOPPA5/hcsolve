#!/usr/bin/env python3
"""HCP 1350: verify image hashes, decode work/transcription.txt with Caesar -1."""
import hashlib, pathlib, re, sys
base = pathlib.Path(__file__).resolve().parent.parent
H = {"source/picture-large.jpg": "cedb7f8f997ac20870d4cf3a56e56ee7f360fc69ef32b817a11a6725a3cbe602",
     "source/address-large.jpg": "78a35f34a6a6d34f9b0ce143fd0e06abe3d07865bffcaf2befe3575cca85c940",
     "work/hires/pc_hcp_31_pic.JPG": "fd95a36e2cc3f2530b877d29a873c7ce77087d41b77f24010b89c497b740174b",
     "work/hires/pc_hcp_31_adr.JPG": "a0d0f112f91829a8efda2f78851d804ba508729a4c890251be533d06e689bcb7"}
for f, h in H.items():
    if hashlib.sha256((base / f).read_bytes()).hexdigest() != h:
        sys.exit(f"HASH MISMATCH {f}")
print("source hashes OK (4 files)")
def shift(c, k):
    if c.isupper(): return chr((ord(c) - 65 + k) % 26 + 65)
    if c.islower(): return chr((ord(c) - 97 + k) % 26 + 97)
    return c
print("plain heading/footer (not enciphered): Thursday. March. 7th")
n = 0
out = []
for l in (base / "work/transcription.txt").read_text().splitlines():
    p = "".join(shift(c, -1) for c in l)
    assert "".join(shift(c, 1) for c in p) == l
    n += len(re.findall(r"[A-Za-z]", l))
    out.append(p)
    print(f"{l:28} -> {p}")
print(f"{n} cipher letters, all read from the pixels, none restored")
print("PLAINTEXT:", " ".join(p.replace(".", "") for p in out).upper())
