from pathlib import Path
import json
from pysat_run import run
b=Path(__file__).resolve().parent
fixture=json.loads((b/'audit.json').read_text());results=[]
for name in ['cadical300','glucose42']:
    for case in fixture['cases']:
        result=run(case['plaintext'],case['ciphertext'],name=name,budget=10000 if name=='cadical300' else 2,w=3,v=4,reverse=True)
        got=any(row['status']=='sat' for row in result['rows'])
        assert got==case['expected_sat'] and not any(row['status']=='unknown' for row in result['rows'])
        if got:
            keys=next(row['keys'] for row in result['rows'] if row['status']=='sat')
            p=case['plaintext']
            for key in keys:
                rows=[list(p[i:i+len(key)]) for i in range(0,len(p),len(key))]
                p=''.join(row[col] for col in key for row in rows if col<len(row))
            assert [(x,y) for x,y in zip(p,case['ciphertext']) if x!=y]==[('n','u')]
        results.append(result)
(b/'pysat-audit.json').write_text(json.dumps(dict(exhaustive_key_triples=72,cases=results),indent=2)+'\n')
print('48 CNF/backend cases PASS')
