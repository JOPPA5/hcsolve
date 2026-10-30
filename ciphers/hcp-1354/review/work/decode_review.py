# independent transcription, keyed by the reviewer from own 4x crops; decode with explicit table
import string
ct="""Tveefo. dibohf
Jo. ifbejoh pg
mfuufs Npoebz
up. qptu dbse
sfdfjwfe. Tvoebz
? Gps XIZ ! Mpp."""
A=string.ascii_lowercase
t={A[i]:A[i-1] for i in range(26)}
n=0
for l in ct.splitlines():
    print(l.ljust(22),''.join(t[c.lower()] if c.isalpha() else c for c in l).upper()); n+=sum(c.isalpha() for c in l)
print(n,'letters')
txt=''.join(c.lower() for c in ct if c.isalpha())
print('freq',{c:txt.count(c) for c in sorted(set(txt),key=lambda c:-txt.count(c))})
print('absent',[c for c in A if c not in txt])
for k in range(26):
    print(k,''.join(A[(A.index(c)-k)%26] for c in txt)[:30])
