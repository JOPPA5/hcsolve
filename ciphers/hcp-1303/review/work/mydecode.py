"""Reviewer's independent decode of HCP1303: sign-class transcription (my own reading of the crops
in review/work/crops, not blind to the ledger) + family key typed from the hcp-1216 legend."""
import re,os,unicodedata
KEY=dict(bar2='a',six='b',cs='cs',d='d',bar3='e',f='f',g='g',hp='h',dot='i',T='j',sec='k',wave='l',s3='m',s2='n',
         loop='o',F='r',bowl='s',gam='t',x='u',chev='v',y='y',z='z')
R="""01 bowl z bar3 F bar3 gam bar3 gam bar3 d bar3 bowl T loop
02 wave bar2 s2 sec bar2 sec dot chev bar2 s2 loop s3
03 hp loop g y bar2 wave bar3 g T loop six six
04 sec bar3 d chev bar3 six bar3 s2 gam bar2 wave bar2 wave T bar2
05 bowl loop F bar2 dot s3 bar3 s2 s3 loop bowl gam
06 hp bar3 bowl gam bar3 s2 gam bar2 F gam loop z
07 sec loop d loop s3 s3 x s2 sec bar2 bar2 z
08 dot gam bowl dot s2 cs hp bar3 bar2 z bar3 F gam
09 bowl bar3 gam bar2 wave loop sec bar3 g y hp bar2 F
10 hp bar3 gam dot g bar2 hp F hp bar2 z bar2
11 s3 bar3 g y bar3 sec s3 bar3 F gam bowl loop F loop
12 z bar2 bowl wave bar3 bowl z bar3 g bar3 bowl z bar3 wave f bar3
13 wave bar3 T gam bar3 gam bar3 s3 bar2 sec loop s2 y chev bar3 gam
14 hp bar2 gam bar3 hp gam dot sec x wave T six bar3 bowl z x wave bar3 dot s3 s2 bar3 sec hp bar2 chev bar2 wave bar2 sec dot
15 six bar3 s3 bar3 g y g y loop s2 g y loop bowl F bar3 s3 dot x T bowl bar2 g bar2 F loop sec bowl z bar2
16 wave bar2 bowl loop s2 hp bar2 chev bar2 s2 dot F T loop s2
s1 dot bowl gam bar3 s2
s2 chev bar3 wave bar3
s3 bar3 d bar3 bowl bar3 s3
s4 dot s3 bar2 d loop
s5 T bar2 f bar3 F dot"""
led={}
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,*t=l.split()
    led[a]=''.join(x.split(':')[0].lower() for x in t if not x.startswith('<') and x!='.')
tot=0;ok=True
from collections import Counter
c=Counter()
for l in R.splitlines():
    a,*t=l.split(); p=''.join(KEY[x] for x in t); tot+=len(t); c.update(t)
    same=p==led[a]; ok&=same
    print(a,p,'' if same else 'DIFF ledger='+led[a])
print('signs',tot,'all equal',ok); print(c.most_common())
print('classes unused:',[k for k in KEY if k not in c])
