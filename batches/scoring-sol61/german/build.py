from pathlib import Path
from collections import Counter,defaultdict
import unicodedata,re,math,json,random,hashlib
p=Path(__file__).resolve().parent

def norm(w):return ''.join(c for c in unicodedata.normalize('NFD',w.lower().replace('ß','ss')) if 'a'<=c<='z')
rules=defaultdict(list);cross={}
for line in (p/'source/de_DE_frami.aff').read_text(encoding='latin1').splitlines():
 f=line.split()
 if len(f)<4 or f[0] not in ['SFX','PFX']:continue
 if f[2] in ['Y','N']:cross[(f[0],f[1])]=f[2]=='Y';continue
 if len(f)<5:continue
 kind,flag,strip,add,cond=f[:5];strip='' if strip=='0' else strip;add=add.split('/')[0];add='' if add=='0' else add
 rules[kind,flag].append((strip,add,re.compile(('^'+cond) if kind=='PFX' else cond+'$')))
def apply(word,kind,flag):
 for strip,add,rx in rules[kind,flag]:
  if not rx.search(word):continue
  if kind=='SFX' and (not strip or word.endswith(strip)):yield (word[:-len(strip)] if strip else word)+add
  if kind=='PFX' and (not strip or word.startswith(strip)):yield add+(word[len(strip):] if strip else word)
words=set();core=set()
for l in (p/'source/de_DE_frami.dic').read_text(encoding='latin1').splitlines():
 f=l.split()
 if not f or f[0].startswith('#'):continue
 parts=f[0].split('/',1);w=parts[0];flags=parts[1] if len(parts)>1 else ''
 if not w.isalpha():continue
 words.add(norm(w));core.add(norm(w));suff=[]
 for flag in flags:suff+=list(apply(w,'SFX',flag))
 words.update(map(norm,suff))
 for flag in flags:
  words.update(map(norm,apply(w,'PFX',flag)))
  if cross.get(('PFX',flag)):
   for sw in suff:words.update(map(norm,apply(sw,'PFX',flag)))
words={w for w in words if 1<=len(w)<=30}
freq=Counter();masks=defaultdict(int);trans=Counter();sentences=[];prev=8
ud={'NOUN':0,'PROPN':0,'ADJ':1,'VERB':2,'AUX':2,'ADV':3,'ADP':4,'PRON':5,'DET':5,'SCONJ':5,'CCONJ':5,'PART':5,'NUM':6}
for l in (p/'source/de_gsd-ud-train.conllu').read_text().splitlines()+['']:
 if not l:
  if prev!=8:trans[prev,9]+=1
  prev=8;continue
 if l.startswith('# text = '):sentences.append(norm(l[9:]))
 f=l.split('\t')
 if len(f)>4 and f[0].isdigit() and norm(f[1]):
  w=norm(f[1]);t=ud.get(f[3],7);freq[w]+=1;masks[w]|=1<<t;core.add(w);trans[prev,t]+=1;prev=t
counts={n:Counter() for n in [3,4,5]}
for w in words:
 for n in counts:counts[n].update(w[i:i+n] for i in range(len(w)-n+1))
for s in sentences:
 for n in counts:counts[n].update({g:v*100 for g,v in Counter(s[i:i+n] for i in range(len(s)-n+1)).items()})
for n,c in counts.items():
 total=sum(c.values());den=total+.1*26**n
 (p/f'model{n}.tsv').write_text(f'#floor {math.log(.1/den)}\n'+''.join(f'{g}\t{math.log((v+.1)/den)}\n' for g,v in sorted(c.items())))
(p/'words.tsv').write_text(''.join(f'{w}\t{freq[w]}\n' for w in sorted(words|set(freq))))
(p/'words-pos.tsv').write_text(''.join(f'{w}\t{freq[w]}\t{masks[w] or 255}\n' for w in sorted(words|set(freq))))
(p/'core-words.txt').write_text('\n'.join(sorted(core))+'\n')
(p/'pos-transitions.tsv').write_text(''.join(f'{a}\t{b}\t{math.log((trans[a,b]+.5)/(sum(trans[a,t] for t in range(10))+5))}\n' for a in range(9) for b in range(10)))
controls=[('control40','bittewiederholensiedasletzteschreibennun',701333),('holdout43','unserebotschafthatihrschreibenheuteerhalten',701334)]
for name,plain,seed in controls:
 alpha=list('abcdefghijklmnopqrstuvwxyz');random.Random(seed).shuffle(alpha)
 (p/(name+'-plain.txt')).write_text(plain);(p/(name+'-key.txt')).write_text(''.join(alpha))
 (p/(name+'-cipher.txt')).write_text(''.join(alpha[ord(c)-97] for c in plain))
 (p/(name+'-reverse-cipher.txt')).write_text(''.join(alpha[ord(c)-97] for c in plain)[::-1])
r={'dictionary_words':len(words),'core_words':len(core),'sentences':len(sentences),'grams':{n:len(c) for n,c in counts.items()},'sources':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'source').iterdir() if f.is_file()},'controls':{name:{'length':len(plain),'seed':seed,'training_sentence_injection':False} for name,plain,seed in controls}}
(p/'build-report.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
