"""Independent decoder: applies family key (hcp-1216 table) to reviewer's sign classes; diffs with solver's literal ledger."""
import re,sys,difflib
K=dict(HEAVY='S',SZ='sz',B2='a',B3='e',F='r',GAM='t',INVT='j',LOOP='o',WAVE='l',ST2='n',ST3='m',SIX='b',BL='c',BR='s',X='u',ZX='z',PL='f',Sk='k',G='g',Y='y',DOTC='i',D4='d',HP='h',CHEV='v')
def v(t):
    if t in('HASH','-'):return ''
    if t in('4','1/2'):return t
    b=re.sub(r'(\?|joined|tick|bar|tilted)$','',t)
    if b=='ST1':return '|'
    if b.endswith(':'):return K[b[:-1]]+':'
    return K[b]
L={}
for l in open('my_signs.txt',encoding='utf-8'):
    if l[0]=='#':continue
    p=l.split();L[p[0]]=''.join(v(t) for t in p[1:])
S={}
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip():continue
    p=l.split();s=''.join(re.sub(r'^\[.*\]$','',t) for t in p[1:])
    S[p[0]]=s.replace('cs','cs').replace(':',':').replace('{#}','').replace('{-}','').replace('{R}','T').replace('{s?}','S').replace('{m?}','m')
tot=0
for k in L:
    a=L[k].replace('c'+'s','cs');b=S[k]
    a2=a.replace('g'+'y','gy').replace('n'+'y','ny')
    sim=difflib.SequenceMatcher(None,a2,b).ratio()
    print(k,'SAME' if a2==b else 'DIFF',a2,'' if a2==b else '| solver: '+b)
print('signs',sum(len(l.split())-1 for l in open('my_signs.txt') if l[0]!='#'))
