"""Reviewer's independent check for HCP1299. Run from repo root with python3 -I.
my_reading.txt: my own eye reading (letter values) from crops of the un-converted scan, typed before diffing.
Decodes solver ledger through the KEY OF HCP1216 (not the solver's dict), then diffs against my reading."""
import json, difflib, os, re, unicodedata
B=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(B,'../../../..')
k=json.load(open(R+'/ciphers/hcp-1216/work/graphic-key.json'))
names={'=':'two-bars','6':'six','(':'left-bowl','4':'joined-two-strokes','#':'three-bars','+':'cross','G':'open-loop-descender',
'H':'two-tall-strokes','P':'tall-short-stroke','i':'dotted-crossed-curve','T':'inverted-T','S':'section-mark','~':'wave','3':'three-short-strokes',
'2':'two-short-strokes','Q':'cursive-loop','F':'F',')':'right-bowl','L':'gamma','X':'x','^':'chevron','Y':'low-descender','Z':'crossed-diagonal'}
def d(t):
    t=t.strip('[]').rstrip(':')
    return 'cs' if t=='CS' else k[names[t]]  # dots ignored: my reading is base letters
led={}; n=0
for l in open(B+'/../../work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,*t=l.split(); led[a]=''.join(d(x) for x in t); n+=len(t)
print('ledger signs',n,'all tokens mapped by 1216 key')
tot=0
for l in open(B+'/my_reading.txt',encoding='utf-8'):
    a,m=l.split(); s=led[a]
    if s!=m:
        for op,i,j,p,q in difflib.SequenceMatcher(None,s,m,autojunk=False).get_opcodes():
            if op!='equal': print(a,op,repr(s[max(0,i-5):i]),repr(s[i:j]),'->',repr(m[p:q])); tot+=max(j-i,q-p)
print('differing letters',tot)
all_=''.join(led.values()); 
for w in ['hogy','edesem','szivem','higyjeel','becsessorait']: print(w,all_.count(w))
