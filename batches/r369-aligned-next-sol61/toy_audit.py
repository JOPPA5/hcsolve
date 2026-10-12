from pathlib import Path
import importlib.util,itertools,json
B=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('aligned',B/'engine.py');e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
def independent_enc(s,k):
 out=[]
 for c in k:
  out.extend(s[r*len(k)+c] for r in range((len(s)+len(k)-1)//len(k)) if r*len(k)+c<len(s))
 return ''.join(out)
p='naxnunu';widths=[2,3,4];records=[]
for mode in ['common_unknown','progressive_unknown']:
 legal=[]
 for keys in itertools.product(*(list(itertools.permutations(range(w))) for w in widths)):
  ranks=[k.index(0)+1 for k in keys]
  if (len(set(ranks))==1 if mode=='common_unknown' else ranks==[ranks[0]+j for j in range(3)]):
   c=p
   for k in keys:c=independent_enc(c,k)
   legal.append((keys,c))
 samples=[legal[0][1],legal[-1][1],legal[0][1].replace('n','u',1),'xxxxxxx','anuxnnu','uuuuuuu']
 for c in samples:
  matches=[keys for keys,pred in legal if all(a==b or (a=='n' and b=='u') for a,b in zip(pred,c)) and sum(a!=b for a,b in zip(pred,c))<=1]
  r=e.solve(p,c,widths,seconds=5,errors=1,alignments=mode)
  sat=r['status'] in ['OPTIMAL','FEASIBLE'];assert r['status']!='UNKNOWN';assert sat==bool(matches),(mode,c,r,matches)
  if sat:
   pred=p
   for k in r['keys']:pred=independent_enc(pred,k)
   assert pred==r['predicted_ciphertext']
  records.append(dict(mode=mode,ciphertext=c,enumerated_legal_keys=len(legal),enumerated_witnesses=len(matches),cp=r))
(B/'toy-audit.json').write_text(json.dumps(records,indent=2)+'\n');print('12 direct-enumeration cases agree',flush=True)
