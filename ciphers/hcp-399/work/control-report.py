from pathlib import Path
import json
p=Path(__file__).parent
report=[]
for name in ['240-1stage','245-1stage','245-1stage-extended','240-2stage','240-3stage']:
 lines=(p/f'control-{name}-result.txt').read_text().splitlines();truth=(p/f'control-{name[:3]}-plain.txt').read_text();guess=lines[-1];correct=sum(a==b for a,b in zip(truth,guess))
 report.append({'control':name,'score':float(lines[0].split()[1]),'matching_positions':correct,'length':len(truth),'exact_plaintext':guess==truth,'budget':{'restarts':200 if 'extended' in name else 30,'steps':100000 if 'extended' in name else 30000}})
print(json.dumps(report,indent=2))
