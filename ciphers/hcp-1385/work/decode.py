#!/usr/bin/env python3
# Run from the repo root: python3 -I ciphers/hcp-1385/work/decode.py
import hashlib, json, re, datetime, pathlib
D = pathlib.Path('ciphers/hcp-1385')
H = {'source/picture-large.jpg':'7c67cc9c308a54e88fcfdf564cf88cd51e72a3d8241c97908dbed1bf16dde7dd',
     'source/address-large.jpg':'75495786e2c3a7e106cdc9d022853166411377df3707cf70c8b237f2f45c4484',
     'work/hires/pc_hcp_66_pic.JPG':'eeedfb279cfbfaea3d48b47a609eb12ffbec7e48fa66a809532c59320d0bdf20',
     'work/hires/pc_hcp_66_adr.JPG':'4a77ebc3880d15f1b337ef917947d6aac39276290c1457e92fb2de48e844cdd3'}
for f, h in H.items():
    assert hashlib.sha256((D/f).read_bytes()).hexdigest() == h, f
def sh(s, k):
    return ''.join(chr((ord(c.upper())-65+k) % 26 + 65) if c.isalpha() else c for c in s)
T = json.loads((D/'work/transcription.json').read_text())
print(T['plain_heading'], '(clear)')
known = opaque = kept = 0
for r in T['rows']:
    out = []
    for tok in re.findall(r'\[[^\]]*\]|\{[^}]*\}|[^\s\[\{]+', r['cipher']):
        if tok[0] == '[':
            out.append(tok); kept += sum(c.isalpha() for c in tok)
        elif tok[0] == '{':
            out.append('{literal ' + sh(tok[1:-1], -1) + ' — unresolved}'); opaque += sum(c.isalpha() for c in tok)
        else:
            d = sh(tok, -1); out.append(d); known += sum(c.isalpha() for c in tok)
            assert sh(d, 1).lower() == tok.lower()
    print(' '.join(out))
print(T['plain_date'], '(clear)')
assert datetime.date(1907, 11, 21).strftime('%A') == 'Thursday'
print(f'-- hashes OK; {known} letters decoded to words, {opaque} unresolved, {kept} abbreviation letters kept literal; PARTIAL')
