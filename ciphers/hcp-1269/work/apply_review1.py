"""One-off: applied the review-1 sign corrections to the ledger and normalized text (kept as a record)."""
p='ciphers/hcp-1269/work/ledger-opus.txt'
s=open(p,encoding='utf-8').read()
R=[('05 K O:diaeresis ) Z O:diaeresis N O G )','05 K O:diaeresis ) Z O:diaeresis N O:dbl G )'),
('Z E N E K A Z A Z O K A','Z N E K A Z A Z O K A'),
('18 F A E D E','18 F A . E D E'),
('20 L O:diaeresis 6','20 L O:dbl 6'),
('F O L A H E Z A L J O:diaeresis','F O L A H A + E L J O:diaeresis'),
('28 CS A K M E F O T','28 CS A K M A F O T'),
('I D E G E N E N','I D E G E N A N'),
('V A N E K K O Z T X','V A N A K O:dbl Z T X'),
('32 L E Z? E G Y','32 L E Z E G Y'),
('S5 V E ) E','S5 V E ) ) E'),
('# Z? = cross sign at right edge, between z and f shapes; ?? = sign under','# ?? = sign under')]
for a,b in R:
    assert s.count(a)==1,a
    s=s.replace(a,b)
s=s.replace('# F=r  )=s','# Corrected after review 1 (rows 5, 15, 18, 20, 23, 28, 30, 32, S5); rows 14-25 rechecked at 2.5-5x.\n# F=r  )=s')
open(p,'w',encoding='utf-8').write(s)
p='ciphers/hcp-1269/work/normalized-opus.txt'
s=open(p,encoding='utf-8').read()
for a,b in [('ha eljön(ne) Pestre','ha feljön(ne) Pestre'),('lapot idegenen,','lapot idegen[?],'),('[? „elez”, feltételez(ni)?]','[? „elez”, „…tehate lez” olvasatlan; feltételez(ni)?]')]:
    assert s.count(a)==1,a
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
p='ciphers/hcp-1269/work/decode_opus.py'
s=open(p,encoding='utf-8').read()
a="""       'Z?': '{z|f}', '??': '{?}',"""
assert a in s
s=s.replace(a,"""       '??': '{?}',""")
open(p,'w',encoding='utf-8').write(s)
