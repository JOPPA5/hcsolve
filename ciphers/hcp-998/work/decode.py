"""Decode hcp-998: python3 -I ciphers/hcp-998/work/decode.py (run from repo root)."""
import hashlib, json, os, sys
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {'source/picture-large.jpg': '015a1a5571fe16fb659680e52d48b432caf0dc6c1d5d5774c520f6575a079fc3',
          'source/address-large.jpg': 'c6fbbf0783a575fe0d5b09518dcfed8ea32ab90b340b70fc1185ab8ac4e1bffa'}
for f, h in HASHES.items():
    d = hashlib.sha256(open(os.path.join(base, f), 'rb').read()).hexdigest()
    print(('OK  ' if d == h else 'BAD ') + f); assert d == h
key = json.load(open(os.path.join(base, 'work/key.json'), encoding='utf-8'))
out = []
for line in open(os.path.join(base, 'work/transcription.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    toks = line.split()
    s = ''.join(key[t] for t in toks)
    out.append(s if toks[-1] == '=' else s + ' ')
text = 'Am 25.11.01. (plain) ' + ''.join(out)
print(' '.join(text.split()))
