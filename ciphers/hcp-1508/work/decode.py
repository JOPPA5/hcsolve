#!/usr/bin/env python3
"""Decode a manual image transcription, preserving unresolved numbers."""
from pathlib import Path
import re, hashlib, json
base = Path(__file__).resolve().parents[1]
key = {1:"M",2:"K",3:"E",4:"R",5:"V",6:"L",7:"O",8:"T",
       9:"P",10:"S",11:"F",12:"A",13:"G",16:"U",17:"I",
       18:"D",20:"C",21:"W",22:"H",24:"X",25:"N",26:"Y",15:"B"}
assert len(set(key.values())) == len(key)
expected = json.loads((base/"work/source-sha256.json").read_text())
for name, digest in expected.items():
    assert hashlib.sha256((base/"source"/name).read_bytes()).hexdigest() == digest
raw=(base/"work/transcription.txt").read_text()
count=0
def word(s):
    global count
    if s.startswith("{"): return s[1:-1]
    out=""
    for t in s.split("."):
        if not t: continue
        count+=1
        if t.isdigit(): out+=key.get(int(t),f"[{t}?]")
        elif t.startswith('[') and t.endswith(']'):
            choices=t[1:-1].split('|')
            out+='['+'|'.join(key.get(int(c),c+'?') if c.isdigit() else c for c in choices)+']'
        else: out+=t
    return out
for line in raw.splitlines():
    print(" ".join(word(s.strip()) for s in line.split(" / ")))
print(f"Numeric positions: {count}")
print("Unmapped number 23 and BELL/BELT's final 6|8 remain unresolved.")
print("Literal EKRA is preserved; EZRA is not a key-consistent reading.")
