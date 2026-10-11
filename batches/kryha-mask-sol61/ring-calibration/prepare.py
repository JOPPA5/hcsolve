from pathlib import Path
import json,random,unicodedata,hashlib
b=Path(__file__).resolve().parent;r=b.parents[2];g=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));a=g['adjacent_distances'];coord=g['unwrapped_effective_coordinates'];digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat']
# Same independent generic preparation as previous frozen TRAIN models.
def prep(block):
 out=[]
 for line in block.splitlines():
  f=line.split('\t')
  if len(f)>4 and f[0].isdigit():
   s=''.join(digits[int(c)] if c.isdigit() and c.isascii() else c for c in f[1]);s=''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z')
   if s:out.append('q'+s+'q' if f[3]=='PROPN' else s)
 return ''.join(out)+'x'
source=r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';train=r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';trainset={prep(s) for s in train.read_text().strip().split('\n\n')};text=''.join(prep(s) for s in source.read_text().strip().split('\n\n') if prep(s) not in trainset);records=[]
for q,(m,start) in enumerate([(20,15000),(26,16500),(30,18000)]):
 plain=text[start:start+385];assert len(plain)==385;rng=random.Random(52385910+q);stops=sorted(rng.sample(range(52),m));phase=rng.randrange(m);P=rng.sample(range(26),26);O=rng.sample(range(26),26);ip={v:i for i,v in enumerate(P)};op={v:c for c,v in enumerate(O)};jumps=[]
 for j,h in enumerate(stops):
  dist=0;x=h
  while True:
   dist+=a[x];x=(x+1)%52
   if x==stops[(j+1)%m]:break
  jumps.append(dist)
 assert sum(jumps)==179;steps=jumps[phase:]+jumps[:phase];d=0;ct=''
 for i,c in enumerate(plain):ct+=chr(97+op[(ip[ord(c)-97]+d)%26]);d=(d+steps[i%m])%26
 decoded=''
 for i,c in enumerate(ct):h=stops[(phase+i)%m];dist=coord[h]-coord[stops[phase]]+179*((phase+i)//m);decoded+=chr(97+P[(O[ord(c)-97]-dist)%26])
 assert decoded==plain
 rec={'label':f'fresh-m{m}','m':m,'length':385,'plaintext':plain,'ciphertext':ct,'input_slots':P,'output_positions':O,'active_holes_zero_based':stops,'phase':phase,'supplied_schedule':steps,'seed':52385910+q,'prepared_TEST_offset':start,'mask_phase_supplied_but_rings_unknown':True};records.append(rec);folder=b/rec['label'];folder.mkdir(exist_ok=True);(folder/'cipher.txt').write_text(ct+'\n');(folder/'schedule.txt').write_text(' '.join(map(str,steps))+'\n')
(b/'controls.json').write_text(json.dumps(records,indent=2)+'\n');model=r/'ciphers/hcp-350/work';(b/'manifest.json').write_text(json.dumps({'TRAIN_source':str(train.relative_to(r)),'TEST_source':str(source.relative_to(r)),'TEST_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'TEST_not_in_any_TRAIN':True,'frozen_models':{str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [model/'ring-unigrams.tsv',model/'ring-4grams.tsv',model/'ring-5grams.tsv']},'training_fraction':.8,'profile_starts':3000,'profile_steps':10000,'profile_retained':300,'MASC':'8*30000','joint4':'8*100000','joint5':'8*100000 from unchanged4winner','selection':'TRAIN-only language scoring; no ring or plaintext truth supplied'},indent=2)+'\n')
