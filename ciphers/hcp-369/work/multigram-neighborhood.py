from pathlib import Path
import subprocess,json
p=Path(__file__).parent
models={};floor={}
for n in (3,4,5):
 lines=Path(f'batches/scoring-sol61/frequency/model{n}.tsv').read_text().splitlines();floor[n]=float(lines[0].split()[1]);models[n]={a:float(b) for a,b in (r.split() for r in lines[1:])}
def score(s):return sum(weight*sum(models[n].get(s[i:i+n],floor[n]) for i in range(len(s)-n+1)) for n,weight in ((3,.15),(4,.4),(5,.8)))
def neighborhood(ct,out):
 key=out.split()[-2];assert len(key)==26 and len(set(key))==26
 unique={}
 for a in range(26):
  for b in range(a,26):
   k=list(key);k[a],k[b]=k[b],k[a];pt=''.join(k[ord(c)-97] for c in ct)
   if pt not in unique:unique[pt]={'score':score(pt),'key':''.join(k),'plaintext':pt,'swap':(a,b)}
 return sorted(unique.values(),key=lambda r:r['score'],reverse=True)
reports=[]
for r in json.loads((p/'multigram-masc-controls.json').read_text()):
 i=r['control'];out=(p/f'multigram-masc-control{i}-result.txt').read_text();candidates=neighborhood(r['cipher'],out);report={'control':i,'candidate_count':len(candidates),'exact_expected_in_retained_set':any(x['plaintext']==r['plain'] for x in candidates),'expected_rank':next((j+1 for j,x in enumerate(candidates) if x['plaintext']==r['plain']),None),'candidates':candidates};reports.append(report);print('control',i,report['exact_expected_in_retained_set'],report['expected_rank'],flush=True)
(p/'multigram-neighborhood-controls.json').write_text(json.dumps(reports,indent=2)+'\n');assert all(r['exact_expected_in_retained_set'] for r in reports)
ct=''.join((p/'transcription.txt').read_text().split())
for rev in (False,True):
 s=ct[::-1] if rev else ct;src=p/f'multigram-neighborhood-target-reverse{rev}.txt';src.write_text(s+'\n');out=subprocess.check_output([str(p/'mono-multigram'),'batches/scoring-sol61/frequency',str(src),'40'],text=True,stderr=(p/f'multigram-neighborhood-target-reverse{rev}-progress.txt').open('w'));(p/f'multigram-neighborhood-target-reverse{rev}-result.txt').write_text(out);candidates=neighborhood(s,out);(p/f'multigram-neighborhood-target-reverse{rev}.json').write_text(json.dumps(candidates,indent=2)+'\n');print('target',rev,'top',candidates[0],flush=True)
