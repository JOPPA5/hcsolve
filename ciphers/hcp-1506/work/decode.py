#!/usr/bin/env python3
"""Decode manually transcribed tokens; never normalize an unmapped number."""
from pathlib import Path
import hashlib
import json

p = Path(__file__).resolve().parents[1]
key = {1: 'M', 3: 'E', 4: 'R', 5: 'V', 6: 'L', 7: 'O', 8: 'T',
       9: 'P', 10: 'S', 11: 'F', 12: 'A', 13: 'G', 14: 'K', 15: 'B',
       16: 'U', 17: 'I', 18: 'D', 20: 'C', 21: 'W', 22: 'H',
       24: 'X', 25: 'N', 26: 'Y'}
assert len(key) == len(set(key.values()))
inv = {v: k for k, v in key.items()}
for f, expected in json.loads((p / 'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p / 'source' / f).read_bytes()).hexdigest() == expected, f

trace = ['section\tline\tword\tposition\traw\tdecoded']
total = mapped = 0
for section, filename in [('MAIN', 'transcription.txt'),
                          ('PERIPHERAL', 'peripheral-transcription.txt')]:
    print(section)
    count = 0
    for lineno, line in enumerate((p / 'work' / filename).read_text().splitlines(), 1):
        if not line or line.startswith('#'):
            continue
        result = []
        for wordno, token in enumerate(line.split(' / '), 1):
            if token.startswith('{'):
                assert token.endswith('}')
                result.append(token[1:-1])
                continue
            nums = list(map(int, token.split('.')))
            letters = []
            for pos, n in enumerate(nums, 1):
                c = key.get(n, f'[{n}]')
                letters.append(c)
                if n in key:
                    assert inv[c] == n
                    mapped += 1
                trace.append(f'{section}\t{lineno}\t{wordno}\t{pos}\t{n}\t{c}')
            result.append(''.join(letters))
            count += len(nums)
        print(' '.join(result))
    total += count
    print(f'{section} numeric positions: {count}')
print(f'Total numeric positions: {total}; mapped: {mapped}; unmapped: {total - mapped}')
print('Source hashes and inverse-key checks passed for mapped tokens.')
(p / 'work/token-trace.tsv').write_text('\n'.join(trace) + '\n')
