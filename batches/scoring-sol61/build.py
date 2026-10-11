from pathlib import Path
from collections import Counter,defaultdict
import unicodedata,re,math,json,hashlib
p=Path(__file__).resolve().parent

def norm(w):return ''.join(c for c in unicodedata.normalize('NFD',w.lower()) if 'a'<=c<='z')
rules=defaultdict(list); cross={}
for line in (p/'source/sk_SK.aff').read_text().splitlines():
 f=line.split()
 if len(f)<4 or f[0] not in ['SFX','PFX']:continue
 if f[2] in ['Y','N']:
  cross[(f[0],f[1])]=f[2]=='Y';continue
 if len(f)<5:continue
 kind,flag,strip,add,cond=f[:5]
 strip='' if strip=='0' else strip;add=add.split('/')[0];add='' if add=='0' else add
 rx=re.compile(('^'+cond) if kind=='PFX' else (cond+'$'))
 rules[(kind,flag)].append((strip,add,rx))
def apply(word,kind,flag):
 for strip,add,rx in rules[(kind,flag)]:
  if not rx.search(word):continue
  if kind=='SFX' and (not strip or word.endswith(strip)):
   yield (word[:-len(strip)] if strip else word)+add
  elif kind=='PFX' and (not strip or word.startswith(strip)):
   yield add+(word[len(strip):] if strip else word)
words=set()
for line in (p/'source/sk_SK.dic').read_text().splitlines()[1:]:
 f=line.split()
 if not f:continue
 token=f[0];parts=token.split('/',1);word=parts[0];flags=parts[1] if len(parts)>1 else ''
 if not word.isalpha():continue
 words.add(norm(word))
 suff=[]
 for flag in flags:
  suff+=list(apply(word,'SFX',flag))
 words.update(map(norm,suff))
 for flag in flags:
  words.update(map(norm,apply(word,'PFX',flag)))
  if cross.get(('PFX',flag)):
   for w in suff:words.update(map(norm,apply(w,'PFX',flag)))
words={w for w in words if 1<=len(w)<=30}
counts={n:Counter() for n in [3,4,5]}
for w in words:
 for n in counts:counts[n].update(w[i:i+n] for i in range(len(w)-n+1))
freq=Counter(); sentences=[]
for line in Path('ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().splitlines():
 f=line.split('\t')
 if len(f)>2 and f[0].isdigit() and norm(f[1]):freq[norm(f[1])]+=1
 if line.startswith('# text = '):sentences.append(norm(line[9:]))
for s in sentences:
 for n in counts:counts[n].update({x:v*10 for x,v in Counter(s[i:i+n] for i in range(len(s)-n+1)).items()})
for n,c in counts.items():
 total=sum(c.values());floor=math.log(0.1/(total+0.1*26**n))
 (p/f'model{n}.tsv').write_text(f'#floor {floor}\n'+''.join(f'{g}\t{math.log((v+0.1)/(total+0.1*26**n))}\n' for g,v in sorted(c.items())))
(p/'words.tsv').write_text(''.join(f'{w}\t{freq[w]}\n' for w in sorted(words|set(freq))))
r={'dictionary_words':len(words),'UD_sentences':len(sentences),'grams':{n:len(c) for n,c in counts.items()},'sources':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'source').iterdir() if f.is_file()},'control_word_coverage_diagnostic_only':{w:w in words for w in ['ziadame','opakovanie','predosleho','telegramu','bez','odkladu']}}
(p/'build-report.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
