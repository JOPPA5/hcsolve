"""Independent check: reviewer's own letter-level reading vs solver ledger, sign-count and diff by row.
Run: python3 -I review/work/check.py (cwd = cipher dir)."""
import difflib
KEY={'F':'R',')':'S','X':'U','6':'B','+':'F','H':'H'}
def sol(t):
    b,_,a=t.partition(':'); s=KEY.get(b,b)
    if a: s={'O':'Ö','X':'Ü','U':'Ü'}.get(s,s)
    return s
S={};R={}
for l in open('work/ledger.txt',encoding='utf8'):
    if l[:1].isdigit():
        p=l.split();S[p[0]]=[sol(t) for t in p[1:]]
for l in open('review/work/ledger_reviewer.txt',encoding='utf8'):
    p=l.split();R[p[0]]=['H' if x=='P' else x for x in p[1:]]
n=sum(map(len,S.values()));print('solver tokens',n,'reviewer tokens',sum(map(len,R.values())))
d=0
for k in S:
    if S[k]!=R[k]:
        for op,a,b,c,e in difflib.SequenceMatcher(None,S[k],R[k],autojunk=False).get_opcodes():
            if op!='equal': d+=1;print(k,op,a,S[k][a:b],'->',R[k][c:e],'context',''.join(S[k][max(0,a-4):b+4]))
print('differences',d)
import collections
print(sorted(collections.Counter(x for v in R.values() for x in v).items()))
