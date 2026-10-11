from pathlib import Path
import subprocess,json
p=Path(__file__).parent
s=''.join(c for c in (p/'transcription-v2.txt').read_text() if c.isalpha());(p/'v2-target-all.txt').write_text(s)
for i in range(len(s)//5):(p/f'v2-target-drop-{i+1:02}.txt').write_text(s[:5*i]+s[5*i+5:])
positions=[0]+list(map(int,(p/'indicator-positions-v2.txt').read_text().split()))
results=[]
with (p/'sweep-v2-results.jsonl').open('w') as f:
 for pos in positions:
  target=p/('v2-target-all.txt' if pos==0 else f'v2-target-drop-{pos:02}.txt')
  for width in range(16,23):
   out=subprocess.check_output([str(p/'multistage'),str(p/'quadgrams.tsv'),str(target),'10','10000',str(width),'0'],text=True).splitlines()
   item={'drop_group':pos,'width':width,'score':float(out[0].split()[1]),'key':[int(x) for x in out[1].split(',') if x],'candidate':out[2]}
   f.write(json.dumps(item)+'\n');f.flush();results.append(item)
  print('completed group',pos,flush=True)
(p/'sweep-v2-top.json').write_text(json.dumps(sorted(results,key=lambda x:x['score'],reverse=True)[:10],indent=2))
