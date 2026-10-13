#!/usr/bin/env python3
"""Reproduce a source-hash-bound MANUAL edition. No automatic image recognition."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parents[3]
n=int(sys.argv[1]); w=root/f'ciphers/hcp-{n}/work'
e=json.loads((w/'manual-edition.json').read_text()); key=json.loads((w/'graphic-key.json').read_text())
source=(w/e['source']).resolve()
assert hashlib.sha256(source.read_bytes()).hexdigest()==e['sha256'],'Source differs from manually inspected scan'
for row in e['rows']:
 text=''.join(t[8:] if t.startswith('literal:') else key[t] for t in row['graphic_tokens'])
 print(f"{row['row']:02}: {text}")
