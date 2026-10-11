from pathlib import Path
import json,sys,itertools
b=Path(__file__).resolve().parent;data=json.load(open(sys.argv[1]));lines=(b/sys.argv[2]).read_text().splitlines();projections=(b/sys.argv[3]).read_text().splitlines();out=[]
for k in range(0,len(lines),4):
 ident,score=lines[k].split();p=list(map(int,lines[k+1].split()));v=projections[int(ident)].split()
 for a,bb in [(-1,-1)]+list(itertools.combinations(range(26),2)):
  key=p.copy()
  if a>=0:key[a],key[bb]=key[bb],key[a]
  pts=[''.join(chr(97+key[ord(c)-97]) for c in s) for s in v]
  out.append(dict(profile_rank=int(ident)+1,swap=[a,bb],P=key,plaintexts=pts))
(b/sys.argv[4]).write_text(json.dumps(out,separators=(',',':'))+'\n');print(len(out),'blind key coverage')
