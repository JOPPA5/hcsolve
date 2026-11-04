# Independent decoder (reviewer). Own reading of the hi-res scan, typed fresh.
import string
alpha=[c for c in string.ascii_uppercase if c!='J']
key={n+2:c for n,c in enumerate(alpha)}
lines=[[[5,21],[11,12,6,10,14,6,18]],[[3,'15U',19,6,23,10,4,9,20]]]
out=[]
for line in lines:
    for w in line:
        s=''
        for t in w:
            if isinstance(t,str): s+={'O':'Ö'}[key[int(t[:-1])]]
            else: s+=key[t]
        out.append(s)
print(' '.join(out))
