"""hcp-1132: decode the Morse transcription and check the source hashes.
Run from the repo root:  python3 -I ciphers/hcp-1132/work/decode.py
"""
import hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.dirname(HERE)
HASHES = {
    'source/address-large.jpg': '2c8e2d3b265bcc8476306c034bd94ee156f48733bc495472693d141ea990b28d',
    'source/picture-large.jpg': '16a0090e66f1261aaff7bc394b1a5432c96a44df2843fb3c0e7cddfa1cd09c9a',
    'work/hires/cpc_--_HU_Debrecen_HU___adr.jpg': 'f08cbfaf39c0ac5f19172d65b94ec2f0af2a295723aae3c7c923ad7ebf23ed92',
    'work/hires/cpc_--_HU_Debrecen_HU___pic.jpg': '7f36f53f0377343352bb2d8c94673204940ac35f0af3ad10ada4b8123b5b60a0',
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + p)
    ok &= got == h
if not ok:
    sys.exit('source hash mismatch')

# International Morse with the Hungarian accented letters used on the card.
MORSE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
         '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
         '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
         '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
         '..-..': 'É', '.--.-': 'Á', '---.': 'Ö'}
SPECIAL = {'/': ' ', ',': ',', '!': '!', '!!': '!!', '[X]': '[struck out]'}

lines = []
for raw in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8'):
    if not raw.strip() or raw.startswith('#'):
        continue
    label, code = raw.split(':', 1)
    out = ''
    for tok in code.split():
        if tok in SPECIAL:
            s = SPECIAL[tok]
            out = out.rstrip() + s if s in (',', '!', '!!') else out + (s if s == ' ' else ' ' + s + ' ')
        elif tok in MORSE:
            out += MORSE[tok]
        else:
            sys.exit(f'unknown Morse group {tok!r} in {label.split()[0]}')
    lines.append((label.split()[0], ' '.join(out.split())))

for lab, txt in lines:
    print(f'{lab:4s} {txt}')
# Columns run on into each other; '|' marks a column end (words may continue across it).
print('\nRUN-ON:', '|'.join(t for _, t in lines))
