#!/usr/bin/env python3
"""hcp-1153: verify scan hashes, decode work/transcription.txt with the Mezokovesd key, print the plaintext."""
import hashlib, os, re, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'fa24f2e97e20ef6377502cb9f3de764d40fe2daeb48afe7408c00d2615f34b64',
     'source/address-large.jpg': '3e8d6b4e40acb154d72adc8accec78058558281a14c47b98e07bf97a81951726',
     'work/hires/cpc_1916-06-09_HU_Mezokovesd_HU_Szomolya_szomolya-38_pic.jpg': 'bb9e6c60fbb9f75e7425b7c92f5470e391c0bef468821fbb13d8c64e8f2dda6c',
     'work/hires/cpc_1916-06-09_HU_Mezokovesd_HU_Szomolya_szomolya-38_adr.jpg': '83bca1d7d102176725833a631cec0ba6b1f33b526b55894da4593fc5feb75bde'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1,': 'b', '1.': 'a', '1:': 'e', '1°': 'á', '.1': 'u', ':1': 'ü',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '5.': 'ly', '6': 'j', '6,': 'n', '6.': 'ny',
       '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
# Token flagged ? on the card row -> value by word sense (SOLUTION.md, Uncertainties).
SENSE = {'1?': 'a'}
rows, out, n, odd = [], [], 0, 0
for l in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if l.startswith('#') or not l.strip():
        continue
    tag, body = l.rstrip('\n').split(': ', 1)
    body = re.sub(r'\{[^}]*\}', '', body)
    s = ''
    for t in body.split():
        if t in ')!':
            continue
        n += 1
        if t.endswith('?'):
            odd += 1
            s += SENSE.get(t) or KEY[t[:-1]]
        else:
            s += KEY[t]
    rows.append((tag, s)); out.append(s)
PLAIN = """Édes Margitkám! Értesítlek hogy szerencsésen leértem. Most pedig itt vagyok az állomáson, várom a vonatot,
a vonat még soká jön, tehát ráérek írni, drága Margitkám, itt látok síró asszonyokat amint válnak el az övéiktől,
és most én is iszonyodva gondolok az elválásra, mert még ha mást lát is az ember még az is könnyet csal a szemébe.
lányka jutsz én nékem oly szerény vagy te épen és oly szép is édesem
Most pedig szátalanszor ölel és csókol hű imádód Árpád"""
def norm(s):
    return re.sub(r'[^a-zéöüá]', '', s.replace('Á', 'á').lower().translate(str.maketrans('óőíúű', 'oöiuü')))
got = ''.join(out)
if norm(got).replace('á', 'a') != norm(PLAIN).replace('á', 'a'):
    sys.exit('MISMATCH\n' + norm(got) + '\n' + norm(PLAIN))
print('cipher signs: %d; %d flagged, read by sense; whole card equals the stated reading' % (n, odd))
print()
for t, s in rows:
    print(t, s)
print('''
Mezőkövesd. VI/9

[Édes Margitkám! Értesítlek, hogy szerencsésen leértem. Most pedig itt vagyok az
állomáson, várom a vonatot, a vonat még soká jön, tehát ráérek írni, drága
Margitkám, itt látok síró asszonyokat, amint válnak el az övéiktől, és most én is
iszonyodva gondolok az elválásra, mert még ha mást lát is az ember, még az is
könnyet csal a szemébe.]

Ha ibolyát látok [lányka]
Eszembe [jutsz én nékem]
[Oly szerény vagy te épen]
[És oly szép is édesem]

[Most pedig szá(m)talanszor ölel és csókol hű imádód Árpád]

Address: Őnagysága / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács''')
