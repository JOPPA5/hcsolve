from pathlib import Path
import json,random,unicodedata,hashlib
b=Path(__file__).resolve().parent;r=b.parents[1];g=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));a=g['adjacent_distances'];coords=g['unwrapped_effective_coordinates'];digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'];ns={'digits':digits,'unicodedata':unicodedata};source=(r/'batches/kryha-mask-sol61/prepare.py').read_text();exec(source[source.index('def prep('):source.index('train=r/')],ns);prep=ns['prep'];tr=r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';te=r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';excluded={prep(s) for s in tr.read_text().strip().split('\n\n')};text=''.join(prep(s) for s in te.read_text().strip().split('\n\n') if prep(s) not in excluded);plains=[text[o:o+385] for o in(23500,25000)];assert all(len(p)==385 for p in plains);rng=random.Random(52770100);holes=sorted(rng.sample(range(52),26));phase=rng.randrange(26);P=rng.sample(range(26),26);O=rng.sample(range(26),26);ip={v:i for i,v in enumerate(P)};op={v:c for c,v in enumerate(O)};jumps=[]
for i,h in enumerate(holes):
 x=h;d=0
 while True:
  d+=a[x];x=(x+1)%52
  if x==holes[(i+1)%26]:break
 jumps.append(d)
assert sum(jumps)==179;records=[]
for q,plain in enumerate(plains):
 ct='';d=0
 for i,c in enumerate(plain):ct+=chr(97+op[(ip[ord(c)-97]+d)%26]);d=(d+jumps[(phase+i)%26])%26
 decoded=''
 for i,c in enumerate(ct):h=holes[(phase+i)%26];dis=coords[h]-coords[holes[phase]]+179*((phase+i)//26);decoded+=chr(97+P[(O[ord(c)-97]-dis)%26])
 assert decoded==plain;records.append({'label':f'message{q}','plaintext':plain,'ciphertext':ct,'prepared_TEST_offset':(23500,25000)[q]})
(b/'control.json').write_text(json.dumps({'known_count':26,'active_holes_zero_based':holes,'phase':phase,'starting_hole':holes[phase],'input_slots':P,'output_positions':O,'seed':52770100,'messages':records,'same_physical_start_reset_each_message':True},indent=2)+'\n');(b/'ciphertexts.txt').write_text('\n'.join(c['ciphertext'] for c in records)+'\n');(b/'coordinates.txt').write_text(' '.join(map(str,coords))+'\n');(b/'manifest.json').write_text(json.dumps({'TRAIN':str(tr.relative_to(r)),'TEST':str(te.relative_to(r)),'TRAIN_sha256':hashlib.sha256(tr.read_bytes()).hexdigest(),'TEST_sha256':hashlib.sha256(te.read_bytes()).hexdigest(),'prepared_TEST_offsets':[23500,25000],'excluded_TEST_sentences_in_any_TRAIN':True,'preparation':'accents stripped, digits spelled, Q propernames, Xsentence markers; exact385segments; ordinary singlepress after everyletter includingJ','known_m':26,'mask_and_both_rings_unknown':True,'message_start':'shared physical start reset for each message; no boundary ngrams'},indent=2)+'\n');print('pair prepared',len(text))
