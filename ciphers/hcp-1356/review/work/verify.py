import datetime,string
# reviewer's own transcription from review/work/*.png; ? = letter under blot
T="Nz px? Efbsftu Cpz Nboz uibolt gps bmm uijt npsojoh Xjui Mpwf Gspn Zp?s Hjsm"
u=string.ascii_uppercase
print(''.join(u[u.index(c)-1] if c in u else c for c in T.upper()))
print(sum(c.isalpha() for c in T),'letters read +',T.count('?'),'blots')
for d in (24,25,26): print(d,datetime.date(1907,3,d).strftime('%A'))
# brute shifts
for k in range(26):
    s=''.join(u[(u.index(c)-k)%26] if c in u else c for c in T.upper())
    print(k,s[:40])
