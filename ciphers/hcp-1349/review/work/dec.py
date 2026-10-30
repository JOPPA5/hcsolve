#!/usr/bin/env python3
# Independent reviewer decoder: own rows typed from reviewer crops; tests all 26 shifts.
rows=["Nz Pxo Cpz","uijt Divsdi Jt","pqqptjuf","Qbsl Qmbdf","uif mbtu pof","pg uijt tupdl","Zpvs Pxo","Hjsm"]
def sh(t,k):
    return ''.join(chr((ord(c.lower())-97-k)%26+97) if c.isalpha() else c for c in t)
for k in (1,):
    for r in rows: print(r,'=>',sh(r,k).upper())
print(sum(c.isalpha() for r in rows for c in r),'letters')
for w in ("Mbsl","Nbsl","Zpsl","Zbsl"): print(w,sh(w,1))
for k in range(26):
    print(k,sh(' '.join(rows[:3]),k)) if k in (0,1,2,25) else None
