#!/usr/bin/env python3
"""Reproduce conditional terminal mapping and manually measured gap evidence."""
import hashlib
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1]
for filename, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/filename).read_bytes()).hexdigest() == digest
data = json.loads((p/'work/terminal-scope.json').read_text())
key = {'. ..': 'R', '...': 'S'}
for name in ('terminal_top_row', 'terminal_bottom_row'):
    row = data[name]
    xs = [point[0] for point in row['approximate_centres']]
    gaps = [b-a for a,b in zip(xs, xs[1:])]
    assert key[row['manual_pattern']] == row['American_Morse_conditional_letter']
    print(name, row['manual_pattern'], '=>', key[row['manual_pattern']],
          'approximate x-centre gaps:', gaps)
print(data['scope_limit'])
print('Cancelled box remains untranscribed. Hash and mapping checks passed; not OCR.')
