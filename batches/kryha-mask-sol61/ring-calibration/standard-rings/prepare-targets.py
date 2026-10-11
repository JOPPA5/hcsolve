from pathlib import Path
import json,hashlib
b=Path(__file__).resolve().parent;r=b.parents[3];cases=[];audit=json.load(open(r/'batches/source-variants-350-351/manifest.json'))
for n in(350,351):
 for reading,path in [('original',r/f'ciphers/hcp-{n}/work/transcription.txt'),('preferred',r/f'batches/source-variants-350-351/{n}-source-preferred.txt')]:
  ct=''.join(path.read_text().lower().split());assert len(ct)==385 and all('a'<=c<='z' for c in ct)
  if reading=='preferred':assert ct==next(x['source_preferred_alternate'] for x in audit if x['cipher']==n)
  for direction,text in [('forward',ct),('reverse',ct[::-1])]:
   label=f'target{n}-'+('preferred-' if reading=='preferred' else '')+direction;case={'label':label,'cipher':n,'direction':direction,'ciphertext':text,'source':str(path.relative_to(r)),'reading':reading,'removed_symbols':None,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'source_auditor_manifest':'batches/source-variants-350-351/manifest.json' if reading=='preferred' else None};cases.append(case);(b/(label+'.txt')).write_text(text+'\n')
(b/'targets.json').write_text(json.dumps(cases,indent=2)+'\n')
