from pathlib import Path
import json,subprocess,itertools,hashlib
b=Path(__file__).resolve().parent;r=b.parents[1];exe=b/'beam';cfg=b/'known-rings-coordinates.txt';key=json.load(open(b/'transferred-key.json'));P=key['P'];O=key['O'];edges=key['adjacent_distances']
def check(ct,q):
 score,a,d,hs,pt=q;holes=[int(x)for x in hs.split(',')if x];a=int(a);d=int(d);assert len(set(holes))==23 and holes[0]==a
 assert sum((holes[(i+1)%23]-holes[i])%52 for i in range(23))==52
 invP={v:i for i,v in enumerate(P)};invO={v:i for i,v in enumerate(O)};out='';cur=d
 for i,c in enumerate(pt):
  out+=chr(97+invO[(invP[ord(c)-97]+cur)%26]);h=holes[i%23];nxt=holes[(i+1)%23]
  while h!=nxt:cur+=edges[h];h=(h+1)%52
 assert out==ct
 return dict(score=float(score),holes=holes,initial_displacement=d,plaintext=pt,reencryption_exact=True,P=P,O=O)
def rows(file):return sorted((x.split()for x in file.read_text().splitlines()),key=lambda x:float(x[0]),reverse=True)
controls=json.load(open(b/'controls.json'));checks=[]
for c in controls:
 qs=rows(b/(c['label']+'-beam128.txt'));v=check(c['ciphertext'],qs[0]);v['label']=c['label'];v['whole_exact']=v['plaintext']==c['plaintext'];v['mask_exact']=v['holes']==c['holes'];v['offset_exact']=v['initial_displacement']==c['initial_displacement'];assert v['whole_exact'];checks.append(v)
(b/'control-verification.json').write_text(json.dumps(checks,indent=2)+'\n')
original=''.join((r/'ciphers/hcp-374/work/transcription.txt').read_text().split());assert len(original)==85
manifest=[];winners=[]
for g,q,v in itertools.product([False,True],repeat=3):
 ct=list(original)
 if g:ct[8]='g'
 if q:ct[24]='q'
 if v:ct[59]='v'
 ct=''.join(ct);label=f'target-G{int(g)}-Q{int(q)}-V{int(v)}';inp=b/(label+'.txt');inp.write_text(ct+'\n');out=b/(label+'-beam128.txt');subprocess.run([str(exe),str(cfg),str(inp),'23','128',str(r),str(out)],check=True)
 qs=rows(out);top=[check(ct,z)for z in qs[:20]];record=dict(label=label,ciphertext=ct,changes=[x for x,yes in [('group2 CRTCS→CRTGS',g),('group5 SPQHO→SPQHQ',q),('group12 TLIJY→TLIJV',v)]if yes],candidates=top);(b/(label+'-keys.json')).write_text(json.dumps(record,indent=2)+'\n');winners.append(dict(label=label,**top[0]));manifest.append(dict(label=label,changes=record['changes']))
(b/'target-winners.json').write_text(json.dumps(winners,indent=2)+'\n');(b/'source-variants.json').write_text(json.dumps(dict(original_sha256=hashlib.sha256((r/'ciphers/hcp-374/work/transcription.txt').read_bytes()).hexdigest(),image_sha256=hashlib.sha256((r/'ciphers/hcp-374/source/cryptogram.jpg').read_bytes()).hexdigest(),pixel_view='source-body-crop.jpg: group5 lastletter descender supportsQ;group12 supportsV;group2 watermark ambiguity C/G retained',variants=manifest),indent=2)+'\n')
for z in winners:print(z['label'],z['score'],z['plaintext'])
