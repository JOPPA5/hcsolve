from pathlib import Path
from collections import Counter
import json,string
p=Path(__file__).resolve().parent;d=json.loads((p.parents[1]/'batches/constraint-sol61/target-cases.json').read_text());quote=d['template'][:-1];rows=[]
for reading,omit,c,budget in d['cases']:
 # With physical column 0 read first at each stage, first plaintext letter is invariant.
 # Fix output[0] to quote[0], then lower-bound further changes by inventory deficits.
 fixed=c[0]!=quote[0];after=quote[0]+c[1:];bounds={fill:int(fixed)+sum((Counter(quote+fill)-Counter(after)).values())for fill in string.ascii_lowercase};low=min(bounds.values());assert low>budget
 rows.append(dict(reading=reading,quote_initial=quote[0],observed_initial=c[0],budget=budget,minimum_inventory_substitution_lower_bound_given_invariant=low,proved_conditional_unsat=True,filler_bounds=bounds))
(p/'first-alignment-independent-audit.json').write_text(json.dumps(rows,indent=2));print([{k:v for k,v in r.items()if k!='filler_bounds'}for r in rows])
