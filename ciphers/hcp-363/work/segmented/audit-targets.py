from pathlib import Path
import json
p=Path(__file__).resolve().parent
summary=json.loads((p/'target-summary.json').read_text());checks={}
for name,line in summary.items():
 case,width=name.split('-w');w=int(width);parts=line.split();key=[int(x) for x in parts[2].removeprefix('key=').split(',') if x];plain=parts[3]
 if case.startswith('400'):inp=p.parent/f'cipher-{case[-1]}.txt'
 else:inp=p/f'omit-{3 if case.startswith("omit3") else 25}-{case[-1]}.txt'
 ct=inp.read_text().strip();assert len(plain)==len(ct);assert sorted(key)==list(range(w))
 assert ''.join(plain[j::w] for j in key)==ct
 checks[name]={'length':len(ct),'permutation':True,'independent_reencryption':True,'semantic_acceptance':False,'input':str(inp),'score':float(parts[1])}
(p/'target-validation.json').write_text(json.dumps(checks,indent=2)+'\n');print('verified candidate coverage and re-encryption',len(checks),'not semantic decipherment')
