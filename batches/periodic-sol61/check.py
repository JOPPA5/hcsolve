from pathlib import Path
import json,sys
b=Path(__file__).resolve().parent
source=(b/'prepare.py').read_text();namespace={};exec(source[source.index('def tables('):source.index("assert enc('geheimnis'")],namespace);enc=namespace['enc']
controls={x['label']:x for x in json.loads((b/'controls.json').read_text())};targets={x['label']:x for x in json.loads((b/'targets.json').read_text())};summary=[];count=0
for file in sorted(b.glob('*results-*.tsv')):
 found={}; best={}
 data=file.read_text();data=data[:data.rfind('\n')+1]
 for line in data.splitlines():
  label,mode,t,rank,score,key,plain=line.split('\t');key=list(map(int,key.split(',')));item=controls.get(label) or targets[label]
  assert enc(plain,mode,key)==item['ciphertext'],(file,label,mode,t)
  count+=1;best.setdefault(label,[]).append((float(score),mode,int(t),plain,key))
  if label in controls and plain==item['plaintext']:found.setdefault(label,[]).append({'mode':mode,'period':int(t),'rank':int(rank),'score':float(score)})
 for label,rows in best.items():
  rows.sort(reverse=True);entry={'file':file.name,'label':label,'exact_plaintext_recovered':bool(found.get(label)) if label in controls else None,'exact_hits':found.get(label,[]),'top':rows[:8]};summary.append(entry)
(b/'checks.json').write_text(json.dumps({'independent_reencryptions_passed':count,'cases':summary},indent=2)+'\n')
for x in summary:
 if x['label'] in controls:print(x['label'],x['exact_plaintext_recovered'],x['exact_hits'])
print('Reencryptions',count)
