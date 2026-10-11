from pathlib import Path
import subprocess,json
p=Path(__file__).resolve().parent
exe=p/'amsco'; model=p/'quadgrams.tsv'
def cells(n,w,phase,mode):
 a=[[]for _ in range(w)];at=0;r=0
 while at<n:
  for c in range(w):
   for j in range(1+((phase+c+(r if mode else r*w))%2)):
    if at<n:a[c].append(at);at+=1
  r+=1
 return a
def run(name,ct):
 (p/(name+'.txt')).write_text(ct+'\n');s=subprocess.check_output([str(exe),str(model),str(p/(name+'.txt'))],text=True);(p/(name+'-results.txt')).write_text(s);return s
control=('ministerstvooznamujezevasuspravusmednesdostalipro'+ 'simzasliteodpoved')[:50]
a=cells(50,7,1,1);key=[3,6,1,4,0,5,2];ct=''.join(control[i] for c in key for i in a[c]);r=run('amsco-control',ct)
(p/'amsco-control-plain.txt').write_text(control+'\n');(p/'amsco-control-key.json').write_text(json.dumps(dict(width=7,phase=1,mode=1,key=key)))
print('AMSCO control exact:',any(x.split()[-1]==control for x in r.splitlines()))
groups=(p/'transcription.txt').read_text().split()
for reading in ('c','o'):
 gs=groups.copy();gs[6]=reading+gs[6][1:]
 for omit in range(-1,11):
  ct=''.join(g for i,g in enumerate(gs) if i!=omit);run(f'amsco-{reading}-omit{omit}',ct)
