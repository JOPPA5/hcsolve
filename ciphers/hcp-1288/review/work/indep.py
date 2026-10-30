"""Reviewer's independent decode of the solver's ledger with a key retyped from the hcp-1216 table;
compares with work/decode.py output and aligns literal letters to the normalized text."""
import re, unicodedata, difflib, collections, subprocess, sys
R='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1288/'
K=dict(A='a',B='b',C='c',D='d',E='e',F='f',G='g',H='h',I='i',J='j',K='k',L='l',M='m',N='n',O='o',P='p',R='r',T='t',V='v',X='u',Y='y',Z='z',CS='cs')
K[')']='s'; K['6']='b'; K['+']='f'; K['?']='?'; K['|']='|'
rows=[];cnt=collections.Counter();n=0
for l in open(R+'work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab,*t=l.split(); n+=len(t); s=''
    for x in t:
        b=x.split(':')[0]; cnt[b]+=1; s+=K[b]
    rows.append((lab,s))
lit=''.join(s for _,s in rows)
print('signs',n,'distinct',len(cnt)); print(cnt.most_common())
for f,*_ in [('S',)]:pass
norm=open(R+'work/normalized.txt',encoding='utf-8').read()
def fold(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if c.isalpha() and not unicodedata.combining(c)); return s
a=lit.replace('?','').replace('|',''); b=fold(re.sub(r'\[sic\]','',norm).replace('Under the stamp',''))
sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
for op,i,j,p,q in sm.get_opcodes():
    if op!='equal': print(op,repr(a[max(0,i-8):i]),'[',a[i:j],'->',b[p:q],']',repr(a[j:j+6]))
