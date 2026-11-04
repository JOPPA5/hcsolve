"""hcp-913: number substitution, A=2 ... I=10, J omitted, K=11 ... Z=26 (Lehmann-family key).
Run from repo root: python3 -I ciphers/hcp-913/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {'source/address-large.jpg': '09f4f6f48da0b7b1522216c327620a61b65cbda70d66c4a2f4fbbd364da0abbc',
     'source/picture-large.jpg': '66e3a9f53480d17720d002811ba1699acbf9e684c5c0805ab7329e862a2c4b34',
     'work/hires/cpc_-03-26_DE_Reichen-(Schlesien)_DE_Schneidwitz_fritzlehmann-18_adr.jpg': 'c40737a375d8415235c3f76077ed7857153bc250ddc7114e7cec6c275a4a4860',
     'work/hires/cpc_-03-26_DE_Reichen-(Schlesien)_DE_Schneidwitz_fritzlehmann-18_pic.jpg': 'b3f88103101973a985dce03df8ba56a5c6b817353f1fd1ba029a26b7cc33ca02'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
KEY = {i + 2: ch for i, ch in enumerate(ALPHA)}
UML = {'A': 'Ä', 'O': 'Ö', 'U': 'Ü'}
out, used = [], set()
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    words = []
    for tok in line.replace('-', ' ').replace('+', ' ! ').split():
        if tok == '!': words.append('!'); continue
        w = ''
        for n in tok.strip('.').split('.'):
            u = n.endswith('"'); v = int(n.rstrip('"')); used.add(v); ch = KEY[v]
            w += (UML.get(ch, ch + '"') if u else ch)
        words.append(w)
    out.append(' '.join(words))
print('\n'.join(out))
print('numbers used:', sorted(used))
