from pathlib import Path
import json
b=Path(__file__).resolve().parent;r=b.parents[3];a=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'))['adjacent_distances'];weights={2:.1,3:.15,4:.4,5:.8};models={n:{s:float(v) for s,v in (line.split() for line in (r/f'batches/kryha-mask-sol61/model{n}.tsv' if n<4 else r/f'ciphers/hcp-350/work/ring-{n}grams.tsv').read_text().splitlines())} for n in range(2,6)};cases=json.load(open(b/'controls.json'))
if (b/'targets.json').exists():cases+=json.load(open(b/'targets.json'))
results=[];count=0
for c in cases:
 path=b/(c['label']+'.tsv')
 if not path.exists():continue
 data=path.read_text();data=data[:data.rfind('\n')+1];rows=[]
 for line in data.splitlines():
  m,off,anchor,rank,score,holes,plain=line.split('\t');m=int(m);off=int(off);anchor=int(anchor);holes=list(map(int,holes.split(',')));assert len(set(holes))==len(holes)==m and holes[0]==anchor;assert all((holes[i+1]-anchor)%52>(holes[i]-anchor)%52 for i in range(m-1));jumps=[]
  for j,h in enumerate(holes):
   x=h;dist=0
   while True:
    dist+=a[x];x=(x+1)%52
    if x==holes[(j+1)%m]:break
   jumps.append(dist)
  assert sum(jumps)==179;d=0;enc='';dec=''
  for i,(p,cc) in enumerate(zip(plain,c['ciphertext'])):enc+=chr(97+(ord(p)-97+d-off)%26);dec+=chr(97+(ord(cc)-97+off-d)%26);d=(d+jumps[i%m])%26
  assert len(plain)==385 and enc==c['ciphertext'] and dec==plain;full=sum(weights[n]*sum(models[n].get(plain[i:i+n],-n) for i in range(385-n+1)) for n in range(2,6));assert abs(full-float(score))<.04;count+=1;row={'m':m,'offset':off,'anchor':anchor,'rank':int(rank),'score':full,'holes':holes,'plaintext':plain}
  if 'plaintext' in c:row['exact_plaintext']=plain==c['plaintext']
  rows.append(row)
 rows.sort(key=lambda z:z['score'],reverse=True);summary={'label':c['label'],'retained_count':len(rows),'best_candidates':rows[:20]}
 if 'plaintext' in c:summary.update(exact_plaintext_ranks=[i for i,z in enumerate(rows) if z['exact_plaintext']],matching_letters_best_generic=sum(a==v for a,v in zip(rows[0]['plaintext'],c['plaintext'])) if rows else 0)
 results.append(summary)
(b/'checks.json').write_text(json.dumps({'complete_candidate_reencryptions_and_rescores':count,'cases':results},indent=2)+'\n')
for z in results:print(z['label'],z['retained_count'],z.get('exact_plaintext_ranks'),z['best_candidates'][0]['plaintext'] if z['best_candidates'] else '')
