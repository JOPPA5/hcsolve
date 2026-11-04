"""hcp-1050: number substitution, A=2 ... I=10, J omitted, K=11 ... Z=26 (same table as Lehmann cards hcp-1113, 1134, 1060).
'"' = umlaut, '_' = bar (doubled letter), '?' kept, line-final '=' joins the word with the next line.
Run from repo root: python3 -I ciphers/hcp-1050/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {'source/address-large.jpg': '705d0bf29587b71a44f01e9833cc8e032d341744c04df67e32e4592dabddf1a1',
     'source/picture-large.jpg': 'b4cd4bdf1caea485160876e7505b4be5ffd6b4de257e3b2f29e630fff8614c22',
     'work/hires/cpc_1910-03-17_DE_Schweidnitz_DE_Konigszelt_fritzlehmann-11_adr.jpg': '5ed75af91938365ad955b46b60ee587aac75945029476a23dd5bc22d97a5704a',
     'work/hires/cpc_1910-03-17_DE_Schweidnitz_DE_Konigszelt_fritzlehmann-11_pic.jpg': 'f3623483657ce21379273e7d3c6fc039767679f7f4069fc3f1d646a0763f0883'}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
ALPHA = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'          # 25 letters, no J
KEY = {i + 2: ch for i, ch in enumerate(ALPHA)}
UML = {'A': 'Ä', 'O': 'Ö', 'U': 'Ü'}
def word(tok):
    tail = '?' if tok.endswith('?') else ''
    w = ''
    for n in tok.rstrip('?').strip('.').split('.'):
        dbl, uml = '_' in n, '"' in n
        ch = KEY[int(n.replace('_', '').replace('"', ''))]
        if uml: ch = UML[ch]
        w += ch * (2 if dbl else 1)
    return w + tail
lines, carry = [], ''
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    join = line.endswith('=')
    toks = [word(t) for t in line.rstrip('=').split(' - ')]
    toks[0] = carry + toks[0]; carry = ''
    if join: carry = toks.pop()
    lines.append(' '.join(toks))
print('\n'.join(lines))
print('\nRUN-ON:', ' '.join(lines))
