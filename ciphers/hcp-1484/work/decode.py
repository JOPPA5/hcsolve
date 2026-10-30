"""HCP 1484: decode work/transcription.txt with work/key.json; verify source hashes.
Run from the repo root:  python3 -I ciphers/hcp-1484/work/decode.py"""
import hashlib, json, os, sys
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
    'source/address-large.jpg': '992ffe23444123a871a16a2f8a374d416a3cd169f309e0b06ba558cffba66d24',
    'source/picture-large.jpg': '72d92929ed7571879aaf4e656ad3c3c290a9603b4e8354e8fec19955c3273e95',
    'source/metadata.md': '0032cde1e0019f0dbc416a5b5bdff36733d50ed6e89d1e5b1d62a7ba14637cbf',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(BASE, p), 'rb').read()).hexdigest()
    if got != h:
        sys.exit('hash mismatch: ' + p)
print('source hashes OK')
key = json.load(open(os.path.join(BASE, 'work/key.json')))
n = 0
out = []
for line in open(os.path.join(BASE, 'work/transcription.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    words = []
    for tok in line.split():
        if tok == '/':
            words.append(' ')
            continue
        if tok in {',', '.', '?', '"', '-'}:
            words.append(tok + (' ' if tok in ',.?' else ''))
            continue
        faint = tok.startswith('[faint]')
        t = tok.replace('[faint]', '')
        dbl = t.endswith('^2')
        t = t[:-2] if dbl else t
        if t not in key:
            sys.exit('unmapped sign: ' + tok)
        n += 1
        letter = key[t]
        words.append(('[' + letter.lower() + ']') if faint else (letter * 2 if dbl else letter))
    s = ''.join(words).replace('  ', ' ').strip()
    out.append(s[:-3] + ',"' if s.endswith(', "') else s)
print('\n'.join(out))
print('%d signs, all mapped' % n)
