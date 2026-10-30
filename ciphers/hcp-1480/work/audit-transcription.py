#!/usr/bin/env python3
"""Inventory check of manual tokens, not automatic image recognition."""
from pathlib import Path
from collections import Counter
import json, hashlib
p=Path(__file__).resolve().parents[1]
for name,digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest()==digest
key=json.loads((p/'work/key.json').read_text())
tokens=(p/'work/transcription.txt').read_text().replace('/',' ').split()
counts=Counter(tokens)
unknown={k:{'count':counts[k],'positions_1_based':[i for i,t in enumerate(tokens,1) if t==k]} for k in counts if key[k] is None}
result={'manual_positions':len(tokens),'distinct_shapes':len(counts),'unresolved_positions':sum(counts[k] for k in unknown),'unknown_shapes':unknown,'source_hashes':'passed','scope':'manual transcript inventory only; image glyph segmentation is not automatic'}
print(json.dumps(result,indent=2))
