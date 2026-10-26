#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parents[1]
key=dict(zip(
"BR0 BR1 B0 B1 BL0 BL1 R0 R1 C0 C1 L0 L1 TR0 TR1 T0 T1 TL0 TL1 V0 V1 >0 >1 <0 <1 ^0 ^1".split(),
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
for name,h in json.loads((p/"work/source-sha256.json").read_text()).items():
    assert hashlib.sha256((p/"source"/name).read_bytes()).hexdigest()==h
inv={v:k for k,v in key.items()}
count=0
for line in (p/"work/transcription.txt").read_text().splitlines():
    tokens=line.split();word="".join(key[t] for t in tokens)
    assert [inv[c] for c in word]==tokens
    count+=len(tokens);print(word)
print("Encrypted glyphs:",count)
print("Source hashes and inverse-key roundtrip passed.")
