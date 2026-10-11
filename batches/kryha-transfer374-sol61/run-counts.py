from pathlib import Path
import json,subprocess
b=Path(__file__).resolve().parent;r=b.parents[1];key=json.load(open(b/'transferred-key.json'));P=key['P'];O=key['O'];coord=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'))['unwrapped_effective_coordinates'];edges=key['adjacent_distances'];invP={v:i for i,v in enumerate(P)};invO={v:i for i,v in enumerate(O)}
def verify(ct,row,m):
 score,a,d,hs,pt=row;hs=[int(x)for x in hs.split(',')if x];assert len(hs)==m and len(set(hs))==m and sum((hs[(i+1)%m]-hs[i])%52 for i in range(m))==52
 dec=''
 for i,c in enumerate(ct):
  j=i%m;dist=coord[hs[j]]-coord[hs[0]]+179*(hs[j]<hs[0])+179*(i//m);dec+=chr(97+P[(O[ord(c)-97]-int(d)-dist)%26])
 assert dec==pt;back='';cur=int(d)
 for i,c in enumerate(pt):
  back+=chr(97+invO[(invP[ord(c)-97]+cur)%26]);h=hs[i%m];nxt=hs[(i+1)%m]
  while h!=nxt:cur+=edges[h];h=(h+1)%52
 assert back==ct
 return dict(score=float(score),holes=hs,initial_displacement=int(d),plaintext=pt,whole_reencryption_exact=True,P=P,O=O)
controls=json.load(open(b/'count-controls.json'));checks=[]
for c in controls:
 v=verify(c['ciphertext'],c['best'],c['m']);v.update(m=c['m'],whole_exact=c['whole_exact']);checks.append(v)
(b/'count-control-verification.json').write_text(json.dumps(checks,indent=2)+'\n');winners=[]
for m in [c['m']for c in controls if c['whole_exact']]:
 for t in json.load(open(b/'target-winners.json')):
  label=t['label'];inp=b/(label+'.txt');out=b/(label+f'-m{m}-beam128.txt');subprocess.run([str(b/'beam'),str(b/'known-rings-coordinates.txt'),str(inp),str(m),'128',str(r),str(out)],check=True);rows=sorted((x.split()for x in out.read_text().splitlines()),key=lambda x:float(x[0]),reverse=True);ct=inp.read_text().strip();top=[verify(ct,q,m)for q in rows[:20]];(b/(label+f'-m{m}-keys.json')).write_text(json.dumps(dict(m=m,label=label,ciphertext=ct,candidates=top),indent=2)+'\n');winners.append(dict(m=m,label=label,**top[0]));print(m,label,top[0]['plaintext'],flush=True)
(b/'target-count-winners.json').write_text(json.dumps(winners,indent=2)+'\n')
