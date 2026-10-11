from optimize_engine import solve
from pathlib import Path
import json
P=Path(__file__).parent
controls=json.loads(Path('batches/r364-key-search-sol61/results.json').read_text());rows=[]
for c in controls:
 r=solve(c['plaintext'],c['ciphertext'],c['widths'],seconds=60,errors=len(c['plaintext']),hint_keys=c['recovered_keys'],optimize_errors=True);r.update(stage='hinted-CP-LNS-control',seed=c['seed'],initial_blind_match=c['matching_positions'],hint_keys=c['recovered_keys'],hint_source='prior independent blind Hungarian run, no planted key',plaintext=c['plaintext'],ciphertext=c['ciphertext']);rows.append(r);(P/'optimize-controls.json').write_text(json.dumps(rows,indent=2));print(c['seed'],r['status'],r.get('objective'),r.get('exact_wholetext'),flush=True)
