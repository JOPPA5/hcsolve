"""Independent decode of review/work/mine.txt and diff with solver's work/ledger.txt.
Run from repo root: python3 -I ciphers/hcp-1224/review/work/verify.py"""
import os,difflib
H=os.path.dirname(os.path.abspath(__file__))
K=dict(sect='k',bar3='e',d='d',chev='v',rb='s',j='j',loop='o',wave='l',bar2='a',st2='n',st3='m',six='b',cs='cs',F='r',i='i',gam='t',g='g',tall='h',y='y',x='z',plus='u',gy='gy',f='f')
K['loop^']='ö';K['plus^']='ü';K['HASH']='#';K['?']='?'
mine={}
for l in open(H+'/mine.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    a,*t=l.split()
    mine[a]=''.join(x.strip('[]') if x[0]=='[' else K[x] for x in t)
print('tokens',sum(len(l.split())-1 for l in open(H+'/mine.txt') if l[0]!='#' and l.strip()))
L={}
for l in open(H+'/../../work/ledger.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    a,*t=l.split()
    s=''
    for x in t:
        if x.startswith('H:'): s+='h'
        elif x=='X': s+='#'
        elif x.startswith('plain:'): s+='43filk'
        elif x=='O:': s+='ö'
        elif x=='U:': s+='ü'
        else: s+=x.lower()
    L[a]=s
for a in mine:
    m=mine[a]; s=L[a]
    if m!=s:
        for op,i,j,p,q in difflib.SequenceMatcher(None,s,m,autojunk=False).get_opcodes():
            if op!='equal': print(a,op,'ledger',repr(s[max(0,i-3):j+3]),'mine',repr(m[max(0,p-3):q+3]))
t=''.join(L.values())
for w in ['hogy','gyöngyösön','edesem','sziv','köszön','köszon']: print(w,t.count(w))
