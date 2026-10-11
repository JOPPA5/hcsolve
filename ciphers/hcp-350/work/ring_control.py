from pathlib import Path
from collections import Counter
import unicodedata,math,random,json
p=Path(__file__).resolve().parent
corpus=p.parents[1]/'hcp-393/work/sk_snk-ud-train.conllu';digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat']
def prepare(tokens):
 out=[]
 for word,pos in tokens:
  s=''.join(digits[int(c)] if c.isdigit() and c.isascii() else c for c in word)
  s=''.join(c for c in unicodedata.normalize('NFD',s.lower())if'a'<=c<='z')
  if s:out.append('q'+s+'q' if pos=='PROPN' else s)
 return ''.join(out)+'x'
sentences=[];words=[]
for line in corpus.read_text().splitlines()+['']:
 if not line:
  if words:sentences.append(words);words=[]
 elif not line.startswith('#'):
  f=line.split('\t')
  if f[0].isdigit():words.append((f[1],f[3]))
bound=int(.8*len(sentences));train=[prepare(s)for s in sentences[:bound]];heldout=[prepare(s)for s in sentences[bound:]];quad=Counter();five=Counter()
for s in train:quad.update(s[i:i+4]for i in range(len(s)-3));five.update(s[i:i+5]for i in range(len(s)-4))
uni=Counter(''.join(train));p.joinpath('ring-unigrams.tsv').write_text(''.join(f'{g} {math.log(v/sum(uni.values()))}\n'for g,v in uni.items()))
for n,c in [(4,quad),(5,five)]:p.joinpath(f'ring-{n}grams.tsv').write_text(''.join(f'{g} {math.log(v)}\n'for g,v in c.items()))
plain=''.join(heldout[:20])[:385];assert len(plain)==385
rng=random.Random(350385);slots=list(range(26));outpos=list(range(26));rng.shuffle(slots);rng.shuffle(outpos);inpos={letter:pos for pos,letter in enumerate(slots)};outslot={pos:letter for letter,pos in enumerate(outpos)};steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9];phase=6;sign=-1;d=0;cipher=[]
for i,c in enumerate(plain):cipher.append(chr(97+outslot[(inpos[ord(c)-97]+d)%26]));d=(d+sign*steps[(phase+i)%17])%26
p.joinpath('ring-control-plain.txt').write_text(plain+'\n');p.joinpath('ring-control-cipher.txt').write_text(''.join(cipher)+'\n');p.joinpath('ring-control-key.json').write_text(json.dumps(dict(input_slots=slots,output_positions=outpos,phase=phase,sign=sign,training_sentences=bound,heldout_sentences=len(heldout),preparation='PROPN Q delimiters, digits spelled independently, sentence X markers, accents removed'),indent=2));print('prepared385heldout control; training sentences',bound,'heldout',len(heldout))
