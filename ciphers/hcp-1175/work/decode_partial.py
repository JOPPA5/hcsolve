# Run from repo root: python3 -I ciphers/hcp-1175/work/decode_partial.py
# PARTIAL key; unknown signs print as [sign].
import hashlib, os
d = 'ciphers/hcp-1175/'
want = {'source/picture-large.jpg': 'c0b0c99ee96d65bc088c2d5cc96299c37ee82c4ebe9b5d56c975965ffa9a1125',
        'source/address-large.jpg': 'e99e3bc4f39e82557231160723e6cbeb2fb73000b29657286fe066dad94ddf28'}
for f, h in want.items():
    assert hashlib.sha256(open(d + f, 'rb').read()).hexdigest() == h, f
key = {'0': 'o', '0,': 'ö', '1.': 'a', '1:': 'e', '1': 'é', '2,': 'cs', '2.': 'i', '3': 'm', '3,': 'r',
       '3.': 'v', '4,': 'f', '4.': 'l', '5': 'h', '5,': 'l', '5.': 'l', '6,': 's', '7': 'k', '7,': 's',
       '7.': 'sz', '8': 'd', '8,': 't'}
for line in open(d + 'work/transcription.txt', encoding='utf-8'):
    if line.startswith('#'): continue
    print(''.join(key.get(t, '[%s]' % t) for t in line.split()))
