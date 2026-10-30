# Independent decode from reviewer's own reading of the rotated hires scan (not from work/transcription.json).
import string
A=string.ascii_lowercase
K=str.maketrans(A+A.upper(),A[-1]+A[:-1]+A.upper()[-1]+A.upper()[:-1])
L=["Nz Pxo Cpz","J bn Tfoejoh","Wbm Gps","Nz Gspn","Zpvs Pxo","Hjsm"]
n=0
for l in L:
    print(l,'->',l.translate(K)); n+=sum(c.isalpha() for c in l)
print('letters incl. Wb? group',n,'excl.',n-3)
for g in ["Wbn","Wbm","Wbo","Wdm","Wdn"]: print(g,g.translate(K))
import datetime;print(datetime.date(1908,1,29).strftime('%A'))
