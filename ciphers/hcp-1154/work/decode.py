#!/usr/bin/env python3
"""hcp-1154: verify scan hashes, decode work/transcription.txt, print the full text."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = 'cpc_1915-11-29_HU_Mezokovesd_HU_Szomolya_szomolya-07_'
H = {'source/picture-large.jpg': 'ed4cd973451801d4ac81f20078e5954d1d2c963aca9530e8a311aa9b4c68ecb4',
     'source/address-large.jpg': '7e4f5f970bf000958b4f46919f9a95523f4662553e027c78ef735c28a8d2bf3c',
     'work/hires/' + N + 'pic.jpg': '3f05abc9d9037bebffbdfdac4acb8a4ee498ef9414f990d35abdfe6d4d4d7db3',
     'work/hires/' + N + 'adr.jpg': '08cf397af8d6258bedd2b87ef6887c88bf5cc3f94b010ade581f626f5708d0a7'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
FAMILY = {'0': 'o', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '2.': 'é', '3': 'd', '3,': 'r',
          '3.': 'v', '4,': 'g', '5': 'h', '5,': 'l', '6,': 'n', '7': 'k', '7,': 's', '7.': 'sz',
          '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
NEW = {'4.': 'gy', '.1': 'u', '4': 'f', '6': 'j'}   # not in the hcp-1174/1178/1179 tables; on FINAL sisters such as hcp-1163, 1168
SENSE = {'3.r': 'r'}                                # written 3. (= v), a slip: card has mevt; mert by sense
K = {**FAMILY, **NEW, **SENSE}
words, signs = [], []
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    cur = ''
    for t in line.split():
        if t == '|':
            words.append(cur); cur = ''
        elif t == '!':
            cur += '!'
        elif t == '-':
            cur += '-'
        else:
            cur += K[t]; signs.append(t)
    words.append(cur + '/')
raw = ' '.join(w for w in words if w).replace('-/ ', '').replace('/', '')
print('distinct signs: %d' % len(set(signs)))
print('signs: %d; family table %d, new signs %d, by sense %d'
      % (len(signs), sum(s in FAMILY for s in signs), sum(s in NEW for s in signs), sum(s in SENSE for s in signs)))
print('\nRaw decode (my word division):\n' + raw)
EXPECT = ("kedves margitkám! kedves margitkám nem hiszem hogy nem haragudnál ne is tagad mert tegnap "
          "észre vettem aszt pedig else képzeled hogy fáj ez nekem")
if raw != EXPECT:
    sys.exit('MISMATCH with stated reading')
print('''
Full card ([ ] = enciphered on the card):

[Kedves Margitkám]!

Szerencsésen haza értem, épen a hat órát ütötte a toronyóra mikor a piacra
értem nagyon hideg volt már talán nem is igen megyek <deleted word> Karácsonyig,
de más-/különben [= máskülönben] nem is tudnám megálni, hogy ne menjek.
[Kedves Margitkám nem hiszem hogy nem haragudnál ne is tagad me[r]t tegnap
észre vettem aszt pedig el se képzeled hogy fáj ez nekem.] Sz. A.

Hiába jártam utánad
Reményeim mind elfogytak.
Olyan lett a szívem mint a
jégvirágos téli ablak.   (a stroke is drawn under téli)
Mindnyájatokat csókollak

Address: Tek. Szépreményű Sziber Margitka kisasszonynak / Szomolya / u. p. Bogács.
Postmark: Mezőkövesd, 915 NOV 2-; date note, top right: 1915 XI/29.''')
