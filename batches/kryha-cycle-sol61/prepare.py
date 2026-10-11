from pathlib import Path
import random,json,unicodedata,hashlib
b=Path(__file__).resolve().parent;r=b.parents[1];g=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));a=g['adjacent_distances'];coord=g['unwrapped_effective_coordinates'];source=r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';sentences=[s[9:] for s in source.read_text().splitlines() if s.startswith('# text = ')];norm=lambda s:''.join(c for c in unicodedata.normalize('NFD',s.lower()) if 'a'<=c<='z');text='x'.join(norm(s) for s in sentences);records=[]
for q,(m,start) in enumerate([(20,3000),(27,4500),(30,6000)]):
 p=text[start:start+385];assert len(p)==385;rng=random.Random(52619600+q);stops=sorted(rng.sample(range(52),m));phase=rng.randrange(m);I=list(range(26));O=list(range(26));rng.shuffle(I);rng.shuffle(O);position={c:i for i,c in enumerate(I)};out={v:c for c,v in enumerate(O)};jumps=[]
 for j,h in enumerate(stops):
  x=h;d=0
  while True:
   d+=a[x];x=(x+1)%52
   if x==stops[(j+1)%m]:break
  jumps.append(d)
 assert sum(jumps)==179
 d=0;cipher=''
 for i,c in enumerate(p):cipher+=chr(97+out[(position[ord(c)-97]+d)%26]);d=(d+jumps[(phase+i)%m])%26
 # Independent inverse using cumulative coordinates, not direct arc walks.
 d=0;decoded=''
 for i,c in enumerate(cipher):
  decoded+=chr(97+I[(O[ord(c)-97]-d)%26]);h=stops[(phase+i)%m];n=stops[(phase+i+1)%m];d=(d+(coord[n]-coord[h])%179)%26
 assert decoded==p
 # Independent per-cycle displacement, for every pair at whole-cycle lag.
 offsets=[];d=0
 for i in range(385):offsets.append(d);d=(d+jumps[(phase+i)%m])%26
 assert all((offsets[i+m]-offsets[i])%26==23 for i in range(385-m))
 rec={'label':f'control-m{m}','m':m,'plaintext':p,'ciphertext':cipher,'output_positions':O,'input_slots':I,'active_holes_zero_based':stops,'phase':phase,'jumps':jumps,'heldout_offset':start,'seed':52619600+q,'preparation':'UD TEST normalized accents, X sentence boundaries; exact385-letter segment; no selective J extra presses'};records.append(rec);(b/f'control-m{m}.txt').write_text(cipher+'\n')
(b/'controls.json').write_text(json.dumps(records,indent=2)+'\n');(b/'provenance.json').write_text(json.dumps({'source':str(source.relative_to(r)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'model_training':False,'key_seeded_optimization':False,'controls_encode_inverse_exact':3,'all_cycle_displacement_checks_passed':True},indent=2)+'\n')
