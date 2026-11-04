"""hcp-1045: number substitution (Lehmann/Susi table as on hcp-1113, 1134): A=2 ... I=10, J omitted, K=11 ... Z=26.
'"' = umlaut, '^' = umlaut not marked on the card (word sense), '=' = doubled letter, 'x' = capital marker, '|' = omitted separator.
Run from repo root: python3 -I ciphers/hcp-1045/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {'source/address-large.jpg': 'de9f5314b08fd407a4a3f570f8fb52de2f3997bb70e000eb68ea168b934b3a5d',
     'source/picture-large.jpg': '64ee863922f8dfb2208dc02453ecc6cd6499e53225025136e0d50fc861752546',
     'work/hires/cpc_1909-10-12_DE_-(Schlesien)_DE_Hier_fritzlehmann-09_adr.jpg': 'ae22ba638bfdda9af18667e1e54a8401aadb865cd3c5cb6b2631b0be03e8a1a3'}
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
    for tok in line.replace('-', ' ').split():
        if tok in '!?': words[-1] += tok; continue
        w = ''
        for n in tok.strip('.').replace('|', '.').split('.'):
            u = '"' in n or '^' in n; dbl = '=' in n
            ch = KEY[int(n.strip('"=x^'))]
            ch = UML[ch] if u else ch
            w += ch * 2 if dbl else ch
        words.append(w)
    out.append(' '.join(words))
print('\n'.join(out))
