import run_pair as r
from pathlib import Path
import json,hashlib,concurrent.futures

def task(args):
 label,cts,phase=args
 v=r.pipeline(label,cts,phase)
 return r.refine5(v)
if __name__=='__main__':
 sources={};cts={}
 for label in ['literal','preferred']:
  texts=[];sources[label]=[]
  for n in [350,351]:
   p=r.R/f'ciphers/hcp-{n}/work/transcription.txt' if label=='literal' else r.R/f'batches/source-variants-350-351/{n}-source-preferred.txt'
   raw=p.read_text();text=''.join(c.lower() for c in raw if c.isascii() and c.isalpha());assert len(text)==385;(r.P/f'{label}-{n}.txt').write_text(text+'\n');texts.append(text);sources[label].append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'length':len(text)})
  cts[label]=texts
 (r.P/'input-provenance.json').write_text(json.dumps(sources,indent=2));(r.P/'variant-manifest.json').write_text((r.R/'batches/source-variants-350-351/manifest.json').read_text());out=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=3)as pool:
  fs=[pool.submit(task,(label,texts,phase))for label,texts in cts.items()for phase in range(17)]
  for f in concurrent.futures.as_completed(fs):
   out.append(f.result());(r.P/'target-results5.json').write_text(json.dumps(sorted(out,key=lambda x:x['language_score'],reverse=True),indent=2))
