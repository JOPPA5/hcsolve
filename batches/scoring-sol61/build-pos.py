from pathlib import Path
from collections import defaultdict,Counter
import unicodedata,re,math,json
p=Path(__file__).resolve().parent

def norm(w):return ''.join(c for c in unicodedata.normalize('NFD',w.lower()) if 'a'<=c<='z')
names=['N','A','V','R','P','F','D','X','BOS','EOS']; ids={v:i for i,v in enumerate(names)}
spell={'noun':0,'acronym':0,'adjective':1,'verb':2,'participle':2,'adverb':3,'preposition':4,'conjunction':5,'pronoun':5,'particle':5,'number':6,'interjection':7}
ud={'NOUN':0,'PROPN':0,'ADJ':1,'VERB':2,'AUX':2,'ADV':3,'ADP':4,'PRON':5,'DET':5,'SCONJ':5,'CCONJ':5,'PART':5,'NUM':6}
rules=defaultdict(list);cross={}
for l in (p/'source/sk_SK.aff').read_text().splitlines():
 f=l.split()
 if len(f)<4 or f[0] not in ['SFX','PFX']:continue
 if f[2] in ['Y','N']:cross[(f[0],f[1])]=f[2]=='Y';continue
 if len(f)<5:continue
 kind,flag,strip,add,cond=f[:5];strip='' if strip=='0' else strip;add=add.split('/')[0];add='' if add=='0' else add
 over=next((spell.get(x[3:],7) for x in f[5:] if x.startswith('po:')),None)
 rules[(kind,flag)].append((strip,add,re.compile(('^'+cond) if kind=='PFX' else cond+'$'),over))
def apply(word,tag,kind,flag):
 for strip,add,rx,over in rules[(kind,flag)]:
  if not rx.search(word):continue
  nt=tag if over is None else over
  if kind=='SFX' and (not strip or word.endswith(strip)):yield (word[:-len(strip)] if strip else word)+add,nt
  elif kind=='PFX' and (not strip or word.startswith(strip)):yield add+(word[len(strip):] if strip else word),nt
words=defaultdict(int)
def put(w,t):
 w=norm(w)
 if w and len(w)<=30:words[w]|=1<<t
for l in (p/'source/sk_SK.dic').read_text().splitlines()[1:]:
 f=l.split()
 if not f:continue
 base=f[0].split('/',1);w=base[0];flags=base[1] if len(base)>1 else ''
 if not w.isalpha():continue
 tag=next((spell.get(x[3:],7) for x in f[1:] if x.startswith('po:')),7);put(w,tag);suff=[]
 for flag in flags:suff+=list(apply(w,tag,'SFX',flag))
 for sw,st in suff:put(sw,st)
 for flag in flags:
  for pw,pt in apply(w,tag,'PFX',flag):put(pw,pt)
  if cross.get(('PFX',flag)):
   for sw,st in suff:
    for pw,pt in apply(sw,st,'PFX',flag):put(pw,pt)
freq=Counter();trans=Counter();prev=8
for l in Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().splitlines()+['']:
 if not l:
  if prev!=8:trans[prev,9]+=1
  prev=8;continue
 f=l.split('\t')
 if len(f)>4 and f[0].isdigit() and norm(f[1]):
  w=norm(f[1]);t=ud.get(f[3],7);freq[w]+=1;put(w,t);trans[prev,t]+=1;prev=t
(p/'words-pos.tsv').write_text(''.join(f'{w}\t{freq[w]}\t{mask}\n' for w,mask in sorted(words.items())))
lines=[]
for a in range(9):
 total=sum(trans[a,b] for b in range(10))
 for b in range(10):lines.append(f'{a}\t{b}\t{math.log((trans[a,b]+.5)/(total+5))}\n')
(p/'pos-transitions.tsv').write_text(''.join(lines))
(p/'pos-report.json').write_text(json.dumps({'words':len(words),'tags':names,'diagnostic':{w:words[w] for w in ['bez','jez','predosleho','telegramu','telegramuje']}},indent=2)+'\n')
print('tagged forms',len(words))
