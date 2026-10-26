#!/usr/bin/env python3
"""Undo false word divisions without changing, adding, or permuting letters."""
from pathlib import Path
import hashlib,json,re
p=Path(__file__).resolve().parents[1]
for name,h in json.loads((p/"work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p/"source"/name).read_bytes()).hexdigest()==h
raw=(p/"work/transcription.txt").read_text()
letters="".join(raw.split())
words=(p/"work/words.txt").read_text().split()
assert letters=="".join(words), "Proposed spacing must preserve every letter in order"
pos=0;out=[]
for word in words:
    out.append(letters[pos:pos+len(word)]);pos+=len(word)
assert pos==len(letters)
print(" ".join(out))
print("Letters:",len(letters))
print("Original line lengths:",[len("".join(s.split())) for s in raw.splitlines()])
print("All source hashes passed. Exact ordered-letter equality passed.")
