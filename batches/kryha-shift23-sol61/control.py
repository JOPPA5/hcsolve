from pathlib import Path
import json,random,unicodedata,collections,hashlib,subprocess,math
b=Path(__file__).resolve().parent;r=b.parents[1];digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'];ns={'digits':digits,'unicodedata':unicodedata};source=(r/'batches/kryha-mask-sol61/prepare.py').read_text();exec(source[source.index('def prep('):source.index('train=r/')],ns);prep=ns['prep'];tr=r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';te=r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';excluded={prep(s) for s in tr.read_text().strip().split('\n\n')};text=''.join(prep(s) for s in te.read_text().strip().split('\n\n') if prep(s) not in excluded);plain=text[37000:37385];assert len(plain)==385;plains=[plain,'q'+plain[:-1]];rng=random.Random(230350351);O=rng.sample(range(26),26);P=rng.sample(range(26),26);ip={x:i for i,x in enumerate(P)};op={x:i for i,x in enumerate(O)};geom=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));coord=geom['unwrapped_effective_coordinates'];adj=geom['adjacent_distances'];records=[];cipher=[]
for pt in plains:
 h=sorted(rng.sample(range(52),23));phase=rng.randrange(23);h=h[phase:]+h[:phase];jumps=[]
 for j,start in enumerate(h):
  x=start;distance=0
  while True:
   distance+=adj[x];x=(x+1)%52
   if x==h[(j+1)%23]:break
  jumps.append(distance)
 assert sum(jumps)==179;d=0;ct=''
 for i,c in enumerate(pt):ct+=chr(97+op[(ip[ord(c)-97]+d)%26]);d=(d+jumps[i%23])%26
 decoded=''
 for i,c in enumerate(ct):delta=coord[h[i%23]]-coord[h[0]]+(179 if h[i%23]<h[0] else 0)+179*(i//23);decoded+=chr(97+P[(O[ord(c)-97]-delta)%26])
 assert decoded==pt;records.append(dict(plaintext=pt,ordered_holes=h,ciphertext=ct));cipher.append(ct)
positions=rng.sample(range(22,376),25);noisy=list(cipher[1]);edits=[]
for i in positions:
 old=noisy[i];new=old
 while new==old:new=chr(97+rng.randrange(26))
 noisy[i]=new;edits.append(dict(index351_zero=i,before=old,after=new))
pair=[cipher[0],''.join(noisy)];(b/'control-pair.json').write_text(json.dumps(pair)+'\n');(b/'control-truth.json').write_text(json.dumps(dict(seed=230350351,P=P,O=O,records=records,corruptions=edits,prepared_TEST_offset=37000,TRAIN_excluded=True,same_plaintext_shift1=True,m=23,distinct_real52hole_masks=True),indent=2)+'\n')
subprocess.run(['python3',str(b/'ransac.py'),str(b/'control-pair.json'),str(b/'control-ransac.json')],check=True)
result=json.load(open(b/'control-ransac.json'));row=result['rows'][0];units=[u for u in range(26) if math.gcd(u,26)==1];equiv=[(u,k) for u in units for k in range(26) if all(v==(u*p+k)%26 for v,p in zip(row['output_positions'],O))];report=dict(recovered_equivalent_output_ring=bool(equiv),coordinate_equivalences=equiv,best_matched_cells=row['matched_cells'],corruptions=25,physical_encoder_inverse_both_exact=True,trials=result['trials'],TEST_offset37000=True,no_truth_read_by_optimizer=True);assert equiv;(b/'control-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(report)
