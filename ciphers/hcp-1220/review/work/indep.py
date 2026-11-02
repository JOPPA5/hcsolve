"""Reviewer's own decoder: sign-class row transcription -> letters; independent of work/decode.py. Diffs against solver ledger."""
import re,sys
K=dict(A='a',B='b',CS='cs',D='d',E='e',F='r',G='t',H='h',I='i',K='k',M='m',N='n',O='o',Q='g',Sbowl='s',T='j',V='v',W='l',X='u',Y='y',Zcross='z',PLUS='f')
K['?']='{?}'
mine={}
for l in open(sys.argv[1]):
    if l[0]=='#' or not l.strip(): continue
    lab,*t=l.split()
    mine[lab]=[K[re.sub(r"[*!.']|\?$",'',x) if x!='?' else '?'] for x in t]
theirs={}
for l in open(sys.argv[2]):
    if l[0]=='#' or not l.strip(): continue
    lab,*t=l.split()
    theirs[lab]=[('{?}' if x=='?' else re.sub(r"[!^]|:.",'',x).replace('H','h')) for x in t if x!='|']
n=0;d=0
for lab in mine:
    print(lab,''.join(mine[lab]),'' if mine[lab]==theirs[lab] else '   DIFF '+''.join(theirs[lab]))
    n+=len(mine[lab]); d+=mine[lab]!=theirs[lab]
print(n,'signs;',d,'rows differ')
from collections import Counter
print(sorted(Counter(x for r in mine.values() for x in r).items()))
