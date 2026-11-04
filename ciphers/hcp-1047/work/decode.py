"""hcp-1047: number substitution, A=2 ... I=10, J omitted, K=11 ... Z=26 (same table as hcp-1113/1134/1060);
'"' = umlaut, '=' = doubling bar, '+' = clause separator.
Run from repo root: python3 -I ciphers/hcp-1047/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {'source/address-large.jpg': '9ca88adb9407444c83c35fddbc67b512c294a77cb1f6d028fc899894c487be77',
     'source/picture-large.jpg': '623d56deb6e877e7ff2b3e7fa352932b6a391e0721bcd1ed0672a307677b79a7',
     'work/hires/cpc_1909-07-24_DE_Freiburg-(Schlesien)_DE_Hier_fritzlehmann-05_adr.jpg':
         'f725eefc8b6a02ae5acad91daf3fa7878b426e8b60e9d03bf52e7829fbce6ae6'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
KEY = {i + 2: ch for i, ch in enumerate(ALPHA)}
UML = {'A': 'Ä', 'O': 'Ö', 'U': 'Ü'}
out = []
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    words = []
    for tok in line.replace(' - ', ' ').replace('+', ' , ').split():
        if tok in (',', '-'):
            if tok == ',': words.append(',')
            continue
        w = ''
        for n in tok.strip('.').split('.'):
            u = '"' in n; dbl = '=' in n
            ch = KEY[int(n.replace('"', '').replace('=', ''))]
            ch = UML[ch] if u else ch
            w += ch * (2 if dbl else 1)
        words.append(w)
    out.append(' '.join(words).replace(' ,', ','))
print('\n'.join(out))
