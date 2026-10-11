from pathlib import Path
import json,hashlib,collections
P=Path(__file__).resolve().parent;R=P.parents[1];M=R/'ciphers/hcp-350/work';steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9]
model={n:{s:float(v) for s,v in (line.split() for line in (M/f'ring-{n}grams.tsv').read_text().splitlines())} for n in [4,5]}
manifest=json.loads((P/'target-manifest.json').read_text());assert all(hashlib.sha256(Path(f).read_bytes()).hexdigest()==h for f,h in manifest['inputs'].items())
out={};errors=[]
for n in [4,5]:
 rows=[json.loads(line) for line in (P/f'target-results{n}.jsonl').read_text().splitlines()];assert len(rows)==68;assert len({(r['label'],r['phase']) for r in rows})==68
 for r in rows:
  ct=(P/r['label']/f"phase{r['phase']}"/'cipher.txt').read_text().strip();d=0;pt=[];I={letter:i for i,letter in enumerate(r['input_slots'])};Oinv={v:c for c,v in enumerate(r['output_positions'])};enc=[]
  assert set(I)==set(Oinv)==set(range(26))
  for i,c in enumerate(ct):
   pt.append(chr(97+r['input_slots'][(r['output_positions'][ord(c)-97]-d)%26]));enc.append(chr(97+Oinv[(I[ord(r['plaintext'][i])-97]+d)%26]));d=(d+steps[(r['phase']+i)%17])%26
  assert ''.join(pt)==r['plaintext'] and ''.join(enc)==ct
  score=sum(model[n].get(r['plaintext'][i:i+n],-n) for i in range(len(ct)-n+1));error=abs(score-r['language_score']);assert error<.04,(n,error);errors.append(error)
 families={}
 for label in sorted({r['label'] for r in rows}):
  group=sorted([r for r in rows if r['label']==label],key=lambda r:r['language_score'],reverse=True);families[label]={'count':len(group),'best_phase':group[0]['phase'],'best_score':group[0]['language_score'],'top3':group[:3]};print(n,label,group[0]['phase'],group[0]['language_score'],group[0]['plaintext'])
 out[str(n)]=families
out.update(independently_verified_finalists=136,score_max_absolute_error=max(errors),source_hashes_unchanged=True,marker_scan={str(n):[f.name for f in (R/f'ciphers/hcp-{n}').iterdir() if f.name=='FINAL' or f.name.startswith(('DONE','REVIEWED'))] for n in [350,351,334]},coherent_solution_claim=False,failure_is_not_exclusion=True)
(P/'target-summary.json').write_text(json.dumps(out,indent=2)+'\n')
