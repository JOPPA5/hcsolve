from pathlib import Path
import subprocess,json
p=Path(__file__).resolve().parent
root=p.parents[3]
sk=root/'batches/scoring-sol61';de=sk/'german'
jobs=[('commercial-sk40',p/'commercial-sk40-cipher.txt'),('commercial-de40',p/'commercial-de40-cipher.txt'),('commercial-target-o40',p.parent/'target-o-40.txt'),('commercial-target-d40',p.parent/'target-d-40.txt')]
for name,inp in jobs:
 with (p/(name+'-results.txt')).open('w') as f,(p/(name+'-progress.txt')).open('w') as err:
  subprocess.run([str(p/'commercial'),str(sk),str(de),str(inp)],stdout=f,stderr=err,check=True)
 print(name,'complete',flush=True)
controls=json.loads((p/'commercial-controls.json').read_text())['heldout_controls']
checks=[]
for c in controls:
 lines=(p/(c['name']+'-results.txt')).read_text().splitlines()[1:]
 tops={lang:next(l for l in lines if l.startswith(lang+' ')) for lang in ['sk','de']}
 correct=next((i+1 for i,l in enumerate([l for l in lines if l.startswith(c['name'].split('-')[-1][:2]+' ')]) if l.split()[-1]==c['plain']),None)
 checks.append({'name':c['name'],'expected':c['plain'],'matching_language_rank':correct,'top':tops,'whole_plain_exact_top1':correct==1})
(p/'commercial-search-control-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2),flush=True)
