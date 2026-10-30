#!/usr/bin/env python3
"""HCP 1356: verify source hashes, decode work/transcription.txt with Caesar -1.
Letters in [brackets] are disclosed restorations under a physical blot."""
import hashlib, pathlib, re, sys
base = pathlib.Path(__file__).resolve().parent.parent
H = {"source/picture-large.jpg": "6e765ae952aaea35929d099d48ac9949ca33a7feafd708d72b50802b83e48621",
     "source/address-large.jpg": "9f982b8df8dd268101c6cfe5b999ec35f7ae9b09aeb02cb613f50ee8c5838b5d",
     "work/hires/pc_hcp_37_pic.JPG": "7b173cf1f12e8f17d3ca417a023c1da8d01f76c011c01e296302360e05a89cb3",
     "work/hires/pc_hcp_37_adr.JPG": "14a9bac6e0a30a991ec225e5d196dbac85e59aefe65492a988b57b2390132e12"}
for f, h in H.items():
    got = hashlib.sha256((base / f).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f"HASH MISMATCH {f}")
print("source hashes OK (4 files)")
def shift(c, k):
    if c.isupper(): return chr((ord(c) - 65 + k) % 26 + 65)
    if c.islower(): return chr((ord(c) - 97 + k) % 26 + 97)
    return c
lines = (base / "work/transcription.txt").read_text().splitlines()
print("plain heading (not enciphered): Sunday 24th")
n = r = 0
out = []
for l in lines:
    p = "".join(shift(c, -1) for c in l)
    assert "".join(shift(c, 1) for c in p) == l
    n += len(re.findall(r"[A-Za-z]", l)); r += len(re.findall(r"\[[a-z]\]", l))
    out.append(p)
    print(f"{l:28} -> {p}")
print(f"{n} cipher letters ({r} restored under blots, {n-r} read from the pixels)")
print("PLAINTEXT:", " ".join(re.sub(r"[\[\].]", "", p) for p in out).upper())
