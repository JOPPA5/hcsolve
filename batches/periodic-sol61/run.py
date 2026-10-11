"""Run three frozen language models; deterministic seed per process; no true keys."""
from pathlib import Path
import subprocess,sys
b=Path(__file__).resolve().parent;root=b.parents[1]
kind=sys.argv[1] if len(sys.argv)>1 else 'controls'
assert kind in ('controls','targets')
ps=[]
for lang,model in [('sk','batches/scoring-sol61'),('de','batches/scoring-sol61/german'),('cs','batches/czech-scoring')]:
 case=b/f'controls-{lang}.tsv' if kind=='controls' else b/'targets.tsv'
 prefix='control' if kind=='controls' else 'target'
 output=open(b/f'{prefix}-results-{lang}.tsv','w');progress=open(b/f'{prefix}-progress-{lang}.log','w')
 ps.append((lang,subprocess.Popen([str(b/'periodic'),str(root/model),str(b/f'{lang}-frequencies.tsv'),str(case)],stdout=output,stderr=progress)))
for lang,p in ps:print(lang,p.wait(),flush=True)
