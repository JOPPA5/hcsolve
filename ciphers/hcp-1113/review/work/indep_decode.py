# Independent reviewer decoder: my own reading of the hi-res scan (rotated), A=2..Z=26 without J.
import string
alpha=[c for c in string.ascii_uppercase if c!='J']
key={i+2:c for i,c in enumerate(alpha)}
rows=[[8,6,12,10,6,3,20,6,18],[19,4,9,2,20,26],[3,10,14],[26,21,18],
      [3,6,19,20,10,(13,2),20,6,14],[19,20,21,14,5,6],[3,6,10],[5,10,18],[5,6,10,14,6],[19,21,19,10]]
def d(n): return key[n[0]]*n[1] if isinstance(n,tuple) else key[n]
print(' '.join(''.join(d(n) for n in w) for w in rows))
