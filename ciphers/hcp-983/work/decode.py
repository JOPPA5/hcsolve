"""hcp-983: number substitution, I/J merged alphabet (A=1 ... H=8, I/J=9, K=10 ... T=19).
Run from repo root: python3 -I ciphers/hcp-983/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
 'source/picture-large.jpg': '588bde2324df8f27080347810cc3b99bf1180fc6ad26c0d7b3d0847d3b9ca491',
 'source/address-large.jpg': '9ea9d0f8255fb8ab1a57a5ad8525041b316644e4daf277d07a24fded0fcc65f1',
 'work/hires/cpc_--___DE_Endsee__pic.jpg': 'd8c93dc9cfd099093173630b6a110fb0a9f3ab6bfd8b0158bda3a73eea5fb4a4',
 'work/hires/cpc_--___DE_Endsee__adr.jpg': '0c2e485078632080ed3bfdbc3d252e298777356482ae2ba93a5306f0a08e0ba7',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    if got != h: sys.exit('hash mismatch: ' + p)
print('source hashes OK')
ALPH = 'ABCDEFGHIKLMNOPQRST'   # 9 = I/J; only values 1-19 occur on the card, so the key is given only up to T (20+ unattested)
KEY = {i + 1: ('I/J' if c == 'I' else c) for i, c in enumerate(ALPH)}
for line in open(os.path.join(D, 'work/transcription.txt')):
    if line.startswith('#') or not line.strip(): continue
    words = []
    for w in line.split('/'):
        nums = [int(n) for n in w.strip().split('.') if n]
        words.append(''.join(KEY[n] for n in nums))
    print(line.strip(), ' => ', ' '.join(words))
