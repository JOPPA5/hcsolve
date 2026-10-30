"""Reviewer's independent decoder: uses hcp-1216/work/graphic-key.json, not the solver's decode.py.
Run from repo root: python3 -I ciphers/hcp-1305/review/work/my_decode.py"""
import json,os,re,subprocess,sys,unicodedata
H=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(H,'..','..','..','..')
G=json.load(open(os.path.join(R,'ciphers/hcp-1216/work/graphic-key.json')))
N={'=':'two-bars','6':'six','(':'left-bowl','d':'joined-two-strokes','E':'three-bars','+':'cross','G':'open-loop-descender','H':'two-tall-strokes','i':'dotted-crossed-curve','J':'inverted-T','K':'section-mark','~':'wave','M':'three-short-strokes','N':'two-short-strokes','O':'cursive-loop','F':'F',')':'right-bowl','T':'gamma','X':'x','V':'chevron','Y':'low-descender','Z':'crossed-diagonal'}
def d(t):
    if t=='?': return '?'
    b,m=t[0],t[1:]
    k=N[b]+({'^':':acute','"':':diaeresis'}.get(m,''))
    return G.get(k) or G[N[b]]
mine={}
for l in open(os.path.join(H,'my_reading.txt'),encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,*t=l.split(); mine[a]=''.join(d(x) for x in t)
out=subprocess.run([sys.executable,'-I',os.path.join(R,'ciphers/hcp-1305/work/decode.py')],capture_output=True,text=True).stdout
sol={}
for l in out.splitlines():
    m=re.match(r'\s*(\d\d|s\d) (\S+)$',l)
    if m: sol[m[1]]=re.sub(r'\[.*?\]','',m[2]).replace('{a|e}','?').replace('{t?}','t')
tot=dif=0
for k,v in mine.items():
    s=sol[k]; tot+=len(v)
    if len(s)!=len(v): print('LEN',k,s,v); continue
    D=[(i,a,b) for i,(a,b) in enumerate(zip(s,v)) if a!=b]; dif+=len(D)
    if D: print(k,'solver',s,'reviewer',v,D)
print('signs',tot,'differences',dif,'rows',len(mine))
print('alphabet',sorted(set(''.join(mine.values()))))
