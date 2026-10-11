from pathlib import Path
import json,random,unicodedata,hashlib
b=Path(__file__).resolve().parent;r=b.parents[1];ns={'digits':['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'],'unicodedata':unicodedata};s=(r/'batches/kryha-mask-sol61/prepare.py').read_text();exec(s[s.index('def prep('):s.index('train=r/')],ns);prep=ns['prep'];train=r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';test=r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';exclude={prep(s)for s in train.read_text().strip().split('\n\n')};stream=''.join(prep(s)for s in test.read_text().strip().split('\n\n')if prep(s)not in exclude);g=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));edges=g['adjacent_distances'];coords=g['unwrapped_effective_coordinates']
case='second';off=54000;rng=random.Random(6173523222);P=rng.sample(range(26),26);O=rng.sample(range(26),26);a=sorted(rng.sample(range(52),23));start=rng.choice(a);options=[(h,(h+d)%52)for h in a if h!=start for d in [-1,1]if(h+d)%52 not in a];old,new=rng.choice(options);bb=sorted((set(a)-{old})|{new});h=[a[a.index(start):]+a[:a.index(start)],bb[bb.index(start):]+bb[:bb.index(start)]];pt=[stream[off:off+385],stream[off-1:off+384]];assert pt[0][:-1]==pt[1][1:];invP={v:i for i,v in enumerate(P)};invO={v:i for i,v in enumerate(O)};cts=[]
for side in range(2):
 ct='';d=0
 for i,ch in enumerate(pt[side]):
  ct+=chr(97+invO[(invP[ord(ch)-97]+d)%26]);x=h[side][i%23];y=h[side][(i+1)%23]
  while x!=y:d+=edges[x];x=(x+1)%52
 dec=''
 for i,ch in enumerate(ct):
  j=i%23;D=coords[h[side][j]]-coords[start]+179*(h[side][j]<start)+179*(i//23);dec+=chr(97+P[(O[ord(ch)-97]-D)%26])
 assert dec==pt[side];cts.append(ct)
(b/(case+'-pair.json')).write_text(json.dumps(cts)+'\n');(b/(case+'-truth.json')).write_text(json.dumps(dict(plaintexts=pt,P=P,O=O,masks=h,seed=6173523222,TEST_offset=off,one_stop_replacement=[old,new],independent_absolute_inverse_generation_check=True),indent=2)+'\n');(b/(case+'-assumptions.json')).write_text(json.dumps(dict(ciphertext_only_optimizer_input=case+'-pair.json',shared_unknown_random_input_output_rings=True,known_selected_stop_count=23,known_real_geometry='52 holes,179 units',shift_relation='A[i] corresponds to B[i+1]',whole385_bodies=True,one_nearby_stop_difference_is_generator_assumption=True,not_supplied_to_physical_search=True,ring_start_resets='generator d0=0 for both; optimizer may infer arbitrary beta',train_sha256=hashlib.sha256(train.read_bytes()).hexdigest(),test_sha256=hashlib.sha256(test.read_bytes()).hexdigest(),preparation='frozen accent stripping, Q proper names, spoken digits, X sentence boundaries; ordinary presses'),indent=2)+'\n');print('Generated fresh cipher-only second385 pair; truth in separate file.')
