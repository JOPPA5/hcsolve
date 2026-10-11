from pathlib import Path
import json,re
from isomorph_solver import solve_isomorph
p=Path(__file__).resolve().parent;repo=p.parents[1]
a=''.join(re.findall('[a-z]',(repo/'ciphers/hcp-350/work/transcription.txt').read_text().lower()));b=''.join(re.findall('[a-z]',(repo/'ciphers/hcp-351/work/transcription.txt').read_text().lower()));assert len(a)==len(b)==385
windows={'prefix20':list(range(20)),'suffix10':list(range(375,385)),'prefix20_and_suffix10':list(range(20))+list(range(375,385))};rows=[]
for label,positions in list(windows.items()):
 for matched_only in [False,True]:
  ix=[i for i in positions if a[i]==b[i]]if matched_only else positions
  texts=[''.join(t[i]for i in ix)for t in [a,b]];r=solve_isomorph(texts,len(ix));r.update(scope=label,identical_positions_only=matched_only,positions_1based=[i+1 for i in ix],ciphertexts=texts,identical=sum(a[i]==b[i]for i in ix),unequal=sum(a[i]!=b[i]for i in ix));rows.append(r)
(p/'350-351-framing-conditional.json').write_text(json.dumps(rows,indent=2));print([{k:r[k]for k in ['scope','identical_positions_only','identical','unequal','nullity','status']}for r in rows])
# Read metadata only for locally acquired ciphers; no portal fetch or solution read.
metadata=[]
for f in sorted((repo/'ciphers').glob('hcp-*/source/metadata.md')):
 text=f.read_text();date=next((line.split(':',1)[1].strip()for line in text.splitlines()if line.startswith('Date:')),None);sender=next((line.split(':',1)[1].strip()for line in text.splitlines()if line.startswith('Sender:')),None);recipient=next((line.split(':',1)[1].strip()for line in text.splitlines()if line.startswith('Recipient:')),None);metadata.append(dict(cipher=f.parents[1].name,date=date,sender=sender,recipient=recipient))
(p/'local-metadata-depth-audit.json').write_text(json.dumps(metadata,indent=2));print(metadata)
