"""hcp-1180: decode the 'algebra' vowel cipher.  Run from repo root:
   python3 -I ciphers/hcp-1180/work/decode.py
Key: 1=a 2=e 3=i 4=o 5=u, 1/1=ä 5/5=ü; letters stand for themselves;
+ - = ( ) . V are decoration (nulls). '#..' keeps a literal number (the date)."""
import hashlib, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
 'source/picture-large.jpg': 'b8edf03ec8aec06eb0f7ed541183f1be11c14604aa68cda1387c02d95883edd1',
 'source/address-large.jpg': '8cbecdb66c4f1e53f283fa9fa6a4076aa2e19e9595a907d1a0b8b28d69812958',
 'work/hires/cpc_--___CH_Neuchatel__pic.jpg': 'fd38fde105815d1219d448e190785c27f090bfe2303017091b47ef7c04d1fbcb',
 'work/hires/cpc_--___CH_Neuchatel__adr.jpg': '516cc836f53ff7940c042163ae066e0f20e4dabe53a4389a59cf84cda5c9a7f9',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p, file=sys.stderr)
    if got != h: sys.exit(1)
KEY = {'1/1': 'ä', '5/5': 'ü', '1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
def dec(seg):
    seg = re.sub(r'\[struck:[^\]]*\]', '', seg)
    out, i = '', 0
    while i < len(seg):
        if seg[i] == '#':
            m = re.match(r'#(\d+)', seg[i:]); out += m.group(1); i += len(m.group(0)); continue
        if seg[i:i+3] in KEY: out += KEY[seg[i:i+3]]; i += 3; continue
        c = seg[i]
        if c in KEY: out += KEY[c]
        elif c.isalpha() and c != 'V': out += c
        elif c == '!': out += '!'
        i += 1
    return out
buf = ''
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    line = line.rstrip('\n')
    if line.startswith('#'):
        if 'Left margin' in line:
            print(' '.join(buf.split())); buf = ''; print('-- left margin --')
        continue
    join = line.endswith('~')
    words = [dec(s) for s in line.rstrip('~').split('|')]
    buf += ' '.join(w for w in words if w) + ('' if join else ' ')
print(' '.join(buf.split()))
