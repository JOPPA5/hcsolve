#!/usr/bin/env python3
"""HCP1554 (pc_hcp_235) - current decoder after review round 1.

Standard library only; writes nothing unless --write-literal is given.
Reads work/transcription-v2.tsv (manual transcription, row id TAB cipher text)
and work/key-v2.json (Anna Ticha family key + v->F + k-shaped G).

Notation in the transcription (and kept in the output):
  {x}      a sign whose class is uncertain; output {letter}
  <...>    written as U+27E8/U+27E9: signs read but presumed abandoned/inked over
           by the writer; output kept inside the same brackets
  [9:40]   ordinary numerals, not cipher
  space . , ! ? -  separators
Supersedes work/decode.py (round-1 audit of the older transcription).
"""
from pathlib import Path
import hashlib, json, re, sys

W = Path(__file__).resolve().parent
C = W.parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    for name, h in json.loads((W / 'source-sha256.json').read_text()).items():
        assert sha(C / 'source' / name) == h, f'source changed: {name}'
    key1 = json.loads((W / 'key.json').read_text())
    key = json.loads((W / 'key-v2.json').read_text())
    assert key == dict(key1, G='g'), 'key-v2 must be key.json plus G'
    assert len(key) == len(set(key.values())) == 24
    rows = [l.split('\t', 1) for l in (W / 'transcription-v2.tsv').read_text().splitlines()]
    tok = re.compile(r'\{.\}|⟨[^⟩]*⟩|\[9:40\]|.')
    units = struck = uncertain = letters = 0
    used = {}
    out = []
    for rid, text in rows:
        plain = []
        for m in tok.finditer(text):
            t = m.group()
            if t.startswith('{'):
                s = t[1]
                assert s in key, (rid, t)
                plain.append('{' + key[s] + '}')
                units += 1; uncertain += 1; letters += len(key[s]); used[s] = used.get(s, 0) + 1
            elif t.startswith('⟨'):
                inner = t[1:-1]
                assert all(s in key for s in inner), (rid, t)
                plain.append('⟨' + ''.join(key[s] for s in inner) + '⟩')
                struck += len(inner)
            elif t == '[9:40]':
                plain.append(t)
            elif t in key:
                plain.append(key[t]); units += 1; letters += len(key[t]); used[t] = used.get(t, 0) + 1
            else:
                assert t in ' .,!?-', (rid, t)
                plain.append(t)
        out.append(f'{rid}: ' + ''.join(plain))
    literal = '\n'.join(out) + '\n'
    lit = W / 'literal-v2.txt'
    if '--write-literal' in sys.argv:
        lit.write_text(literal)
    assert lit.read_text() == literal, 'saved literal-v2.txt differs'
    print(literal, end='')
    print(f'\nRows: {len(rows)} (16 main + 2 insertions + 3 marginal)')
    print(f'Read cipher units: {units} (of which {uncertain} marked uncertain {{}}), '
          f'plaintext letters: {letters}, CH units: {used.get("H", 0)}, G units: {used.get("G", 0)}')
    print(f'Signs presumed abandoned by the writer (⟨⟩, not counted above): {struck}')
    print(f'Key classes used: {len(used)}/{len(key)}; unused: {sorted(set(key) - set(used))}')
    print('Saved literal-v2.txt: OK')


if __name__ == '__main__':
    main()
