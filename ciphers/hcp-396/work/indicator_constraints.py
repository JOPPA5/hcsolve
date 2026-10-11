from pathlib import Path
import json
p=Path(__file__).resolve().parent
groups=(p/'transcription.txt').read_text().split()
def code(n):return ''.join(str((n+j)%10) for j in range(5)) if n<10 else str(n)+'0'+str(n+1)
def feasible(s,d):
 mapping={}
 for c,v in zip(s,d):
  if c in mapping and mapping[c]!=v:return False
  mapping[c]=v
 return max([list(mapping.values()).count(v) for v in set(mapping.values())])<=3
table={str(i):chr(97+i) for i in range(10)}
for n in range(1,23):
 group=''.join(table[d] for d in code(n))
 assert feasible(group,code(n))
assert not feasible('abcad','12345')
out=[]
for reading in ('c','o'):
 gs=groups.copy();gs[6]=reading+gs[6][1:]
 for i,g in enumerate(gs):
  out.append(dict(reading=reading,position=i+1,group=g,possible_alignment=[n for n in range(1,23) if feasible(g,code(n))]))
(p/'indicator-constraints.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
