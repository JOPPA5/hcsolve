"""Independent decoder for HCP1257 (reviewer). Maps ledger tokens to named graphic classes, then letters via
hcp-1301/work/graphic-key.json (not the solver's KEY). Compares with solver's literal block.
Run: python3 -I ciphers/hcp-1257/review/work/decode_review.py"""
import json,os,re,difflib,subprocess,sys
R='/Users/tomaspavuk/Desktop/hcsolve/ciphers/'
gk=json.load(open(R+'hcp-1301/work/graphic-key.json'))
cls={'A':'two-bars','6':'six','D':'joined-two-strokes','E':'three-bars','+':'cross','G':'open-loop-descender','I':'dotted-crossed-curve',
 'J':'inverted-T','K':'section-mark','L':'wave','M':'three-short-strokes','N':'two-short-strokes','O':'cursive-loop','H':'tall-short-stroke',
 'F':'F',')':'right-bowl','T':'gamma','X':'x','V':'chevron','Y':'low-descender','Z':'crossed-diagonal'}
spec={'CS':'cs','H':'h','N?':'n','E?':'e','L?':'l','I?':'i','Y?':'?','L~':'l','A~':'a','[blot]':'','[o?]':'o','[646]':'','[D]':'d'}
fix={('05','G E T'):'G A T',('15','M I T T E'):'M I T E',('26','G Y E F'):'G Y A F'}
def dec(t):
    b,_,a=t.partition(':')
    if b in spec: return spec[b]
    k=cls[b]+(':'+a if a else '')
    return gk[k]
rows=[];cov={};sp=0
for l in open(R+'hcp-1257/work/ledger-opus.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab,*t=l.split()
    for x in t: cov[x]=cov.get(x,0)+1
    rows.append((lab,t))
lit=[(lab,''.join(dec(x) for x in t)) for lab,t in rows]
tot=sum(len(t) for _,t in rows)
print('rows',len(rows),'tokens',tot,'distinct',len(cov))
print('special',{k:v for k,v in cov.items() if not re.fullmatch(r'[A-Z6+)]|CS|[OX]:diaeresis',k)})
sol=subprocess.run(['python3','-I',R+'hcp-1257/work/decode_opus.py'],capture_output=True,text=True).stdout
s={m.group(1):m.group(2) for m in re.finditer(r'^\s*(\d\d|S\d) (\S+)$',sol,re.M)}
bad=0
for lab,t in lit:
    a=t; b=re.sub(r'\{blot\}|\{646\}','',s[lab]); b=re.sub(r'\{y\?\}','?',b); b=re.sub(r'[{}\[\]]','',b)
    if a!=b: bad+=1;print('DIFF',lab,a,b)
print('rows differing from solver:',bad)
md=open(R+'hcp-1257/SOLUTION.md',encoding='utf-8').read()
miss=[lab for lab in s if lab[0]!='S' and s[lab] not in md]
print('literal rows absent from SOLUTION.md:',miss)
print('corrected rows:')
L=dict(lit)
for lab,old,new in (('05','maget','magat'),('15','mitt','mit'),('26','gyer','gyar')):
    print(lab,L[lab].replace(old,new))
