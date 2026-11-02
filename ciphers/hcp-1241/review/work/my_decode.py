"""Independent decode: reviewer's neutral sign list + key rebuilt from hcp-1216/work/graphic-key.json; diff with solver literal output."""
import json,re,subprocess,sys,collections
R='/Users/tomaspavuk/Desktop/hcsolve/ciphers/'
gk=json.load(open(R+'hcp-1216/work/graphic-key.json',encoding='utf-8'))
N={'B2':'two-bars','B3':'three-bars','ST3':'three-short-strokes','ST2':'two-short-strokes','ST':'joined-two-strokes','GM':'gamma','RB':'right-bowl',
'DCC':'dotted-crossed-curve','WV':'wave','OL':'open-loop-descender','LD':'low-descender','CL':'cursive-loop','SX':'six','SEC':'section-mark',
'PX':'x','ZX':'crossed-diagonal','CR':'cross','IT':'inverted-T','CH':'chevron','F':'F'}
def d(t,cnt):
    cnt[t.rstrip(":'")]+=1
    if t=='.':return '.'
    if t=='TS':return '{h/p}'
    if t=='OB':return 'cs'
    if t=='FL':return '{FL}'
    if t=='BLOT':return '{BLOT}'
    m=''
    if t[-1]==':':m=':diaeresis';t=t[:-1]
    if t[-1]=="'":m=':acute';t=t[:-1]
    k=N[t]+m
    return gk[k] if k in gk else gk[N[t]]+m
cnt=collections.Counter();mine=[]
for l in open('my_signs.txt',encoding='utf-8'):
    if l.startswith('#'):continue
    lab,*ts=l.split(); mine.append(''.join(d(t,cnt) for t in ts))
out=subprocess.run([sys.executable,'-I',R+'hcp-1241/work/decode.py'],capture_output=True,text=True).stdout
sol=[l.split(' ',1)[1] for l in out.splitlines() if re.match(r'\d\d ',l)]
def canon(s):
    s=s.replace('{h/p}','#').replace('{FL}','?').replace('{BLOT}','?').replace('{b?}','?').replace('[s]','?').replace('.','')
    return s.replace('h','#').replace('p','#')
bad=0
for i,(a,b) in enumerate(zip(mine,sol),1):
    print(i,a)
    a2,b2=canon(a),canon(b)
    if a2!=b2: bad+=1;print('  DIFF solver:',b)
print('rows',len(mine),len(sol),'diff rows',bad,'signs',sum(v for k,v in cnt.items() if k!='.'),'marks',cnt['.'])
print(sorted(cnt.items(),key=lambda x:-x[1]))
