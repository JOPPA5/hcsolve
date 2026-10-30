#!/usr/bin/env python3
"""Mutating local hash refresh; source/reference pins are verified, never rebaselined."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];W=R/'work';REPO=R.parents[1]
for name,base in [('source-sha256.json',R),('reference-sha256.json',REPO)]:
 for p,h in json.loads((W/name).read_text()).items(): assert hashlib.sha256((base/p).read_bytes()).hexdigest()==h,p
recordpaths=['work/key.json','work/transcription.json','work/transcription.txt','work/literal.txt','work/positions.csv','work/source-controls.json','work/uncertainties.json','work/qa-followup.json']
(W/'record-sha256.json').write_text(json.dumps({p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in recordpaths},indent=2)+'\n')
paths=[R/'SOLUTION.md',R/'NOTES.md']+[p for p in sorted(W.iterdir()) if p.is_file() and p.name!='canonical-sha256.json']
(W/'canonical-sha256.json').write_text(json.dumps({str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},indent=2)+'\n')
print('Sealed',len(paths),'local artifacts.')
