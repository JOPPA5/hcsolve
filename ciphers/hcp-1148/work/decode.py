#!/usr/bin/env python3
"""hcp-1148: check scan hashes, decode work/transcription.txt, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = 'cpc_1916-05-09_HU_Mezokovesd_HU_Szomolya_szomolya-34'
H = {'source/picture-large.jpg': 'd4a8b41bc559d3def5de0bda1512711a8af44da8b1b381a8e0f304cb19499204',
     'source/address-large.jpg': 'a2a1c967817200c2c35b3ee54b8671b986d35f85fa51e8db186a0737ce4a5a3d',
     'work/hires/%s_pic.jpg' % B: '2d307ae8b67b7f778ceed52571fa9189790a425af75654beceba579a02062724',
     'work/hires/%s_adr.jpg' % B: 'eb5f55b9653acc3e4adf5eb68724359736c7263496cda04c2121625a39c5d0ce'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '.1': 'u', '1,': 'b',
       '0': 'o', '0,': 'ö', '2': 'c', '2,': 'cs', '2.': 'é',
       '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '6.': 'ny',
       '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
# .1 is u, ú and, in this writer's one-dot form, also ü, ű (keresztül, üdvözöl, hű).
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ű': 'ü', 'ú': 'ü', 'u': 'ü'})
from collections import Counter
used = Counter()
words, blocks, n, odd = [], [], 0, 0
for ln in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    ln = ln.strip()
    if ln.startswith('# Block'):
        words = []; blocks.append(words)
    if not ln or ln[0] == '#':
        continue
    word, ct = ln.split(' = ')
    got = ''
    for t in ct.split():
        if t == '/':
            continue
        n += 1
        used[t.split('~')[0]] += 1
        if '~' in t:
            sign, val = t.split('~'); odd += 1
            got += val
        else:
            got += KEY[t]
    if got.translate(FOLD) != word.lower().translate(FOLD):
        sys.exit('MISMATCH %r -> %r' % (ct, got))
    words.append(word)
print('cipher signs: %d; %d decode by the table, %d by word sense (marked ~ in transcription)\n'
      % (n, n - odd, odd))
print('distinct signs on the card: %d, of %d in the key; counts: %s\n'
      % (len(used), len(KEY), ' '.join('%s=%d' % kv for kv in sorted(used.items()))))
print('Block 1:', ' '.join(blocks[0]))
print('Block 2:', ' '.join(blocks[1]))
print('Block 3:', ' '.join(blocks[2]))
print('\nOpen text on the card: Mezőkövesd 1916. V/9')
print('Address: Tek. Sziber Margitka Kisasszonynak, Borsodm., Szomolya, u.p. Bogács')
