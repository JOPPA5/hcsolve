#!/usr/bin/env python3
"""Independent check: own retyping from reviewer's crops (not reading the solver's JSON); Caesar sweep."""
rows=["Nz Pxo Mpwf? Cpz","Nboz uibolt","gps dbset pg","Xjoetps Mpwf","gspn","Z P Hjsm"]
def sh(s,k):
    return ''.join(chr((ord(c.lower())-97-k)%26+97) if c.isalpha() else c for c in s)
for r in rows: print(r,'->',sh(r,1))
t=''.join(c for r in rows for c in r if c.isalpha()); print('letters',len(t),'(+1 for the disputed sign = 54)')
words=set('my own boy many thanks for cards of windsor love from girl'.split())
for k in range(26):
    n=sum(sh(w,k) in words for r in rows for w in r.split()); print(k,n,end=' | ')
print()
