"""Reviewer's independent decode of HCP1307. My own row transcription (mine.txt) in sign-class
names, read from review/work/crops/; the key is taken from the hcp-1216 SOLUTION.md table.
Compares with the solver's ledger as decoded by a separate token map. Run: python3 -I review/work/my_read.py"""
import os,re,difflib
W=os.path.dirname(os.path.abspath(__file__));D=os.path.dirname(os.path.dirname(W))
K=dict(bar2='a',six='b',cs='cs',dt='d',bar3='e',fx='f',zig='g',hp='h',ic='i',it='j',ss='k',wav='l',st3='m',st2='n',lp='o',fs='r',bwl='s',gam='t',xp='u',chv='v',dsc='y',xd='z')
mine={}
for l in open(W+'/mine.txt',encoding='utf-8'):
    if not l.strip():continue
    lab,*t=l.split();mine[lab]=[K[x.split('.')[0]] for x in t]
S={'=':'a','6':'b','()':'cs','%':'d','E':'e','+':'f','G':'g','H':'h','@':'i','J':'j','K':'k','~':'l','3':'m','2':'n','O':'o','R':'r',')':'s','T':'t','X':'u','V':'v','Y':'y','Z':'z'}
led={}
for l in open(D+'/work/ledger.txt',encoding='utf-8'):
    if not l.strip() or l[0]=='#':continue
    lab,*t=l.split();led[lab]=[S[re.sub(r"['*?^:]+$",'',x)] for x in t]
print('mine',sum(map(len,mine.values())),'ledger',sum(map(len,led.values())))
for k in led:
    a,b=mine[k],led[k]
    if a!=b:
        print(k,'differs');print('  mine  ',''.join(a));print('  ledger',''.join(b))
    print(k,''.join(a)) if a==b else None
