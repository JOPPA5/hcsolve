from pathlib import Path
import subprocess,json
p=Path(__file__).resolve().parent;root=p.parents[3]
checks=[]
controls={x['name']:x for x in json.loads((p/'controls.json').read_text())['heldout_controls']}
for name in ['sk40','de40','target-o40','target-d40']:
 for lang,model in [('sk',root/'batches/scoring-sol61'),('de',root/'batches/scoring-sol61/german')]:
  dest=p/(name+'-'+lang+'-reranked.txt')
  with dest.open('w') as out:subprocess.run([str(p/'rerank'),str(model),str(p/(name+'-results.txt')),lang],stdout=out,check=True)
  lines=dest.read_text().splitlines();print(name,lang,lines[0],flush=True)
  if name in controls and lang==name[:2]:
   expected=controls[name]['plain'];rank=next((i+1 for i,l in enumerate(lines) if l.split()[-1]==expected),None)
   checks.append({'name':name,'rank':rank,'exact_top1':rank==1,'top':lines[0]})
(p/'rerank-control-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
