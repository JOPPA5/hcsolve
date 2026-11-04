"""hcp-1201: number substitution A=1 ... V=22, X=23 (25-letter French alphabet without W).
Run from repo root: python3 -I ciphers/hcp-1201/work/decode.py"""
import hashlib, pathlib
D = pathlib.Path(__file__).resolve().parent.parent
HASHES = {
 'source/address-large.jpg': '488fd2c9a7a8b9c7f2977c6915ddd7cc9b2e445dd7190a2cb53b880c7930dd5e',
 'source/picture-large.jpg': 'd45d76e4809812db766b17ab897675f8d2033e0e62ba097fde464f326228a570',
 'work/hires/cpc_1901-03-05_DE_Kiel_DE_Zeitz_hedwigzipfel-13_adr.jpg': 'f0709e7622200113b7c8b3d0474b7b0302769b214fa48293f937a6f73cd21233',
 'work/hires/cpc_1901-03-05_DE_Kiel_DE_Zeitz_hedwigzipfel-13_pic.jpg': '2f4b940125318bc3cc73293a79c2c3ff8da4da5621a1066e9999c6a91e3a59a5',
}
for p, h in HASHES.items():
    got = hashlib.sha256((D / p).read_bytes()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + p)
    assert got == h
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'  # no W
KEY = {i + 1: c for i, c in enumerate(ALPHA)}
lines = [l for l in (D / 'work/transcription.txt').read_text().splitlines() if l and not l.startswith('#')]
for l in lines:
    nums = [int(x) for x in l.split('-')]
    print(l, '->', ''.join(KEY[n] for n in nums))
print('Line 1 position 5 is written 3 (=C); the word needs E (=5): sender slip -> SOUVENIR')
print('Plaintext: Souvenir affectueux. / Devine / A. M')
