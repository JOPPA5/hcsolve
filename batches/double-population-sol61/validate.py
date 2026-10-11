import json,re,hashlib
from pathlib import Path
w=Path(__file__).resolve().parent;root=w.parents[1]
controls=json.loads((root/'ciphers/hcp-399/work/idp/controls.json').read_text());results=[]
def encode(p,k):return ''.join(p[c::len(k)] for c in k)
for c in controls:
 if len(c['plaintext'])!=240:continue
 name=c['label'].split('-')[0];ct=(root/f'ciphers/hcp-399/work/idp/{name}-240.txt').read_text().strip()
 for mode in ('landscape','blind','late'):
  logfile=w/f'{name}-{mode}.log'
  if not logfile.exists():continue
  match=re.search(r'^RESULT score=([\d.-]+) inner=([0-9,]+) outer=([0-9,]+) ([a-z]+)$',logfile.read_text(),re.M)
  if not match:continue
  sc=float(match[1]);inner=[int(v) for v in match[2].split(',') if v];outer=[int(v) for v in match[3].split(',') if v];p=match[4]
  assert sorted(inner)==list(range(20)) and sorted(outer)==list(range(17))
  assert encode(encode(p,inner),outer)==ct
  exact=p==c['plaintext'];keys=[inner,outer]==c['keys']
  if mode=='landscape':assert exact and keys
  results.append({'control':c['label'],'mode':mode,'score':sc,'positions_correct':sum(a==b for a,b in zip(p,c['plaintext'])),'total':240,'full_plaintext_exact':exact,'both_keys_exact':keys,'independent_reencryption':'PASS','known_outer_supplied':mode=='landscape'})
(w/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
