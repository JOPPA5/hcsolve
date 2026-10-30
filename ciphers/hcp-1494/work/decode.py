#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parents[1]
key=json.loads((p/"work/key.json").read_text())
for name,h in json.loads((p/"work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p/"source"/name).read_bytes()).hexdigest()==h
count=0;ambiguous=0
for line in (p/"work/transcription.txt").read_text().splitlines():
    out=[]
    for word in line.split(" / "):
        if word.startswith("{"):out.append(word[1:-1]);continue
        result=""
        for t in word.split():
            count+=1
            if t.startswith("["):
                ambiguous+=1
                result+="["+"|".join(key[x] for x in t[1:-1].split("|"))+"]"
            else:result+=key[t]
        out.append(result)
    print(" ".join(out))
print("Cipher positions:",count,"ambiguous:",ambiguous)
print("Source hashes passed; manual transcription, not OCR.")
