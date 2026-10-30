#!/usr/bin/env python3
"""Numeric reverse alphabet; preserves uncertain image readings."""
from pathlib import Path
import hashlib,json,re
p=Path(__file__).resolve().parents[1]
key={n:chr(91-n) for n in range(1,27)}
for name,h in json.loads((p/"work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p/"source"/name).read_bytes()).hexdigest()==h
count=0;ambiguous=0
for line in (p/"work/transcription.txt").read_text().splitlines():
    words=[]
    for word in line.split(" / "):
        out=[]
        for token in word.split("."):
            count+=1
            if token.startswith("["):
                ambiguous+=1
                out.append("["+"|".join(key[int(n)] for n in token[1:-1].split("|"))+"]")
            else: out.append(key[int(token)])
        words.append("".join(out))
    print(" ".join(words))
print("Numeric positions:",count,"ambiguous:",ambiguous)
print("Source hashes verified. Manual transcription, not OCR.")
