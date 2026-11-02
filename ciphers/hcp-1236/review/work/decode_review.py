"""Independent decode of the reviewer's ledger; diffs against solver's letters (accents stripped)."""
import re,sys,unicodedata,difflib,os,json
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.join(here,'..','..')
k={'rb':'s','cd':'z','F':'r','G':'t','iT':'j','+':'f','w':'l','x':'u','6':'b','pn':'h','k0':'k'}
for c in 'aedginmkovc': k.setdefault(c,c)
k['gy']='gy';k['cs']='cs'
mine={}
for l in open(here+'/my_ledger.txt',encoding='utf-8'):
    if l[0]=='#':continue
    p=l.split(); mine[p[0]]=''.join(k[t.rstrip("'\"")] for t in p[1:])
sol={}
ks={'F':'r',')':'s','X':'u','6':'b','+':'f','H':'h','GY':'gy','CS':'cs','VT':'vt','I?':'i','A!':'a'}
for l in open(root+'/work/ledger.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip():continue
    p=l.split(); sol[p[0]]=''.join(ks.get(t.split(':')[0],t.split(':')[0].lower()) for t in p[1:])
n=0
for r in mine:
    print(r,mine[r], '' if mine[r]==sol[r] else '  <-- solver: '+sol[r]); n+=len(mine[r])
print('letters',n,'rows differing',sum(mine[r]!=sol[r] for r in mine))
