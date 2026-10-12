from pathlib import Path
from collections import Counter
import json,hashlib
b=Path(__file__).resolve().parent;records=[]
for file in sorted(b.glob('*.json')):
    data=json.loads(file.read_text())
    if isinstance(data,dict) and 'rows' in data and 'plaintext' in data:
        records.append(dict(file=file.name,cases=len(data['rows']),statuses=dict(Counter(r['status'] for r in data['rows'])),legal_n=21,complete_rank_sweep=len(data['rows'])==21,positive_witness=any(r['status']=='sat' for r in data['rows'])))
sources=list(Path('ciphers/hcp-369/source').glob('*'))+[Path('batches/repeat369-365-sol61/closest-inventory.json')]
summary=dict(scope='conditional widths22/22/21, common alignment, two public365 preparations, omission WITPK, one predicted N to literal U; no target key yet',records=records,source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources if p.is_file()},implementation_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in b.glob('*.py')})
(b/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
for row in records:print(row['file'],row['cases'],row['statuses'])
