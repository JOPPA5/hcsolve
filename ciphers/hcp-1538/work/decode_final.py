#!/usr/bin/env python3
"""Final decoder (round 2): applies work/key.json to work/transcript-final.txt.
Every glyph must be in the key; read, partly-visible and restored signs are counted separately.
Output: literal plaintext per row; restorations stay in [brackets], partly visible in (parens).
Checks the source scans are unchanged and that work/decoded-final.txt equals the output."""
import hashlib, json, sys
from pathlib import Path
W = Path(__file__).resolve().parent; C = W.parent
HASH = {'source/picture.jpg': 'e888e16106a10cb0c8900783cdd85650e69695a4b6e4ff6df292df84ed607564',
        'source/address.jpg': 'e70cff172a5725995dc769e241b2e161d9672655487b36d11c76080d52d7c714'}
key = json.loads((W/'key.json').read_text())
for rel, want in HASH.items():
    if hashlib.sha256((C/rel).read_bytes()).hexdigest() != want: sys.exit(f'HASH FAILURE: {rel}')
read = restored = partial = 0; out = []
for raw in (W/'transcript-final.txt').read_text().splitlines():
    if not raw.strip() or raw.startswith('#'): continue
    rid, text = raw.split(' ', 1)
    text = text.replace(' || ', ' ').replace('||', '')
    res = []; mode = None
    for ch in text:
        if ch in '[(':
            mode = ch; res.append(ch); continue
        if ch in '])':
            mode = None; res.append(ch); continue
        if ch in key:
            res.append(key[ch])
            if mode == '[': restored += 1
            elif mode == '(': partial += 1
            else: read += 1
        elif ch.isalnum():
            sys.exit(f'UNMAPPED glyph {ch!r} in {rid}')
        else:
            res.append(ch)
    out.append(f'{rid} ' + ''.join(res))
head = (f'COMPLETE literal reading: {read} signs read, {partial} partly visible, {restored} restored; '
        f'{read+partial+restored} cipher signs total; no unmapped glyphs.')
text = head + '\n' + '\n'.join(out) + '\n'
saved = W/'decoded-final.txt'
if '--write' in sys.argv: saved.write_text(text)
elif saved.exists() and saved.read_text() != text: sys.exit('decoded-final.txt differs from current decoding')
print(text, end='')
