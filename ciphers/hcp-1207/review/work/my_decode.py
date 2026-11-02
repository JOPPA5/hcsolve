"""Reviewer's independent decode of HCP1207. My own row reading from review/work/crops, typed as sign-class
codes before comparing with work/ledger-opus.txt. Run: python3 -I ciphers/hcp-1207/review/work/my_decode.py"""
import re,os,collections
K=dict(b2='a',six='b',bb='cs',tk='D',b3='e',pl='f',hk='G',ij='j',sec='k',w='l',s3='m',s2='n',lp='o',tall='^',cc='i',
 Fr='r',bo='s',ga='t',xx='u',ch='v',lo='y',xd='z',gy='gy',od='ö',dbl='ű')
# tk = long stroke + tick read d; hk = hooked g; both near-homographs, Decoded as d/g after sense calls marked in the row
R="""b0 xd b3 Fr ga b3 ga b3 tk b3 bo b3 gy b3 ga w b3 s2
Fr b3 s3 b3 s2 lo b3 s3 sec cc ch b2 s2 lp s3 tall lp gy b2 w b3 hk
ij lp six six sec b3 tk ch b3 six b3 s2 ga b2 w b2 w ij b2 bo lp
Fr b2 cc s3 bo b2 ij s2 b2 w b2 ga ga b2 w sec b3 w ga xx
tk b2 ga s2 lp s3 tall lp gy b3 s3 cc ga od w b3 s2 lo
s2 lo cc Fr b2 pl b3 w ga b3 s3 six b3 sec od ch b3 ga
sec b3 xd b3 ga s3 b3 Fr ga lp ij b2 s2 ch lp s2 b2 ga tall lp xd
w b3 ga ga b3 s3 ch b3 xd b3 s2 lo b3 w ch b3 b3 bo b3 bo ga b3
ij od s2 ch cc bo xd b2 b3 bo Fr b3 hk b3 w
Fr b3 ga b3 w cc sec w b3 b2 tall cc tall b3 s2 od s3
b3 bo cc gy w b3 hk s2 b2 gy lp six six bo b2 ij s2 b2 w b2
ga lp s3 Fr b2 sec b3 tk b3 s2 b3 s2 b3 bo ga b3 w b2 ga lp hk b2
tall b2 ga lp s3 s3 b3 hk tall b3 bb b2 sec sec b3 bo lp s2
s2 b3 s3 b3 Fr sec b3 xd b3 sec tall b2 xd b2 b3 tk b3 bo b3 s3
cc Fr ij b2 s3 b3 hk tall lp gy s3 cc sec lp s3 b3 gy tall b2 bo xd
ga lp Fr cc b3 sec ga lp w bb b2 sec s3 b2 Fr b2 Fr b2 tk ij lp
s2 lp s2 b3 tk b3 tk b3 bo b3 s3 b2 s3 b3 tk cc w b3 tall b3 ga
s3 xx w b2 bo lp s2 ij lp w tall b2 s3 b2 Fr b3 s2 b3 s3
s3 xx w b2 ga tall b2 ga lp sec s3 b2 hk b2 ch b2 w
b3 tk b3 bo b3 s3 tall b2 ij lp w s3 xx w b2 ga hk lp s2
tk lp w ij lp s2 cc s3 tk lp ij b2 Fr sec cc
cc ij bo lp sec b2 ga hk lp s2 tk lp w ? sec lp tk lp s3
s3 b2 hk b2 pl b3 w od w cc bo ga b3 s2 ch b3 w b3 tk b3 bo b3 s3 cc s3 b2 tk lp ij b2 pl b3 Fr cc"""
R=R.replace('b0 ','bo ')
mine=[''.join(K.get(t,t) for t in l.split()).replace('D','d').replace('G','g') for l in R.split('\n')]
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','work','ledger-opus.txt')
led=[l for l in open(D,encoding='utf-8') if re.match(r'\d\d ',l)]
def dec(l):
    o=''
    for t in l.split()[1:]:
        if t in('7','0','[orakor]'):continue
        o+={'O:':'ö','{?}':'?'}.get(t,t.lower().replace('h','^') if t=='H' else t.lower())
    return o
bad=0
for i,(a,b) in enumerate(zip(mine,map(dec,led)),1):
    f='ok ' if a==b else 'DIFF'; bad+=a!=b
    print(f'{i:02d} {f} {a}'+('' if a==b else f'  | ledger {b}'))
print('rows differing',bad,'of',len(led))
t=''.join(mine); print('signs',len(t),'edesem',t.count('edesem'),'hogy',t.replace('^','h').count('hogy'))
print(collections.Counter(t).most_common())
