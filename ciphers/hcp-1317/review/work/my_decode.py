import re,sys
K=dict(b2='a',b3='e',st2='n',st3='m',lt='h',tl='d',S='k',R='s',CC='cs',F='r',G='t',W='l',Xh='u',Xt='z',P='f',I='i',O='o',O2='ö',J='j',Hk='g',Y='y',Ch='v',Six='b')
def dec(t):
    t=t.strip('[]?'); return K[t]
rows={}
for l in open('my_reading.txt',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    a=l.split(); rows[a[0]]=''.join(dec(x) for x in a[1:]); 
# solver ledger
rep=dict(F='r',Fc='r',X='u',T='t'); 
sol={}
for l in open('../../work/ledger.txt',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    a=l.split(); s=''
    for x in a[1:]:
        x=x.strip('[]'); b=x.split(':')[0]; d=':' in x
        m={'F':'r','Fc':'r',')':'s','X':'u','+':'f','T+':'t','CS':'cs','H':'h'}.get(b,b.lower())
        if d and b=='O': m='ö'
        s+=m
    sol[a[0]]=s
n=0;diff=0
for k in rows:
    n+=len(open and rows[k])
    if rows[k]!=sol[k]:
        diff+=1; print('DIFF',k,'\n  rev',rows[k],'\n  sol',sol[k])
    else: print('same',k,rows[k])
print('rows',len(rows),'rows differing',diff)
