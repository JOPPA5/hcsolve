import re
sol=[l.split(None,1) for l in open('../../work/ledger.txt',encoding='utf-8') if l[:2].isdigit()]
K={'F':'r',')':'s','X':'u','6':'b','GY':'gy','CS':'cs','N?':'n','M?':'m','[?]':'?','[?]Y':'?y','H':'d','O:dacute':'o'}
mine=open('r2/my_out2.txt').read().split('\n')
for i,(n,r) in enumerate(sol):
    s=''
    for t in r.split():
        if t[0]=='<': s+=t[1:-1].replace('é','e'); continue
        s+=K.get(t,t.lower())
    m=mine[i]
    print(n,'same' if s==m else 'DIFF', '' if s==m else (s,m))
