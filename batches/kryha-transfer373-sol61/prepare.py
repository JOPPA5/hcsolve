from pathlib import Path
import json,random,unicodedata,hashlib
b=Path(__file__).resolve().parent;r=b.parents[1]
g=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));coord=g['unwrapped_effective_coordinates'];edges=g['adjacent_distances'];key=json.load(open(b/'transferred-key.json'));P=key['P'];O=key['O']
(b/'known-rings-coordinates.txt').write_text(' '.join(map(str,P+O+coord))+'\n')
ns={'digits':['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'],'unicodedata':unicodedata};source=(r/'batches/kryha-mask-sol61/prepare.py').read_text();exec(source[source.index('def prep('):source.index('train=r/')],ns);prep=ns['prep']
train=r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';test=r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu';exclude={prep(s) for s in train.read_text().strip().split('\n\n')};stream=''.join(prep(s) for s in test.read_text().strip().split('\n\n') if prep(s) not in exclude)
records=[]
for idx,offset in enumerate([61000,63000]):
 plain=stream[offset:offset+650].replace('j','i').replace('x','j');rng=random.Random(3736500+idx);stops=sorted(rng.sample(range(52),23));phase=rng.randrange(23);holes=stops[phase:]+stops[:phase];d0=rng.randrange(26);invP={c:i for i,c in enumerate(P)};invO={p:c for c,p in enumerate(O)};ct='';d=d0
 for i,c in enumerate(plain):
  ct+=chr(97+invO[(invP[ord(c)-97]+d)%26]);h=holes[i%23];nxt=holes[(i+1)%23]
  while h!=nxt:d+=edges[h];h=(h+1)%52
 decoded=''
 for i,c in enumerate(ct):
  j=i%23;delta=coord[holes[j]]-coord[holes[0]]+179*(holes[j]<holes[0])+179*(i//23);decoded+=chr(97+P[(O[ord(c)-97]-d0-delta)%26])
 assert decoded==plain and len(plain)==650
 rec=dict(label=f'control{idx}',seed=3736500+idx,TEST_offset=offset,plaintext=plain,ciphertext=ct,holes=holes,initial_displacement=d0,P=P,O=O,independent_inverse_pass=True);records.append(rec);(b/f'control{idx}.txt').write_text(ct+'\n')
(b/'controls.json').write_text(json.dumps(records,indent=2)+'\n');(b/'manifest.json').write_text(json.dumps(dict(train_sha256=hashlib.sha256(train.read_bytes()).hexdigest(),test_sha256=hashlib.sha256(test.read_bytes()).hexdigest(),rings_source='ciphers/hcp-350/work/kryha-decipherment/key.json',rings_sha256=hashlib.sha256((b/'transferred-key.json').read_bytes()).hexdigest(),known_rings=True,mask_start_displacement_unknown_to_beam=True,preparation='Frozen prep, accent stripping, Q proper names, conditional J sentence delimiter and I/J merging, ordinary presses only'),indent=2)+'\n')
