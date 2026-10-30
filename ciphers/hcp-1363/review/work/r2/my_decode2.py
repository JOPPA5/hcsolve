# Independent retyping from reviewer's own crops (round 2); not reading solver's JSON.
rows=["Nz Pxo Mpwjoh Cpz","Nboz uibolt","gps dbset pg","Xjoetps Mpwf","gspn","Z P Hjsm"]
sh=lambda s,k:''.join(chr((ord(c.lower())-97-k)%26+97) if c.isalpha() else c for c in s)
print([sh(r,1) for r in rows]); print(sum(c.isalpha() for r in rows for c in r))
words=set("my own loving boy many thanks for cards of windsor love from girl".split())
for k in range(26):
    n=sum(w in words for r in rows for w in sh(r,k).split())
    if n: print(k,n)
import datetime; print(datetime.date(1907,7,19).strftime('%A'))
