#!/usr/bin/env python3
"""hcp-1160: verify scan hashes, decode work/transcription.txt, print the full plaintext."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '17685f5448a020b0b6e6391340433bfa1cf521a1e04618a363057bbcb1e55ea7',
     'source/address-large.jpg': '5199a690075da4aa258e385d16ed46121730a0117aaa9e8c3a079a9d67694cf3',
     'work/hires/cpc_1915-11-11_HU_Mezokovesd_HU_Szomolya_szomolya-05_pic.jpg': '21eea21852c5dec5a90ed9433c007d75a0fc4dfd8ad9d7aef9c292013bc5816b',
     'work/hires/cpc_1915-11-11_HU_Mezokovesd_HU_Szomolya_szomolya-05_adr.jpg': 'e4c940ef03d51dc05cd9dbd4f4de7a0d6e8da1600afc0fc8052cd3872c9b490b'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '.1': 'u',
       '1,': 'b', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g',
       '4.': 'gy', '5': 'h', '5,': 'l', '5.': 'ly', '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's',
       '7.': 'sz', '8': 'm', '8,': 't', '8.': 'ty', '9': 'p', '9,': 'z', '9.': 'zs'}
ODD = {':1~ü': 'ü',  # üdő: one dot free, the second fused with the stem; `üdő` stands open on the card
       '6~ny': 'ny'}  # könnyet: under the blot the mark has a comma outline; ny is a word-sense restoration
K = {**KEY, **ODD}
SIGN = {':1~ü': ':1', '6~ny': '6.'}  # the sign each ~ token is taken for, for the distinct count
# Expected decoding in the writer's spelling, unaccented where the sign does not mark length.
READ = {
 'L1': 'kedves margitkám',
 'L2': 'a lapodat megkaptam melynek nagyon megörültem',
 'L3': 'kedves margitkám tudhatod hogy ha csak lehet fel megyek de ha nagyon rosz üdö lesz nem mehetek',
 'P1': 'elhervadok porba hullok mint rozsárol a szirom',
 'P2': 'nem ejt könnyet senki értem pusztán áll majd a sirom',
 'P3': 'az erdei kis dalosok zengik el hattyudalom',
 'P4': 'egy boho szegény fiuval kevesebb lesz mondhatom',
 'F1': 'bocsás meg',
 'F2': 'számtalanszor csokollak',
 'V1': 'a fénykép készevan pénszt külgyél le majd kiváltom és feviszem',
}
rows = {}
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    lab, ct = line.rstrip('\n').split('\t')
    rows[lab] = ct
n = odd = 0
OUT = {}
for lab, ct in rows.items():
    ws = []
    for w in ct.split('|'):
        toks = w.split()
        n += len(toks)
        odd += sum(t in ODD for t in toks)
        ws.append(''.join(K[t] for t in toks))
    OUT[lab] = ' '.join(ws)
    if OUT[lab] != READ[lab]:
        sys.exit('MISMATCH %s:\n %s\n %s' % (lab, OUT[lab], READ[lab]))
print('ciphertext signs: %d (%d distinct); %d decode by the table, %d by sense (see ODD)'
      % (n, len({SIGN.get(t, t) for c in rows.values() for t in c.split() if t != '|'}), n - odd, odd))
print('\nRaw decoding (the writer\'s spelling; the signs do not mark o/ó, i/í, u/ú):\n')
for lab in rows:
    print('%s  %s' % (lab, OUT[lab]))
print('''
Full text ([ ] = enciphered):

[Top margin, violet pencil:] [a fénykép készevan, pénszt külgyél le, majd kiváltom és feviszem]

[Kedves Margitkám]! [A lapodat megkaptam, melynek nagyon megörültem. Kedves Margitkám,
tudhatod hogy ha csak lehet fel megyek, de ha nagyon rosz üdő lesz nem mehetek.]

I
[Elhervadok, porba hullok, / mint rózsáról a szirom, /
nem ejt könnyet senki értem, / pusztán áll majd a sírom.]
II
[Az erdei kis dalosok / zengik el hattyúdalom ... /
Egy bohó szegény fiúval / kevesebb lesz, mondhatom.]

ha esetleg rosz üdő lenne és nem mehetnék [bocsás meg] ) [számtalanszor csókollak] ) Mindnyájatokat csókollak.

1915. XI/11. Sz. A.

Address: Szépreménnyü / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács. / Borsod m.''')
