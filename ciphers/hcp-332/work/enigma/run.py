from pathlib import Path
import subprocess,json
p=Path(__file__).resolve().parent
root=p.parents[3]
sk=root/'batches/scoring-sol61';de=sk/'german'
jobs=[('sk40',p/'sk40-cipher.txt'),('de40',p/'de40-cipher.txt'),('target-o40',p.parent/'target-o-40.txt'),('target-d40',p.parent/'target-d-40.txt')]
for name,inp in jobs:
 with (p/(name+'-results.txt')).open('w') as f,(p/(name+'-progress.txt')).open('w') as err:
  subprocess.run([str(p/'search'),str(sk),str(de),str(inp)],stdout=f,stderr=err,check=True)
 print(name,'complete',flush=True)
controls=json.loads((p/'controls.json').read_text())['heldout_controls']
checks=[]
for c in controls:
 lines=(p/(c['name']+'-results.txt')).read_text().splitlines()[1:]
 tops={lang:next(l for l in lines if l.startswith(lang+' ')) for lang in ['sk','de']}
 correct=next((i+1 for i,l in enumerate([l for l in lines if l.startswith(c['name'][:2]+' ')]) if l.split()[-1]==c['plain']),None)
 checks.append({'name':c['name'],'expected':c['plain'],'matching_language_rank':correct,'top':tops,'whole_plain_exact_top1':correct==1})
(p/'search-control-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2),flush=True)
