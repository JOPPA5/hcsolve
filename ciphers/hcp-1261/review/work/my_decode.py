import re,difflib
K=dict(two='n',three='e',hk='h',bar2='a',Fsign='r',opng='g',cross='u',tkd='d',invT='j',lp='o',gam='t',gyj='gy',dcurve='i',rbowl='s',sect='k',wave='l',strk3='m',zed='z',six='b',sixbowl='cs',ydesc='y',chev='v',dot='.',capM='m',BLOT='*')
K['cross+']='f';K['cross"']='ü';K['lp"']='ö'
d=open('../../work/ledger-opus.txt',encoding='utf-8')
L={}
for l in d:
    if l.strip() and l[0]!='#':
        a,*t=l.split();L[a]=[x for x in t]
def norm(t):
    t=t.replace('X:d','ü').replace('O:d','ö').replace('O:a','o').rstrip('!?')
    m={'F':'r',')':'s','X':'u','6':'b','+':'f','GY':'gy','CS':'cs','P':'h','.':'.'}
    return m.get(t,t.lower())
same=tot=0
for l in open('my_reading.txt',encoding='utf-8'):
    if l[0]=='#':continue
    a,*t=l.split()
    mine=[K[x] for x in t]; his=[norm(x) for x in L[a]]
    print(a,''.join(mine))
    for op,i,j,p,q in difflib.SequenceMatcher(None,mine,his,autojunk=False).get_opcodes():
        if op=='equal': same+=j-i
        else: print('   DIFF',op,mine[i:j],his[p:q])
    tot+=len(his)
print('agree',same,'of',tot)
