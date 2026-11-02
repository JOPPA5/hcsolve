#!/usr/bin/env python3
"""hcp-1157: verify scan hashes, decode the two digit lines, print the full card text."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'e99219880cfa1f1ef556cc97fb149d4742d9d035eea8a84d14786b85345508c7',
     'source/address-large.jpg': 'aa753b0c191f8d442e0447866347560eb9d8cf7fc29de3b5dd55feeea92f1488',
     'work/hires/cpc_1915-12-03_HU_Mezokovesd_HU_Szomolya_szomolya-08_pic.jpg': '201bda21e69e30a506f9798beb54fdcdf046168acab254ad8cc33fb485620cd8',
     'work/hires/cpc_1915-12-03_HU_Mezokovesd_HU_Szomolya_szomolya-08_adr.jpg': '1c5383d9655d09278cf9166970389b02bd4cf05c3b73293a31d6d9ab11a696b4'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
# Family key (hcp-1174), only signs on this card. 4. = gy is not on that table; it is also on FINAL hcp-1165.
KEY = {'1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '2.': 'é', '3': 'd', '3,': 'r',
       '3.': 'v', '4,': 'g', '4.': 'gy', '6,': 'n', '7': 'k', '7,': 's',
       '8': 'm', '8,': 't'}
C = [("7 1: 3 3. 1: 7,", 'kedves'), ("8 1. 3, 4, 1 8, 7 1' 8", 'margitkám'),
     ("2. 7,", 'és'), ("1' 6, 4. 1 7 1' 8", 'ángyikám')]
out = []
for ct, want in C:
    got = ''.join(KEY[t] for t in ct.split())
    if got != want:
        sys.exit('MISMATCH %r -> %r vs %r' % (ct, got, want))
    out.append(got)
print('ciphertext signs: %d, all decoded by the table (one 7, in Margitkám, is a looped variant form)' % sum(len(c.split()) for c, _ in C))
print()
print('[Kedves Margitkám / És ángyikám /]  (decoded: %s; / = single end stroke)' % ' '.join(out))
print('''Word division as on the card:
Édes anyám már elment csütörtökön Róza itt maradt nem
tudom medig lesz itt.
En a régi kvártélyon háltam pénteken este
demajd az életembe került még most is nagyon
rosszul vagyok a dolog úgy történt hogy a szoba
nagyon hideg volt és vittem szenet és fát magam
voltam egyik inassem hált ott felvoltam
12 óráig mert rendezgettem egyet mást aztán
betüzeltem a kályhába jól meg raktam szénnel
a cső egyhelyen lyukas
én lefeküdtem és egyóra múlva felébredtem bor-
zasztó hányinger fogot elő
aligbírtam felkelni már nem volt erőm az ajtót nagy
nehezen kinyitottam és ki szaladtam az udvarra ) a szén gáz akart megölni
Sz. A.
mindnyájatokat csókollak.
''')
print('Address: Tek. / Szépreményü / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács.')
print('Postmark: MEZŐKÖVESD 915 DEC 3 N C (see SOLUTION.md on the day digit).')
print('[ ] = enciphered on the card; everything else is open text on the card.')
