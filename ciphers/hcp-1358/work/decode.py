#!/usr/bin/env python3
"""hcp-1358: check sources, decode the manual transcription by Caesar -1."""
from pathlib import Path
import hashlib, json, string
ROOT = Path(__file__).resolve().parents[1]
HASH = {
 'source/picture-large.jpg': '17ffb2361dcaec6600df7469b0d8ef13e0ced6243d2b21f657d3333c271fadc3',
 'source/address-large.jpg': 'f3ec7a3cbfba2a00b96f0271823e346511cb58fecdc1695fc57964fc89be9b92',
 'work/hires/pc_hcp_39_pic.JPG': '894ca22c686237219ebfc5221cdcfb7e5520be61ba950e049b85757f8f4cf7b4',
 'work/hires/pc_hcp_39_adr.JPG': '9f85e7e6e1dbfe81010e55d5d5dd32689a2b90fa8e0590e0fa1f5ea544381255',
}
for name, want in HASH.items():
    if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != want:
        raise SystemExit('Hash mismatch: ' + name)
U, L = string.ascii_uppercase, string.ascii_lowercase
dec = str.maketrans(U + L, U[-1] + U[:-1] + L[-1] + L[:-1])
enc = str.maketrans(U[-1] + U[:-1] + L[-1] + L[:-1], U + L)
data = json.loads((ROOT / 'work/transcription.json').read_text())
n = 0
for row in data['rows']:
    plain = row.translate(dec)
    assert plain.translate(enc) == row
    n += sum(c.isalpha() for c in row)
    print(f'{row:26} {plain.upper()}')
print()
text = ' '.join(data['rows']).translate(dec).upper().replace('.', '')
for s in data['slips']:
    print(f"Writer's slip: {s['word']} sign {s['sign']} reads {s['read']}, expected {s['expected']}: {s['literal']} as written, {s['intended']} intended.")
    text = text.replace(s['literal'], s['intended'])
print('Intended text:', text)
print('Plain, not enciphered:', data['plain_not_enciphered'])
print(f'{n} enciphered letters. Source hashes and round trip verified.')
