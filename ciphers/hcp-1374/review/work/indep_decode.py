# independent: own transcription typed from review crops; shift by -1 via ord arithmetic
import datetime
rows=["Nz Pxo * Cpz","Wfsz jemf tupsn","up Ebz","Nz * zpvs Pxo","* Hjsm"]
d=lambda c:chr((ord(c.lower())-97-1)%26+97)
n=0
for r in rows:
    o=[]
    for w in r.split():
        if w=='*':o.append('[abbr]');continue
        o.append(''.join(map(d,w)));n+=len(w)
    print(r,'->',' '.join(o))
print(n,'letters');print(datetime.date(1907,10,18).strftime('%A'))
for w in ["Wfss","jemf","tupsu","tupsn","tupsz","tupsv"]:print(w,''.join(map(d,w)))
