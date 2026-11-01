# Independent reviewer transcription, written from review/work band crops before diffing against the solver ledger.
# Own notation: one char per sign. A=two bars E=three bars K=S/section D=short-then-long pair H=tall+tick
# N=two equal strokes M=three strokes L=wave O=loop-n shape S=right bowl T=gamma R=F-shape V=chevron Z=crossed tail
# U=plain x I=dotted curve Y=undotted curve J=inverted T G=open loop B=six Q=gy ligature; lowercase in <> = plain cursive
# ? marks a sign I can only place by word sense (blot); () struck.
ROWS="""
KEDVESJOLANKAM
REMELEMHOQELEG
JOLTELNEKORAI
EDESEMLEQ<en>EL
NEZESEL(NEZESE)ILO
NAYLONAIRA?DENA
Q<on>SOKDOLGAVAN
HIQEELEDESEM
?JZAVAROSIRAS
?INTITVANAMIT
LATDATSORAIMZA
VAROSIRASABOL
?ERSZETAKARTAMTEH
?I.EDESEMIR?ONHON
?OQMIUJSAG?OQ
??GODNAKRAJTAMAROSZ
?Y?LVEK.ISTENVELA
VISZONTLATASRA
"""
P=dict(A='a',E='e',K='k',D='d',H='h',N='n',M='m',L='l',O='o',S='s',T='t',R='r',V='v',Z='z',U='u',I='i',Y='y',J='j',G='g',B='b',Q='gy')
def dec(r):
    o='';c=False;i=0
    while i<len(r):
        x=r[i]
        if x=='<':
            j=r.index('>',i);o+=r[i+1:j];i=j+1;continue
        o+=x if x in '().?' else P[x]; i+=1
    return o
import re,unicodedata
led=[]
for l in open('work/ledger.txt',encoding='utf-8'):
    if l[0].isdigit(): led.append(l.split()[1:])
KEY=dict(gy='gy',b2='a',six='b',sl='d',b3='e',lg='g',th='h',dc='i',ud='y',it='j',sec='k',wv='l',s3='m',s2='n',lp='o',Fr='r',rb='s',gm='t',xc='u',ch='v',zc='z')
def sol(ts):
    o=''
    for t in ts:
        if t in '[]': continue
        if t=='.': o+='.'; continue
        if t[0]=='~': o+=t[1:]; continue
        o+=KEY[t.lstrip('?').rstrip("'")]
    return o
tot=0;diff=0
for n,(r,t) in enumerate(zip(ROWS.split(),led),1):
    a=dec(r).replace('(','').replace(')','');b=sol(t)
    tot+=len(b)
    d=[(i,x,y) for i,(x,y) in enumerate(zip(a,b)) if x!=y and x!='?']
    k=[i for i,x in enumerate(a) if x=='?']
    print(f'{n:02} {a}\n   {b}', 'LEN' if len(a)!=len(b) else '', 'DIFF',d,'blots',len(k))
    diff+=len(d)
print('letters',tot,'hard diffs',diff)
from collections import Counter
print(sorted(Counter(x for r in led for x in r if x not in '[].' and x[0]!='~').items(),key=lambda z:-z[1]))
