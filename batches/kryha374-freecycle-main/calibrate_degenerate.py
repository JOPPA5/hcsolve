from pathlib import Path
import json,time
from crt_fixed_unused import solve
out=Path(__file__).resolve().parent
cs=json.loads((out/'controls.json').read_text());rs=[]
for j in [0,2]:
 x=cs[j];r=solve(x['p'],x['c'],x['m'],30000,cycle=x['planted_D']);rs.append(dict(control=j,result=r));print(j,r['status'],r.get('seconds'),flush=True);(out/'degenerate-calibration.json').write_text(json.dumps(rs,indent=2)+'\n')
