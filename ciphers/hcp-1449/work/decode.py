"""Decode hcp-1449. Run from repo root:
python3 -I ciphers/hcp-1449/work/decode.py
Checks source hashes, then transliterates work/transcription.txt with work/key.json."""
import hashlib, json, sys, pathlib
d = pathlib.Path(__file__).resolve().parent.parent
ref = json.loads((d/'work/source-sha256.json').read_text())
for name, h in ref.items():
    got = hashlib.sha256((d/'source'/name).read_bytes()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + 'source/' + name)
    if got != h: sys.exit(1)
key = json.loads((d/'work/key.json').read_text()); key.pop('_comment')
lines = [l for l in (d/'work/transcription.txt').read_text(encoding='utf-8').splitlines() if l and not l.startswith('#')]
print()
for l in lines:
    out = ''.join(key.get(c, c) if c != ' ' else ' ' for c in l)
    unk = [c for c in l if c != ' ' and c not in key]
    if unk: sys.exit('unmapped glyphs: %r' % unk)
    print(l, ' -> ', out)
