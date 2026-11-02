"""Independent review decode: my own sign-class transcription from enlarged crops (review/work/*.png),
written before comparing to work/ledger.txt. Class names, then key from hcp-1216 table."""
K=dict(bar2='a',six='b',bowlL='c',lng2='d',bar3='e',plus='f',loopG='g',tick='h',dotloop='i',invT='j',sect='k',wave='l',
 str3='m',str2='n',loop='o',F='r',bowlR='s',gam='t',X='u',chev='v',desc='y',zx='z',loopD='o',uml='ö',uuml='ü',UPT='?T',BLOT='#',over8='#')
R='''sect bar3 lng2 chev bar3 bowlR invT loop wave bar2 str2 sect bar2
str3 bar2 F wave bar2 gam loop str3 sect uml zx bar3 wave
bar2 wave loop sect bar2 tick loop zx tick loop loopG desc
sect dotloop X gam bar2 bowlR dotloop gam str2 bar2 sect tick bar2 zx loop sect
six loop wave six loop bowlL bowlR bar2 bowlR loop str2 str3 bar3 loopG
str2 bar3 sect bar3 str3 str3 bar3 F gam bar2 zx gam
uml str2 dotloop gam X lng2 invT bar2 over8 tick loop loopG desc
str3 dotloop invT str2 bar3 tick bar3 zx bar3 str3 F bar3
bar3 bowlR dotloop sect six bar3 bowlL bowlR bar3 tick bar2 zx loop sect loop gam
sect bar3 F uuml wave str2 dotloop tick bar2 plus bar2 UPT
tick bar2 wave loop str3 str3 bar3 loopG sect bar3 wave
gam bar3 str2 bar3 str3 bowlR zx dotloop six uml wave
sect dotloop chev bar2 str2 loop str3 wave bar3 loopG desc bar3 str2
six loop wave lng2 loop loopG six loop wave lng2 loop loopG dotloop gam
bowlR bar2 bar2 zx bar2 gam X lng2 BLOT gam tick loop loopG desc
str3 bar3 loopG gam uml F gam bar3 loopG desc
bowlR zx dotloop chev bar3 gam dotloop bowlR gam bar3 str2 chev bar3 wave bar3
chev loop wave gam sect bar3 lng2 chev bar3 bowlR bowlR bar3 plus bar3 F dotloop'''.split('\n')
mine=[''.join(K[t] for t in r.split()) for r in R]
import re
led=[]
M={'F':'r',')':'s','X':'u','H':'h','+':'f','6':'b','GY':'gy','M?':'','Z#':'z','A#':'#','#':'#','J!':'?T','D!':'h','E?':'e','O:':'ö','X:':'ü'}
for l in open('../../work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    t=l.split()[1:]; led.append(''.join(M.get(x,x.lower()) for x in t))
n=0
for i,(a,b) in enumerate(zip(mine,led),1):
    print(f'{i:02d}',a,'' if a==b else '   <> ledger '+b); n+=a!=b
print('rows differing',n,'signs',sum(len(r.split()) for r in R))
from collections import Counter
print(sorted(Counter(''.join(mine)).items()))
