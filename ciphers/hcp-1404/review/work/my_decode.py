# Independent reviewer decode of hcp-1404 (reviewer's own reading of source/address.jpg)
rows = ["Zpvs Pxo", "E-l Hjsm"]   # as read by the reviewer; E-l = abbreviation group
def sh(s, k): return ''.join(chr((ord(c.lower())-97+k)%26+97) if c.isalpha() else c for c in s)
for r in rows:
    print(r, '->', sh(r,-1).upper(), '| +1 instead:', sh(r,1).upper())
for k in range(26):
    print(k, sh("Zpvs Pxo Hjsm", -k))
