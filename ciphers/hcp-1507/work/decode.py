#!/usr/bin/env python3
"""Manual number transcription; no OCR or silent error correction."""
from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parents[1]
key={1:"M",3:"E",4:"R",6:"L",7:"O",8:"T",9:"P",10:"S",
     11:"F",12:"A",13:"G",14:"K",16:"U",17:"I",18:"D",
     20:"C",21:"W",22:"H",24:"X",25:"N",26:"Y"}
assert len(key)==len(set(key.values()))
for name,h in json.loads((p/"work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p/"source"/name).read_bytes()).hexdigest()==h
inv={v:k for k,v in key.items()}
count=0
for line in (p/"work/transcription.txt").read_text().splitlines():
    out=[]
    for token in line.split(" / "):
        if token.startswith("{"): out.append(token[1:-1]);continue
        nums=list(map(int,token.split(".")))
        plain="".join(key[n] for n in nums)
        assert [inv[c] for c in plain]==nums
        count+=len(nums)
        out.append(plain)
    print(" ".join(out))
print(f"Encrypted numeric positions: {count}")
print("All positions mapped; inverse-key roundtrip passed.")
