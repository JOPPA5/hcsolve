"""hcp-974 decoder. Run from repo root: python3 -I ciphers/hcp-974/work/decode.py"""
import hashlib, pathlib, sys
D = pathlib.Path(__file__).resolve().parent.parent
HASHES = {
 'source/picture-large.jpg': 'f553e87a54b376cfe4741e7321a5b55a6c92357b009906adc33b4366d0dfef76',
 'source/address-large.jpg': 'a4cb850e61cefc6b5bd669f4e667ecdcab5c77f0da55a03742a0cb20281fee1a',
 'work/hires/cpc_--27_DE_Bruckenau_DE_Heidelberg_heidelberg-03_pic.jpg': '02c8167d8877c850a9e8fedb9c22da93025dad9de82c0be7f0b7d34de6d2f685',
 'work/hires/cpc_--27_DE_Bruckenau_DE_Heidelberg_heidelberg-03_adr.jpg': '437ec47d5957e616a38890ba6be1ab33443277cb0fa9670b93e3d61b90d3eebe',
}
for p, h in HASHES.items():
    got = hashlib.sha256((D / p).read_bytes()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + p)
    if got != h: sys.exit(1)
# key: digits 1-5 = vowels a e i o u, 6-0 = l m n r s; every other letter plain
KEY = dict(zip('1234567890', 'aeioulmnrs'))
words, out = [], []
for line in (D / 'work/transcription.txt').read_text().splitlines():
    if line.startswith('#') or not line.strip(): continue
    ws = []
    for w in line.split(' / '):
        ws.append(''.join(KEY.get(t, t.lower() if t.isalpha() else t) for t in w.split()))
    out.append(' '.join(ws))
print('\n'.join(out))
