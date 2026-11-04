"""hcp-1097: vowel-to-digit substitution a=1 e=2 i=3 o=4 u=5. Run from repo root:
python3 -I ciphers/hcp-1097/work/decode.py"""
import hashlib, pathlib, sys
D = pathlib.Path(__file__).resolve().parent.parent
H = {
 'source/picture-large.jpg': 'd867a0f35bb3a5324511fcf3e3ed3300d49ee9dae7df342ad9bd60e527e55d1b',
 'source/address-large.jpg': 'ffd9104293d2ca427e34ad5bdcf6ee2259a1d247271638460c67812ab3ce9a08',
}
for p, h in H.items():
    got = hashlib.sha256((D / p).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f'HASH MISMATCH {p}')
print('source hashes OK')
KEY = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
lit = []
for line in (D / 'work/transcription.txt').read_text().splitlines():
    if line.startswith('#SIG'):
        sig = line[4:].strip(); dec = ''.join(KEY.get(c, c) for c in sig)
        print(f'{sig:28s} -> {dec}   (signature)'); lit.append(dec); continue
    if not line or line.startswith('#'):
        continue
    out = ''.join(KEY.get(c, c) for c in line)
    lit.append(out)
    print(f'{line:28s} -> {out}')
print('\nLITERAL PLAINTEXT:')
print(' '.join(lit).upper())
