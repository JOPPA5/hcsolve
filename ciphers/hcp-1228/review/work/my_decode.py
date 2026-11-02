"""Reviewer's independent decoder: sign shapes -> letters using the family key in hcp-1216/work/graphic-key.json (shape names mapped here)."""
import re,subprocess,sys,difflib,json
R='/Users/tomaspavuk/Desktop/hcsolve/ciphers/'
fam=json.load(open(R+'hcp-1216/work/graphic-key.json'))
M={'2':'two-bars','3':'three-bars','6':'six','w':'wave','s3':'three-short-strokes','s2':'two-short-strokes','L':'cursive-loop',
'J':'joined-two-strokes','G':'gamma','F':'F','R':'right-bowl','S':'section-mark','Z':'open-loop-descender','Y':'low-descender',
'I':'dotted-crossed-curve','T':'inverted-T','C':'chevron','X':'x','Q':'crossed-diagonal','P':'cross'}
EXTRA={'Hk':'h','BB':'cs'}
def d(t):
    if t=='|':return ' '
    if t[0]=='[':return t[1:-1]
    q=t.endswith('?');t=t.rstrip('?')
    acc=':acute' if t.endswith("'") else ':diaeresis' if t.endswith('"') else ''
    t=t.rstrip("'\"")
    v=EXTRA.get(t) or fam[M[t]+acc]
    return '['+v+']' if q else v
mine={}
for l in open(R+'hcp-1228/review/work/my_transcription.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip():continue
    a,*t=l.split();mine[a.lstrip('0') if a[0]=='0' else a]=''.join(d(x) for x in t)
o=subprocess.run(['python3','-I',R+'hcp-1228/work/decode.py'],capture_output=True,text=True).stdout
sol={}
for l in o.split('Literal')[1].split('Normalized')[0].splitlines()[1:]:
    if l.strip():
        a,x=l.split(None,1);sol[a.lstrip('0') if a[0]=='0' else a]=x
n=lambda s:re.sub(r'[\s\[\]]','',s)
tot=diff=0
for k in mine:
    m=mine[k];s=sol[k].replace('[cancelled] ','');tot+=len(n(m))
    print(k.rjust(3),m)
    if n(m)!=n(s):
        print('    SOLVER:',s);diff+=1
print('letters',tot,'rows differing (accents count)',diff)
strip=lambda s:s.translate(str.maketrans('áéóöőúüűí','aeooouuui'))
print('rows differing ignoring accents:',[k for k in mine if strip(n(mine[k]))!=strip(n(sol[k].replace('[cancelled] ','')))])
