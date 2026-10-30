# Independent review decode: my own sign-by-sign reading of the hires crops, in my own notation,
# key rebuilt from hcp-1216 sign classes, not from work/decode.py. Compare to the solver's literal rows.
# a=two bars e=three bars etc.: written as sign names separated by spaces.
K=dict(bar2='a',six='b',cs='cs',sT='d',bar3='e',plus='f',g='g',gy='gy',Ts='h',ic='i',invT='j',sect='k',wave='l',s3='m',s2='n',loop='o',F='r',bowl='s',gam='t',ux='u',chev='v',y='y',zx='z')
R='''
sect bar3 sT chev bar3 bowl bar3 gy bar3 gam wave bar3 s2 F bar3
s3 bar3 s2 y bar3 s3 gam ux sT bar2 gam loop s3 Ts loop gy
bowl zx bar3 F bar3 s2 cs bar3 bowl bar3 s2 s3 bar3 g bar3 F sect bar3 zx
gam bar3 s3 bar2 zx ux gam six bar2 s2 gam bar2 wave bar2 wave sect loop zx
gam bar2 s3 bar3 gy sect loop cs ic chev bar2 wave bar2 s3 bar3
wave y ic sect bar3 gam s3 bar3 g gam bar2 s3 bar2 sT
gam bar2 sect bar2 Ts loop gy chev ic bowl zx s2 bar3 sect
plus bar3 wave loop wave six bar3 invT loop gam bar3 sect bar2 F loop sect
bowl zx bar2 wave bar2 bowl six bar2 s2 s3 bar3 g F bar2 ic bowl
wave loop chev loop sT loop zx gam bar3 sect sT bar3 s2 bar3
sect ic ic bowl chev loop wave gam plus bar3 gy chev bar3 F bar3
bar3 s2 s2 bar3 s3 gam bar2 wave bar2 sect loop zx gam bar2 s3
s3 bar3 loop wave y bar2 s2 bar3 six bar3 F bar3 sect bar3 wave
bowl bar3 Ts bar2 wave bar2 ic bowl gam bar3 s2 s2 bar3 sect bar3 zx bar3 wave
six bar3 zx bar2 F loop s3 bowl loop F bar2 ic s3
s3 bar3 F gam s3 bar2 F sect bar3 chev bar3 bowl bar2 ic sT
invT loop s3 ux wave bar2 gam bar2 bowl sect ic chev bar2 s2 loop sect
sT bar2 F bar2 bowl zx gam ic s2 ic bowl gam bar3 s2 chev bar3
bar3 sT bar3 bowl bar3 s3 bar2 gam bar2 chev loop wave six loop wave
ic s3 bar2 sT loop sect bar2 sT chev bar2 bowl bowl bar3 plus bar3 F ic
gam ic bowl zx gam bar3 wave bar3 bar2 sect bar3 sT chev bar2 bowl s3 bar2 s3 bar2 gam
'''
sol=[l.split(None,1) for l in open('work/ledger.txt',encoding='utf8') if l[:1].isdigit()]
import subprocess
out=[''.join(K[t] for t in l.split()) for l in R.strip().splitlines()]
M={'=':'a','6':'b','CS':'cs','/d':'d','E':'e','+':'f','G':'g','GY':'gy','/h':'h','I':'i','J':'j','S':'k','~':'l','3':'m','2':'n','O':'o','F':'r',')':'s','T':'t','X':'u','V':'v','Y':'y','Z':'z'}
for i,(o,(lab,toks)) in enumerate(zip(out,sol),1):
    s=''.join(M[t.split(':')[0]] for t in toks.split())
    print(f'{i:02d} {o}', '' if o==s else f'   <> solver {s}')
from collections import Counter
print(sum(len(l.split()) for l in R.strip().splitlines()),'signs in main rows; types used:',len({t for l in R.split() for t in [l]}))
