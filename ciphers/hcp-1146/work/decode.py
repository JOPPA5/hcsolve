#!/usr/bin/env python3
"""hcp-1146: verify scan hashes, decode work/transcription.txt, print the full text."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': '15a1e3f4fb859e941bd9ece4732828bd1b74339fb545cd787ecbb1697e37b8ff',
     'source/address-large.jpg': '78ed8282bca37c7c6ba03fc31b4ed1f1b1e8012863ba1135334bd0d425372fb1',
     'work/hires/cpc_1916-04-14_HU_Mezokovesd_HU_Szomolya_szomolya-28_pic.jpg': '05947d00c655406688e0d7c189514becfe2919a30725a57d9ce214ef995258ef',
     'work/hires/cpc_1916-04-14_HU_Mezokovesd_HU_Szomolya_szomolya-28_adr.jpg': '01aa86fb3d49159d74f04a85a858a16374cafa564c799c4fe0fc23f37371cea9'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '1,': 'b',
       ':1': 'ü', '.1': 'u', '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v',
       '4': 'f', '4,': 'g', '4.': 'gy', '5': 'h', '5,': 'l', '6': 'j', '6,': 'n',
       '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't', '8.': 'ty',
       '9': 'p', '9,': 'z'}
ODD = {'5~l': 'l',  # hála: no comma seen under the 5
       '8~t': 't',  # mulattatlak: blurred, k-shaped sign under the row above
       '7~s': 's'}  # mégis: sign overwritten, blotted
OVERLAP = {'1.~a': 'a',  # mulattatlak: taken alone looks like 4. ; upper stroke belongs to the row above
           '7~k': 'k'}   # mulattatlak: taken alone looks like a barred 4 ; same overlap
K = {**KEY, **ODD, **OVERLAP}
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ú': 'u', 'ű': 'u', 'É': 'é', 'Á': 'á',
                      'M': 'm', 'I': 'i', 'ú': 'u'})
L = {}; n = odd = ovl = 0; used = set()
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    sec, rest = line.split(' ', 1)
    ct, reading = [s.strip() for s in rest.split('|')]
    toks = ct.split()
    got = ''.join(K[t] for t in toks)
    if got != reading.translate(FOLD):
        sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, reading))
    n += len(toks); odd += sum(t in ODD for t in toks); ovl += sum(t in OVERLAP for t in toks); used |= set(toks)
    L.setdefault(sec, []).append(reading)
print('cipher signs: %d: %d clean by the table, %d by sense, %d read through a stroke overlap; %d distinct table signs\n'
      % (n, n - odd - ovl, odd, ovl, len(used - set(ODD) - set(OVERLAP))))
J = lambda k: '[' + ' '.join(L[k]) + ']'
print(J('T') + '!')
print(J('A') + ' (' + J('P') + ') ' + J('B') + '\n')
print(J('V1') + ',\nDe ' + J('V2') + ',\nOtt maradt az ' + J('V3') + ',\nÉn ' + J('V4') + '.\n')
print('Ezer ember jár az utcán,\nVagy több is tán e városban,\nS én ' + J('V7') + ',')
print('Mert hisz nem ' + J('V8') + '.\n')
print('Sz' + J('V9') + ',\nÉrted [élek lányk]a,')
print('Elmondottam ' + J('V11') + ' is,\nS ' + J('V12') + '.\n')
print('[' + ' '.join(L['C'][:-1]) + '] ([' + L['C'][-1] + '])')
print('Mezőkövesd. 1916. IV/14\n')
print('Address: Őnagysága / Szépreményü / Sziber Margitka / kis-asszonynak / Szomolya / u. p. Bogács. / (Borsod m.)')
print('[ ] = enciphered on the card.')
