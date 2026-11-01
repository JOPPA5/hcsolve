"""Reviewer's independent decode: sign names typed from review crops (g*.png, z_*.png), key restated
from the HCP1216 table, not imported from the solver's script. Run: python3 -I indep_decode.py"""
import re,subprocess,os
K=dict(bar2='a',six='b',sl='d',bar3='e',loop='g',iT='j',sect='k',wave='l',s3='m',s2='n',cur='o',
 tall='h',talp='p',F='r',bowl='s',gam='t',x='u',chev='v',zed='z',icr='i',gyy='gy',opp='cs')
R="""sect bar3 sl chev bar3 bowl iT cur wave bar2 s2 sect bar2 s3
gam x sl bar2 gam cur s3 tall cur gyy bowl zed bar3
F bar3 s2 opp bar3 bowl bar3 s2 s3 bar3 loop bar3 F
sect bar3 zed gam bar3 s3 icr loop bar2 zed CROSS tall cur gyy
bar3 gyy sect icr opp bowl zed bar2 wave bar2 sl s2 icr
sect bar3 wave wave bar3 gam sl bar3 bar2 zed bar3 F gam
bar2 six cur wave sl cur loop bowl bar2 loop bar3 F gam
bowl cur sect sect bar2 wave s2 bar2 gyy cur six six
DEL bar2 wave sl cur zed bar2 gam cur sect F bar2
icr bowl sect bar3 talp bar3 bowl wave bar2 s2 s2 bar3 sect
icr bowl gam bar3 s2 chev bar3 wave bar3 bar3 sl bar3 bowl bar3 s3
loop cur s2 sl cur wave iT cur s2 s2 bar3 tall
F bar3 s3 sect icr cur s2 gam gam icr bowl zed
gam bar2 bowl zed icr chev bar3 six cur wave icr s3 bar2 sl
JHEAVY bar2 bar2 gam bar2 chev cur wave six cur wave""".split('\n')
mine=[''.join(K.get(t,'?') for t in r.split()) for r in R]
out=subprocess.run(['python3','-I','ciphers/hcp-1254/work/decode_opus.py'],cwd='../../../..',capture_output=True,text=True).stdout
theirs=[l[4:] for l in out.splitlines() if re.match(r' \d\d ',l)]
for i,(m,t) in enumerate(zip(mine,theirs),1):
    n=t.replace('{+}','?').replace('[deleted]','?').replace('{e|a}','e').replace('{j?}','?').replace('ö','o')
    print(f'{i:02}',m,'SAME' if m==n else 'DIFF '+t)
print('signs',sum(len(r.split()) for r in R))
from collections import Counter
print(sorted(Counter(t for r in R for t in r.split()).items(),key=lambda x:-x[1]))
