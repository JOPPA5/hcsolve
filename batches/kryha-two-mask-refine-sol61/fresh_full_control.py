from pathlib import Path
import json,random,unicodedata,subprocess
B=Path(__file__).resolve().parent;R=B.parents[1];S=R/'batches/kryha-two-mask-language-sol61';ns={'digits':['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'],'unicodedata':unicodedata};s=(R/'batches/kryha-mask-sol61/prepare.py').read_text();exec(s[s.index('def prep('):s.index('train=r/')],ns);prep=ns['prep'];excluded={prep(x)for x in (R/'ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().strip().split('\n\n')};stream=''.join(prep(x)for x in (R/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text().strip().split('\n\n')if prep(x)not in excluded);a=stream[44000:44385];pts=[a,'q'+a[:-1]];g=json.loads((R/'batches/kryha-wheel-sol61/wheel52.json').read_text());co=g['unwrapped_effective_coordinates'];adj=g['adjacent_distances'];rng=random.Random(2335035112);P=rng.sample(range(26),26);O=rng.sample(range(26),26);ip={x:i for i,x in enumerate(P)};io={x:i for i,x in enumerate(O)};cts=[];schedules=[];hs=[]
for pt in pts:
 h=sorted(rng.sample(range(52),23));k=rng.randrange(23);h=h[k:]+h[:k];hs.append(h);jumps=[]
 for x,y in zip(h,h[1:]+h[:1]):
  z=x;v=0
  while True:
   v+=adj[z];z=(z+1)%52
   if z==y:break
  jumps.append(v)
 d=0;ct='';ds=[]
 for i,ch in enumerate(pt):ds.append(d);ct+=chr(97+io[(ip[ord(ch)-97]+d)%26]);d=(d+jumps[i%23])%26
 assert sum(jumps)==179;cts.append(ct);schedules.append(ds)
K=[(schedules[1][21+j]-schedules[0][20+j])%26 for j in range(23)];delta=[(K[(j+1)%23]-K[j])%26 for j in range(23)];data=dict(ciphertexts=[ct[20:375]for ct in cts],ciphertexts_full=cts,O=O,K=K,delta=delta,crop_start=20,crop_end=375,known_output_ring=True);(B/'fresh-full-input.json').write_text(json.dumps(data,indent=2));(B/'fresh-full-truth.json').write_text(json.dumps(dict(plaintexts=pts,Pfull=P,masks_full=hs,O=O,seed=2335035112,TEST_offset=44000,TRAIN_excluded=True),indent=2))
# Correct A-aligned pooled heuristic: B histogram subtracts K[j], not K[0].
H=[[0]*26 for _ in range(23)]
for i in range(354):
 H[i%23][(O[ord(data['ciphertexts'][0][i])-97]-23*(i//23))%26]+=1
 H[i%23][(O[ord(data['ciphertexts'][1][i+1])-97]-23*(i//23)-K[i%23])%26]+=1
freq={l:float(v)for l,v in(x.split()for x in(R/'ciphers/hcp-350/work/ring-unigrams.tsv').read_text().splitlines())};vals=adj+delta+[freq[chr(97+i)]for i in range(26)]+sum(H,[]);run=subprocess.run([str(S/'enumerate-profile')],input=' '.join(map(str,vals)),text=True,capture_output=True,check=True);(B/'fresh-full-profile.txt').write_text(run.stdout);print(run.stdout.splitlines()[0])
