from pathlib import Path
import json
b=Path(__file__).resolve().parent
exec(compile((b/'run.py').read_text().split('# Run existing')[0],str(b/'run.py'),'exec'))
rows=json.loads((b/'exact-results-cap4.json').read_text());original=[r for r in map(json.loads,(old/'actual-results.jsonl').read_text().splitlines())if r['status']=='unknown']
for i,r in enumerate(rows):
 if r['status']!='bounded-out':continue
 row=original[i];new=fit(row['p'],row['c'],row['press_indices'],row['m']);new.update(case_id=row['case_id'],original_status='unknown',original_timeout_ms=row['timeout_ms'],previous_vector_status='bounded-out',explicitly_extended_bound='GF2<=5,GF13<=4,total<=913952');rows[i]=new;print(new['case_id'],new['status'],new.get('enumerated'),new.get('seconds'),flush=True)
(b/'exact-results.json').write_text(json.dumps(rows,indent=2)+'\n')
