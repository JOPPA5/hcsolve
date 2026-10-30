#!/usr/bin/env python3
"""hcp-1828: verify source hashes, then decode. Run from the repo root:
python3 -I ciphers/hcp-1828/work/decode.py"""
import hashlib, json, os, sys, collections
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
H = {"source/picture-large.jpg": "1b75c88115b042673b9341b793c98c6bca71a1a07f6520b434e6e48a9d7a2906",
     "source/address-large.jpg": "a4b769987ce605fe29b228c5219298c75b8a08d893a7eec43e1aaef9765b4f1e",
     "work/hires/pc_hcp_509_pic.JPG": "a4b37f97fb057b4021e1a3787806d805163377212b01c7c20013457a1952da54",
     "work/hires/pc_hcp_509_adr.JPG": "77f3522453857ea9f8fb1b0d682ade41c52bd5bc62cbcbd177acf08af91d4d80"}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), "rb").read()).hexdigest() != h:
        sys.exit("HASH MISMATCH " + p)
print("source hashes OK")
key = json.load(open(os.path.join(D, "work/key.json")))
if len(set(key.values())) != len(key): sys.exit("key is not one-to-one")
rows = [l.split() for l in open(os.path.join(D, "work/transcription.txt")) if l.strip() and not l.startswith("#")]
assert len(rows) == 10
# Reading order: card turned 180 degrees = last row first, each row right to left.
lines = ["".join(key[s] for s in reversed(r)) for r in reversed(rows)]
for n, l in zip(range(10, 0, -1), lines): print(f"R{n:<2} {l}")
text = "".join(lines)
words = ("THANKS FOR CARD A BEAUTY SEND ANYTHING IN THE CASTLE OR RUIN LINE WHEN YOU "
         "CANT GET ANY MORE ACTRESSES WITH LOVE FROM ADE")
assert words.replace(" ", "") == text, "segmentation does not match"
print(len(text), "signs,", len(key), "distinct; none unread")
print(words)
c = collections.Counter(s for r in rows for s in r)
print("unused key entries:", sorted(set(key) - set(c)))
