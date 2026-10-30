#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parents[1]
for name,h in json.loads((p/"work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p/"source"/name).read_bytes()).hexdigest()==h
raw=(p/"work/transcription.txt").read_text()
def shift(s,n):
    out=""
    for c in s:
        if "a"<=c<="z":out+=chr((ord(c)-97+n)%26+97)
        elif "A"<=c<="Z":out+=chr((ord(c)-65+n)%26+65)
        else:out+=c
    return out
plain=shift(raw,-1)
assert shift(plain,1)==raw
print(plain,end="")
print("Encrypted letters:",sum(c.isascii() and c.isalpha() for c in raw))
print("Source hashes and full inverse-key roundtrip passed.")
if "--all-shifts" in __import__("sys").argv:
    for n in range(26):print(f"shift +{n}: "+shift(raw,n).replace("\n"," / "))
