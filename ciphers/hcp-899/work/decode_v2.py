#!/usr/bin/env python3
"""HCP 899: decode the full manual shape transcription (work/transcript_v2.json)
with the three-state Pigpen key. Checks SHA-256 of the source files first.
Run from the repo root:  python3 ciphers/hcp-899/work/decode_v2.py"""
from pathlib import Path
import hashlib, json
root = Path(__file__).resolve().parents[1]
d = json.loads((root/'work/transcript_v2.json').read_text())
for name, want in d['source_sha256'].items():
    got = hashlib.sha256((root/name).read_bytes()).hexdigest()
    assert got == want, f'source changed: {name}'
key = d['key']
assert len(set(key.values())) == len(key)
dec = lambda toks: ''.join(key[t] for t in toks.split())
n_up = n_lo = n_obs = 0
print('== Upper personal message ==')
for r in d['upper']:
    words = [w for w in r['tokens'].split('/')]
    n_up += sum(len(w.split()) for w in words)
    print(r['label'], ' '.join(dec(w) for w in words))
print('== Lower poem ==')
for r in d['lower']:
    out = []
    for w in r['words']:
        n = len(w['tokens'].split()); n_lo += n; n_obs += len(w['obscured'])
        assert all(1 <= i <= n for i in w['obscured'])
        txt = dec(w['tokens'])
        out.append(''.join(c.lower() if i+1 in w['obscured'] else c for i, c in enumerate(txt)))
    print(r['label'], ' '.join(out))
print(f'glyphs: upper {n_up}, lower {n_lo}, total {n_up+n_lo}; '
      f'lower glyphs partly obscured by watermark (shown lower-case): {n_obs}')
print('Source hashes OK. Manual transcription; the script does not read pixels.')
