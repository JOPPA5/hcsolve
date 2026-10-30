"""HCP 1483: verify source hashes, decode work/transcription.txt with work/key.json.
Run from the repo root:  python3 -I ciphers/hcp-1483/work/decode.py"""
import hashlib, json, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {'source/address-large.jpg':'9aea5446304f7425c0fc663661263d5836a09436dc604f707f0c06e629009982',
     'source/metadata.md':'51970f6a20227bccc7487e29d2c807f64ce0fa02c92a319c39dc4e6ee54a8b07',
     'source/picture-large.jpg':'0bfa0277f55a118988b6561bf42ffbfdf4e4eb0e88374a44c91ff350e5cbad1e'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    if got != h: sys.exit(f'HASH MISMATCH {p}')
key = json.load(open(os.path.join(D, 'key.json'))); key.pop('_doc')
n = 0
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    line = line.rstrip('\n')
    if not line or line.startswith('#'): continue
    lab, body = line.split(':', 1)
    out, prev = [], ''
    i, toks = 0, []
    # split, keeping <...> groups intact
    s = body.strip()
    while s:
        if s.startswith('<'):
            j = s.index('>'); toks.append(s[:j+1]); s = s[j+1:].strip()
        else:
            t, _, s = s.partition(' '); toks.append(t); s = s.strip()
    for t in toks:
        if t.startswith('<'): out.append(t[1:-1] + ' '); continue
        if t == '/': out.append(' '); continue
        if t == 'x2': out.append(prev); n += 1; continue
        if t.startswith('ins:'): prev = key[t[4:]]; out.append('^' + prev); n += 1; continue
        if t in key: prev = key[t]; out.append(prev); n += 1; continue
        if t in list(',.!?"'): out.append(t); continue
        sys.exit(f'unknown token {t!r} in {lab}')
    print(f'{lab:4} ' + ''.join(out).replace('  ', ' ').strip())
print(f'-- source hashes OK; {n} enciphered letters decoded, all signs mapped')
