"""Reviewer's independent decode: sign names typed from the reviewer's own crops (row*.png), key from sign shapes.
Run: python3 -I review/work/indep_decode.py from the cipher dir."""
import re, subprocess
K=dict(bar2='a',six='b',pair='cs',ltick='d',bar3='e',hook='g',dcross='i',sect='k',wave='l',str3='m',str2='n',loop='o',
       rtick='h',bowl='s',gam='t',cross='u',chev='v',low='y',zed='z',eff='r',invt='j',
       loopd='ö',crossd='ü',one='1',zero='0',comma=',',dot='.',hy='-')
R=["bowl zed bar3 eff bar3 gam bar3 gam bar3 gam bar3 ltick bar3 bowl invt loop wave bar2 str2 sect bar2 str3",
"six bar3 pair bar3 bowl bowl loop eff bar2 dcross gam str3 bar3 hook sect bar2 rtick gam bar2 str3 str3 bar3 wave low bar3 gam",
"dcross hook bar3 str2 sect loop bowl zed loopd str2 loopd sect dot dcross hook bar2 zed bar2 str2 loop eff crossd hy",
"wave loopd sect rtick loop hook low dcross hook low bowl zed loop wave dcross str3 bar2 eff str2 bar3",
"sect crossd str2 sect gam bar3 hook bar3 zed str2 dcross sect bar3 wave bar3 str2 bar3 bar3 hook low str3 bar2 bowl gam",
"bar3 ltick bar3 bowl bar3 str3 comma sect bar3 ltick chev bar3 bowl bar3 str3 str2 bar3 rtick bar2 eff bar2 hook cross ltick invt loop str2",
"rtick loop hook low eff loopd chev dcross ltick bar3 str2 dcross eff loop sect ltick bar3 one zero eff bar3",
"eff bar3 str2 ltick bar3 zed loop str2 sect bar3 wave wave bar3 str2 str2 dcross dot"]
mine=[''.join(K[t] for t in r.split()) for r in R]
n=sum(len(r.split()) for r in R); print('tokens',n)
sol=open('../../SOLUTION.md',encoding='utf-8').read()
blk=re.search(r'## Literal decipherment\s+```\n(.*?)```',sol,re.S).group(1).strip().splitlines()
blk=[l.split(' ',1)[1] for l in blk]
for i,(a,b) in enumerate(zip(mine,blk),1): print(i,'SAME' if a==b else 'DIFF',a,'' if a==b else b)
from collections import Counter
print(sorted(Counter(t for r in R for t in r.split()).items(),key=lambda x:-x[1]))
