"""hcp-927: check source hashes, decode work/transcription.txt (hand-written International/German Morse).
Run from the repo root:  python3 -I ciphers/hcp-927/work/decode.py
"""
import hashlib, os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
    'source/address-large.jpg': 'aa6dee6ff6f1ee4ebaa0f2894cd673706f1e8d51c5db4462303188ecd2039e01',
    'source/picture-large.jpg': '9f8da7fa494d5fd4527faa3aaccdc4004f7375973a929b31c7c72a6343366c87',
    'work/hires/cpc_1910-06-19_DE_Graudenz-(Grudziadz)_DE_Rendsburg__adr.jpg': '343d6504e3ed07662aa2bc78d0fd26fb1b37d26b6aa913b322f436f2048866c3',
    'work/hires/cpc_1910-06-19_DE_Graudenz-(Grudziadz)_DE_Rendsburg__pic.jpg': 'c469e2bc646cc78b4d6c93903334f742aeccdb65d7ad95e3c2a9242d857a64df',
}
ok = True
for rel, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, rel), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + rel)
    ok &= got == h
if not ok:
    sys.exit('hash mismatch')

M = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
     '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
     '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
     '-.--': 'Y', '--..': 'Z', '----': 'CH', '..--': 'Ü', '---.': 'Ö', '.-.-': 'Ä',
     '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
     '---..': '8', '----.': '9', '-----': '0'}

def dec(tok):
    if tok == '/': return ' '
    if tok == ',': return ','
    if tok == '//': return '='
    if tok.startswith('{'): return tok[1:-1]
    if tok.startswith('[?'): return '[?' + tok[2:-1] + ']'
    if tok not in M: sys.exit('unknown sign ' + tok)
    return M[tok]

lines = {}
for raw in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    m = re.match(r'^([CR]\d+):\s*(.*)$', raw.rstrip('\n'))
    if m:
        lines[m.group(1)] = m.group(2).split()

def run(keys):
    out = ''
    for k in keys:
        txt = ''.join(dec(t) for t in lines[k])
        print('  %-4s %s' % (k, txt))
        out += txt
    return re.sub(' +', ' ', out.replace('=', '')).strip()

print('\nPart A - main message (vertical lines, right to left):')
a = run(sorted(k for k in lines if k[0] == 'C'))
print('\nPart B - upside-down rows at the top edge (row 4 first):')
b = run(['R4', 'R3', 'R2', 'R1'])
print('\nRunning text A: ' + a)
print('Running text B: ' + b)
