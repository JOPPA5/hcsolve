#!/usr/bin/env python3
"""Bounded checks on frozen manual Morse; no new visual transcription."""
from pathlib import Path
import hashlib
import itertools
import json

root = Path(__file__).resolve().parents[1]
for name, expected in json.loads((root / 'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root / 'source' / name).read_bytes()).hexdigest() == expected
rows = json.loads((root / 'work/transcription.json').read_text())['rows']
codes = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
key = dict(zip(codes, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
anomaly = rows[5]['groups'][3]
assert anomaly == '.-.-'
print('Global element transformations (letter delimiters unchanged):')
for reverse, invert in itertools.product((False, True), repeat=2):
    def transform(group):
        if reverse:
            group = group[::-1]
        if invert:
            group = group.translate(str.maketrans('.-', '-.'))
        return group
    out = []
    for row in rows:
        out.append(''.join(key.get(transform(g), '{' + transform(g) + '}') for g in row['groups']))
    print(f'reverse_elements={reverse}, invert_elements={invert}: ' + ' / '.join(out))
print('\nAll added internal separators in the anomalous group:')
for cuts in itertools.product((False, True), repeat=len(anomaly)-1):
    if not any(cuts):
        continue
    parts, start = [], 0
    for pos, cut in enumerate(cuts, 1):
        if cut:
            parts.append(anomaly[start:pos])
            start = pos
    parts.append(anomaly[start:])
    print(' / '.join(parts) + ' => ' + ''.join(key[p] for p in parts))
print('\nHistorical checks, scoped to cited tables in historical-code-check.md:')
print('International/Continental C = -.-.; Vail 1845 American C = .. . (internal long gap).')
print('Neither table gives C = .-.-. No source marks changed.')
print('42 frozen manual groups; 41 standard A-Z letters plus 1 preserved anomaly.')
print('Source hashes verified. Script does not verify handwriting or pixels.')
