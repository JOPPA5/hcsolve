import sys
lines=["Nz. Efbsftu. uibolt -","gps. mfuufs ju. Xbt","gjof [**] N yy gspn","Zpvs. pxo. Hjsm"]
def d(c):
    if c.isalpha():
        b=ord('A') if c.isupper() else ord('a')
        return chr((ord(c)-b-1)%26+b)
    return c
n=0
for l in lines:
    out=''.join(d(c) for c in l) if '[**]' not in l else l.split('[**]')[0].translate({})
    out=''.join(d(c) if not (i>=l.find('[') and i<=l.find(']') and '[' in l) else c for i,c in enumerate(l))
    n+=sum(c.isalpha() for c in l)
    print(f"{l:24} -> {out}")
print("letters:",n)
