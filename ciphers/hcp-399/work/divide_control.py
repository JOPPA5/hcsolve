from pathlib import Path
import random,json,collections,unicodedata,math
p=Path(__file__).resolve().parent
# New double control uses preserved explicitly invented control plaintext; no targetcrib.
plain=(p/'control-240-plain.txt').read_text().strip();rng=random.Random(2399);keys=[];ct=plain
for w in (20,17):
 k=list(range(w));rng.shuffle(k);keys.append(k);ct=''.join(ct[c::w]for c in k)
(p/'divide-control.txt').write_text(ct+'\n');(p/'divide-control-key.json').write_text(json.dumps(keys))
# Independent Slovak training sentences from shared public UD SNK corpus.
counts=collections.Counter();total=0;sent=[]
source=p.parents[1]/'hcp-393'/'work'/'sk_snk-ud-train.conllu'
for line in source.read_text().splitlines()+['']:
 if not line:
  s=''.join(sent);counts.update(s[i:i+2]for i in range(len(s)-1));total+=max(0,len(s)-1);sent=[]
 elif not line.startswith('#'):
  f=line.split('\t')
  if f[0].isdigit():sent.append(''.join(c for c in unicodedata.normalize('NFD',f[1].lower())if'a'<=c<='z'))
(p/'bigrams.tsv').write_text(''.join(a+b+' '+str(math.log((counts[a+b]+.1)/(total+67.6)))+'\n'for a in 'abcdefghijklmnopqrstuvwxyz'for b in 'abcdefghijklmnopqrstuvwxyz'))
