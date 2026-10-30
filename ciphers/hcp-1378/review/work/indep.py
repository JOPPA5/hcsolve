# independent decoder: own hand-keyed reading from the reviewer's crops, explicit table, no shared code with work/decode.py
import calendar, string
L=string.ascii_lowercase
T={c:L[(i+25)%26] for i,c in enumerate(L)}
R=["Nz Pxo Cpz","Ibwf J Tfou","dbse pg","Zpvs Hjsm"]
n=0
for l in R:
    o=[''.join(T[c] for c in w.lower()) for w in l.split()]; n+=sum(map(len,o)); print(l,'->',' '.join(o))
print('letters',n,'distinct cipher',len(set(''.join(R).lower().replace(' ',''))))
print('alt w->v OVN; u for w:',''.join(T[c] for c in 'ibuf'),'n for w:',''.join(T[c] for c in 'ibnf'))
print('all 26 shifts of clear words:')
for k in (1,25):
    print(k,''.join(chr((ord(c)-97+k)%26+97) if c.isalpha() else c for c in 'the martyrs memorial oxford thursday'))
print(calendar.day_name[calendar.weekday(1907,11,14)])
