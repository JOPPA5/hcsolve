"""Partial decode of HCP 1448. Run from repo root:
   python3 -I ciphers/hcp-1448/work/decode_partial.py
Checks source hashes, then applies the digit key (vowels 1-5, l m n s 6-9; all other letters plain)."""
import hashlib, json, pathlib, sys
d = pathlib.Path(__file__).resolve().parent
src = d.parent / "source"
for name, h in json.loads((d / "source-sha256.json").read_text()).items():
    p = src / pathlib.Path(name).name
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    print(("OK  " if got == h else "BAD ") + p.name)
    if got != h: sys.exit(1)
KEY = dict(zip("123456789", "aeioulmns"))
for line in (d / "transcript_partial.txt").read_text().splitlines():
    if line.startswith("#"): continue
    print("".join(KEY.get(c, c) for c in line))
