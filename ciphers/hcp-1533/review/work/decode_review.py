"""Reviewer's independent decoder (does not import solver code).
usage: python3 -I decode_review.py KEY.json READING.txt
KEY maps shape label -> plaintext; READING has one cipher row per line.
Characters not in the key must be punctuation/space, else reported."""
import json, sys
key = json.load(open(sys.argv[1], encoding='utf-8'))
units = 0; unknown = []
for ln, line in enumerate(open(sys.argv[2], encoding='utf-8'), 1):
    line = line.rstrip('\n')
    if not line or line.startswith('#'):
        continue
    out = []
    for ch in line:
        if ch in key:
            out.append(key[ch]); units += 1
        elif ch in ' .,-?;:!"()':
            out.append(ch)
        else:
            out.append('[' + ch + ']'); unknown.append((ln, ch))
    print(''.join(out))
print(f'\n# units={units} unknown={unknown}', file=sys.stderr)
