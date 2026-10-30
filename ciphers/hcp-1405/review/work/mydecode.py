import sys
rows=["Nz Pxo [El] Cpz","J ibwf Cffo","wfsz cvtz","up-Ebz","Nz [N & L] Zpvs","Pxo [Mu] Hjsm"]
def d(c):
    if c.isalpha():
        b=65 if c.isupper() else 97
        return chr((ord(c)-b-1)%26+b)
    return c
n=0
for r in rows:
    out=[]
    for t in r.split():
        if t.startswith('[') or t in('&','L]','[N'): out.append(t); continue
        out.append(''.join(d(c) for c in t).upper()); n+=sum(c.isalpha() for c in t)
    print(' '.join(out))
print(n)
