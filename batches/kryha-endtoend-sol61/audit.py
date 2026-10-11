from pathlib import Path
import json,hashlib
b=Path(__file__).resolve().parent;r=b.parents[1];rankpath=b/'pilot-blind-ranked.json';assert rankpath.exists();rows=json.loads(rankpath.read_text());truth=json.loads((b/'pilot-truth.json').read_text());ct=json.loads((b/'pilot-pair.json').read_text());geo=json.loads((r/'batches/kryha-wheel-sol61/wheel52.json').read_text());edges=geo['adjacent_distances'];results=[]
# Independent adjacent-hole walker, not optimizer's absolute-coordinate projection.
for rank,w in enumerate(rows):
 P=w['P'];O=w['O'];assert sorted(P)==sorted(O)==list(range(26));hA,hB=w['masks'];closing=0;hole=hB[-1]
 while hole!=hB[0]:closing+=edges[hole];hole=(hole+1)%52
 beta=(w['K'][0]-closing)%26;whole=[hA,[hB[-1]]+hB[:-1]];texts=[];enc=[]
 for q in range(2):
  holes=whole[q];assert len(set(holes))==23;arcs=[]
  for j in range(23):
   distance=0;x=holes[j];end=holes[(j+1)%23]
   while x!=end:distance+=edges[x];x=(x+1)%52
   arcs.append(distance)
  assert sum(arcs)==179
  d=beta if q else 0;plain='';cipher='';invP={v:i for i,v in enumerate(P)};invO={v:i for i,v in enumerate(O)}
  for i,ch in enumerate(ct[q]):
   p=P[(O[ord(ch)-97]-d)%26];plain+=chr(97+p);cipher+=chr(97+invO[(invP[p]+d)%26]);d+=arcs[i%23]
  texts.append(plain);enc.append(cipher)
 assert texts==w['plaintexts'];assert enc==ct
 affine=[(u,k)for u in range(26)if __import__('math').gcd(u,26)==1 for k in range(26)if all(O[i]==(u*truth['O'][i]+k)%26 for i in range(26))]
 equivalent_input=max((sum(P[(u*j+k)%26]==truth['P'][j]for j in range(26))for u,k in affine),default=0)
 within_rank=sum(z.get('n')==w['n']for z in results)
 used={ord(x)-97 for text in texts for x in text}
 results.append(dict(rank_within_ngram=within_rank,observed_plaintext_alphabet_size=len(used),input_ring_equivalent_slots=equivalent_input,output_ring_affine_gauges=affine,exact_original_masks=[a==z for a,z in zip(whole,truth['masks'])],n=w['n'],rank=rank,score=w['score'],gauge=w['gauge'],beta=beta,exact_plaintext_letters=[sum(a==z for a,z in zip(p,t))for p,t in zip(texts,truth['plaintexts'])],full385_reencryption=[a==z for a,z in zip(enc,ct)],mask_validity=True,plaintexts=texts))
(b/'pilot-independent-audit.json').write_text(json.dumps(dict(blind_ranking_sha256=hashlib.sha256(rankpath.read_bytes()).hexdigest(),truth_read_only_after_blind_ranking_saved=True,results=results),indent=2)+'\n');print(json.dumps([{k:v for k,v in a.items()if k!='plaintexts'}for a in results],indent=2))
