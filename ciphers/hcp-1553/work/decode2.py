#!/usr/bin/env python3
"""HCP1553 (pc_hcp_234) - current decoder after review round 1.

Standard library only; writes nothing unless --write-literal is given.
Reads work/transcription-v2.tsv (manual transcription: row id TAB cipher text)
and work/key-v2.json (Anna Ticha family key + shallow-v F + k-shaped G).

Notation (kept in the output):
  {x}   sign read as class x but visually anomalous; output {letter}
  [x]   sign restored from context (overinked); output [letter]
  ~     short non-letter stroke (dash); output as '-'
  space . , ? -  separators
Supersedes work/decode.py (audit of the pre-review partial transcription).
"""
from pathlib import Path
import hashlib, json, re, sys

W = Path(__file__).resolve().parent
C = W.parent


def main():
    for name, h in json.loads((W / 'source-sha256.json').read_text()).items():
        assert hashlib.sha256((C / 'source' / name).read_bytes()).hexdigest() == h, f'source changed: {name}'
    key1 = json.loads((W / 'key.json').read_text())
    key = json.loads((W / 'key-v2.json').read_text())
    assert key == dict(key1, G='g'), 'key-v2 must be key.json plus G'
    assert len(key) == len(set(key.values())) == 24
    rows = [l.split('\t', 1) for l in (W / 'transcription-v2.tsv').read_text().splitlines()]
    tok = re.compile(r'\{.\}|\[.\]|.')
    units = letters = anomalous = restored = 0
    used = {}
    out = []
    for rid, text in rows:
        plain = []
        for m in tok.finditer(text):
            t = m.group()
            if len(t) == 3:
                s = t[1]
                assert s in key, (rid, t)
                plain.append(t[0] + key[s] + t[2])
                anomalous += t[0] == '{'; restored += t[0] == '['
            elif t in key:
                s = t; plain.append(key[s])
            elif t == '~':
                plain.append('-'); continue
            else:
                assert t in ' .,?-', (rid, t)
                plain.append(t); continue
            units += 1; letters += len(key[s]); used[s] = used.get(s, 0) + 1
        out.append(f'{rid}: ' + ''.join(plain))
    literal = '\n'.join(out) + '\n'
    lit = W / 'literal-v2.txt'
    if '--write-literal' in sys.argv:
        lit.write_text(literal)
    assert lit.read_text() == literal, 'saved literal-v2.txt differs'
    print(literal, end='')
    print(f'\nRows: {len(rows)}; cipher units: {units} ({anomalous} anomalous {{}}, {restored} restored []); '
          f'plaintext letters: {letters}; CH units: {used.get("H", 0)}; G units: {used.get("G", 0)}')
    print(f'Key classes used: {len(used)}/{len(key)}; unused: {sorted(set(key) - set(used))}')
    print('Saved literal-v2.txt: OK')


if __name__ == '__main__':
    main()
