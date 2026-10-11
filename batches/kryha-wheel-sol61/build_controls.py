from pathlib import Path
import json,random,unicodedata,shutil,hashlib
p=Path(__file__).resolve().parent;repo=p.parents[1];geometry=json.loads((p/'wheel52.json').read_text());a=geometry['adjacent_distances'];coordinates=geometry['unwrapped_effective_coordinates'];digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat']
sentences=[];words=[]
def prepare(tokens):
 out=[]
 for word,pos in tokens:
  word=''.join(digits[int(c)] if c.isdigit()and c.isascii() else c for c in word)
  w=''.join(c for c in unicodedata.normalize('NFD',word.lower())if'a'<=c<='z')
  if w:out.append('q'+w+'q' if pos=='PROPN' else w)
 return ''.join(out)+'x'
source=repo/'ciphers/hcp-393/work/sk_snk-ud-train.conllu'
for line in source.read_text().splitlines()+['']:
 if not line:
  if words:sentences.append(words);words=[]
 elif not line.startswith('#'):
  f=line.split('\t')
  if f[0].isdigit():words.append((f[1],f[3]))
bound=int(.8*len(sentences));heldout=''.join(prepare(s)for s in sentences[bound:]);results=[]
for m,offset in [(20,0),(26,700),(30,1400)]:
 plain=heldout[offset:offset+385];rng=random.Random(52179385+m);stops=sorted(rng.sample(range(1,53),m));phase=rng.randrange(m);P=list(range(26));O=list(range(26));rng.shuffle(P);rng.shuffle(O);I={c:i for i,c in enumerate(P)};inv={i:c for c,i in enumerate(O)};d=0;slot=phase;ct=[];jumps=[]
 for i,h in enumerate(stops):
  to=stops[(i+1)%m];at=h;jump=0
  while True:
   jump+=a[at-1];at=at%52+1
   if at==to:break
  jumps.append(jump)
 assert sum(jumps)==179
 for c in plain:ct.append(chr(97+inv[(I[ord(c)-97]+d)%26]));d=(d+jumps[slot])%26;slot=(slot+1)%m
 ct=''.join(ct);dec=[];d=0;slot=phase
 # Independent inverse calculates arcs from coordinates, not the above walk/jumps.
 for c in ct:
  dec.append(chr(97+P[(O[ord(c)-97]-d)%26]));h=stops[slot];to=stops[(slot+1)%m];arc=(coordinates[to-1]-coordinates[h-1])%179 or 179;d=(d+arc)%26;slot=(slot+1)%m
 assert ''.join(dec)==plain
 folder=p/f'control-m{m}';folder.mkdir(exist_ok=True);(folder/'plaintext.txt').write_text(plain+'\n');(folder/'ciphertext.txt').write_text(ct+'\n');key=dict(active_holes=stops,active_phase_index=phase,starting_hole=stops[phase],input_slots=P,output_positions=O,sign=1,steps=jumps,cycle_sum=179,cycle_residue=23,rng_seed=52179385+m,heldout_offset=offset,preparation='constructed control only: PROPN Q delimiters, decimaldigits spelled, sentenceX, accents removed; ordinary onepress perletter');(folder/'key.json').write_text(json.dumps(key,indent=2));results.append(dict(active_count=m,length=385,encode_inverse_exact=True,phase=phase,cycle_sum=179))
shutil.copyfile(repo/'ciphers/hcp-350/work/ring-4grams.tsv',p/'ring-4grams.tsv')
(p/'controls-verification.json').write_text(json.dumps(dict(results=results,corpus_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),training_sentence_boundary=bound,heldout_sentences=len(sentences)-bound,model='frozen model trained exclusively on first80percent completeUDsentences; heldout uses final20percent',target_data_used=False),indent=2));print(results)
