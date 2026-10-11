from pathlib import Path
from collections import Counter
import random,json,unicodedata,math,hashlib
b=Path(__file__).resolve().parent;r=b.parents[1];g=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));a=g['adjacent_distances'];coord=g['unwrapped_effective_coordinates'];digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat']
def prep(block):
 out=[]
 for line in block.splitlines():
  f=line.split('\t')
  if len(f)>4 and f[0].isdigit():
   s=''.join(digits[int(c)] if c.isdigit() and c.isascii() else c for c in f[1]);s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
   if s:out.append('q'+s+'q' if f[3]=='PROPN' else s)
 return ''.join(out)+'x'
train=r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';blocks=train.read_text().strip().split('\n\n');bound=int(.8*len(blocks));traintexts=[prep(s) for s in blocks[:bound]]
for n in (2,3):
 counts=Counter()
 for text in traintexts:counts.update(text[i:i+n] for i in range(len(text)-n+1))
 (b/f'model{n}.tsv').write_text(''.join(f'{s} {math.log(v)}\n' for s,v in counts.items()))
source=r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';alltrain={prep(s) for s in blocks};text=''.join(prep(s) for s in source.read_text().strip().split('\n\n') if prep(s) not in alltrain);records=[]
for q,(m,start) in enumerate([(20,10000),(26,11500),(30,13000)]):
 plain=text[start:start+385];assert len(plain)==385;rng=random.Random(52119635+q);stops=sorted(rng.sample(range(52),m));phase=rng.randrange(m);P=rng.sample(range(26),26);O=rng.sample(range(26),26);ipos={c:i for i,c in enumerate(P)};out={p:c for c,p in enumerate(O)};jumps=[]
 for j,h in enumerate(stops):
  x=h;d=0
  while True:
   d+=a[x];x=(x+1)%52
   if x==stops[(j+1)%m]:break
  jumps.append(d)
 assert sum(jumps)==179
 d=0;ct=''
 for i,c in enumerate(plain):ct+=chr(97+out[(ipos[ord(c)-97]+d)%26]);d=(d+jumps[(phase+i)%m])%26
 dec=''
 for i,c in enumerate(ct):
  slot=(phase+i)%m;distance=coord[stops[slot]]-coord[stops[phase]]+179*((phase+i)//m);dec+=chr(97+P[(O[ord(c)-97]-distance)%26])
 assert dec==plain
 rec={'label':f'control-m{m}','m':m,'plaintext':plain,'ciphertext':ct,'input_slots':P,'output_positions':O,'active_holes_zero_based':stops,'phase':phase,'starting_hole_zero_based':stops[phase],'seed':52119635+q,'TEST_prepared_stream_offset':start};records.append(rec);folder=b/rec['label'];folder.mkdir(exist_ok=True);(folder/'cipher.txt').write_text(ct+'\n');(folder/'known-rings.txt').write_text(' '.join(map(str,P+O))+'\n')
(b/'controls.json').write_text(json.dumps(records,indent=2)+'\n');(b/'coordinates.txt').write_text(' '.join(map(str,coord))+'\n');(b/'manifest.json').write_text(json.dumps({'train':str(train.relative_to(r)),'test':str(source.relative_to(r)),'TRAIN_sentence_boundary':bound,'train_sha256':hashlib.sha256(train.read_bytes()).hexdigest(),'test_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'n2n3_models':'first80percentTRAINonly, logcounts, unseen floor=-n','n4n5_models':'frozen ciphers/hcp350 ring models, same first80percentTRAINpreparation','preparation':'genuine TEST segments exact385, accentstripped, Qpropernames, digitsspelled, Xsentence; no selectiveJ','known_ring_stage':'true input/outputrings SUPPLIED ONLY for separate mask calibration; mask and phase not supplied'},indent=2)+'\n')
