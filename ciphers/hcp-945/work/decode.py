import hashlib, json, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {
 'source/picture-large.jpg': 'dc7ee2eb4f2d3407f3076d0efde4b1d08a324feace6fff62d292d82e9990166f',
 'source/address-large.jpg': '8b9972880b63a59a55dfee37d626aa2b678bfb4441d8e9aa1a86672a8132fa52',
 'work/hires/cpc_1898-04-30_DE_Hagen-in-Westfalen_DE_Malchow-in-Mecklenburg__pic.jpg': 'a15106b1d250cda517cafc000df3a99ad2b457a0723d0191a11824f9feaad1ea',
 'work/hires/cpc_1898-04-30_DE_Hagen-in-Westfalen_DE_Malchow-in-Mecklenburg__adr.jpg': '86fa221b141d5f192364e4fd54db96ec71faf4f701977c31e63cc290b5d9ee08',
}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    if got != h:
        sys.exit('hash mismatch: ' + p)
print('source hashes OK')
key = json.load(open(os.path.join(D, 'work/key.json'), encoding='utf-8'))
lines = []
for ln in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    ln = ln.strip()
    if not ln or ln.startswith('#'):
        continue
    words = [''.join(key[t] for t in w.split()) for w in ln.split(' / ')]
    lines.append(' '.join(words))
for l in lines:
    print(l)
expected = 'meine liebe frieda reise heute nach neheim hüsten dein eduard'
assert ' '.join(lines) == expected, ' '.join(lines)
print('\nReading: Meine liebe Frieda! Reise heute nach Neheim Hüsten. Dein Eduard.')
