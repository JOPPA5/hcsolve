from pathlib import Path
import json
p=Path(__file__).parent;report=[]
for name,period in [('control-vig',9),('control-vig15',15)]:
 line=next(l for l in (p/(name+'-results.txt')).read_text().splitlines() if l.split()[0]==str(period));pt=line.split()[3];truth=(p/'control-vig-plain.txt').read_text()
 report.append({'control':name,'period':period,'matching_known_positions':sum(a==b for a,b in zip(pt,truth) if a!='?'),'known_positions':sum(a!='?' for a in pt),'key_recovered':list(map(int,line.split()[2].strip(',').split(',')))==list(map(int,(p/(name+'-key.txt')).read_text().split()))})
print(json.dumps(report,indent=2))
