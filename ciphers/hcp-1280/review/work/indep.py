"""Reviewer's independent decode. Sign classes were transcribed by the reviewer from review/work/crops,
before comparison with work/ledger.txt; key is the HCP1216 table, typed separately. Run from cipher dir."""
import re,unicodedata
KEY=dict(bar2='a',six='b',cs='cs',d='d',bar3='e',cross='f',G='g',Gy='gy',icur='i',T='j',sec='k',wv='l',wvy='ly',
 m3='m',n2='n',loop='o',p='p',F='r',rb='s',gam='t',chev='v',xt='z')
R="""
bar3' d bar3 rb T loop wv bar2 n2 sec bar2 m3 chev bar2 F
chev bar2 F? gam rb loop F bar2 icur m3 bar3 G sec bar2 p
gam bar2 m3 m3 bar3 wvy? icur G bar2 xt bar2 n2
rb loop sec Gy loop: gam F bar3 wv bar3 m3 gam loop" wv
m3 bar3 n2 gam bar3 gam cross bar3 wv cross loop G bar2 d
T bar2 bar3' F gam bar3 sec loop rb? xt loop" n2 bar3 gam bar3
m3 bar3 gam m3 bar3 wvy F bar3 wv bar3 chev bar3' wv
six bar3 n2 chev bar2' wv? bar2 rb xt loop wv loop sec d bar3
m3 loop rb gam n2 icur n2 cs icur d loop" m3
icur rb gam bar3 n2 chev bar3 wv bar3 bar2 chev icur rb xt loop n2 gam
wv bar2' gam bar2 rb F bar2 bar2 sec icur gam icur rb xt
gam bar2 rb xt icur chev bar3' six loop wv bar3' rb loop wvy
cross loop F loop n2 rb? xt bar3 F bar3 gam icur
bar2 sec bar2 F bar2 wv chev bar2 bar2 sec bar2 F bar3' six F bar3 n2
gam bar3 chev bar2 Gy bar2 xt bar3 rb xt bar3 m3 six bar3
"""
M={"'":'́',':':'̈','"':'̋'}
def dec(t):
    q=t.endswith('?'); t=t.rstrip('?'); m=t[-1] if t[-1] in M else ''; t=t.rstrip("':\"")
    s=KEY[t]; 
    if m: s=unicodedata.normalize('NFC',s+M[m])
    return s
mine=[''.join(dec(t) for t in l.split()) for l in R.strip().splitlines()]
led=[]
for l in open('work/ledger.txt',encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        o=''
        for t in l.split()[1:]:
            if t=='-':continue
            b,_,m=t.partition(':'); b=b.rstrip('!').lower()
            o+=unicodedata.normalize('NFC',b+{'a':'́','d':'̈','dd':'̋','':''}[m])
        led.append(o)
for i,(a,b) in enumerate(zip(mine,led),1):
    print(f'{i:02} {"same" if a==b else "DIFF"} {a}'+('' if a==b else f'  | ledger {b}'))
print('signs:',sum(len(l.split()) for l in R.strip().splitlines()),'rows',len(mine))
