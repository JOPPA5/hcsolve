from pathlib import Path
import json
b=Path(__file__).resolve().parent;r=b.parents[1];geometry=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));a=geometry['adjacent_distances'];models={};weights={2:.1,3:.15,4:.4,5:.8}
for n in range(2,6):path=b/f'model{n}.tsv' if n<4 else r/f'ciphers/hcp-350/work/ring-{n}grams.tsv';models[n]={s:float(v) for s,v in (line.split() for line in path.read_text().splitlines())}
records=[]
for c in json.load(open(b/'controls.json')):
 P=c['input_slots'];O=c['output_positions'];ct=c['ciphertext'];ipos={v:i for i,v in enumerate(P)};opos={v:i for i,v in enumerate(O)};rows=[];data=(b/c['label']/'known-beam.tsv').read_text();data=data[:data.rfind('\n')+1]
 for line in data.splitlines():
  anchor,rank,score,key,plain=line.split('\t');holes=list(map(int,key.split(',')));assert len(set(holes))==len(holes)==c['m'];assert holes[0]==int(anchor);assert all((holes[i+1]-holes[0])%52>(holes[i]-holes[0])%52 for i in range(len(holes)-1));jumps=[]
  for j,h in enumerate(holes):
   x=h;dist=0
   while True:
    dist+=a[x];x=(x+1)%52
    if x==holes[(j+1)%len(holes)]:break
   jumps.append(dist)
  assert sum(jumps)==179;d=0;enc='';dec=''
  for i,(pc,cc) in enumerate(zip(plain,ct)):
   enc+=chr(97+opos[(ipos[ord(pc)-97]+d)%26]);dec+=chr(97+P[(O[ord(cc)-97]-d)%26]);d=(d+jumps[i%len(holes)])%26
  assert enc==ct and dec==plain
  independent=sum(weights[n]*sum(models[n].get(plain[i:i+n],-n) for i in range(len(plain)-n+1)) for n in range(2,6));assert abs(independent-float(score))<.03
  rows.append({'anchor':int(anchor),'rank':int(rank),'score':independent,'holes':holes,'plaintext':plain,'exact_plaintext':plain==c['plaintext'],'physical_mask_exact':set(holes)==set(c['active_holes_zero_based']),'starting_stop_exact':holes[0]==c['starting_hole_zero_based']})
 rows.sort(key=lambda z:z['score'],reverse=True);record={'label':c['label'],'known_rings':True,'m_supplied':c['m'],'mask_and_phase_not_supplied':True,'candidate_count':len(rows),'exact_plaintext_found':any(z['exact_plaintext'] for z in rows),'exact_ranks':[i for i,z in enumerate(rows) if z['exact_plaintext']],'candidates':rows};records.append(record)
(b/'known-results.json').write_text(json.dumps(records,indent=2)+'\n')
for x in records:print(x['label'],x['candidate_count'],x['exact_plaintext_found'],x['exact_ranks'][:8],x['candidates'][0]['plaintext'] if x['candidates'] else '')
