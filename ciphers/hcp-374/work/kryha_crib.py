"""Conditional sliding-crib test, original 17-step Kryha; no recovered text assumed."""
from pathlib import Path
import random,json,collections
p=Path(__file__).parent
steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9]
def shifts(n,phase,sign):
 d=0;v=[]
 for i in range(n):v.append(d);d=(d+sign*steps[(i+phase)%17])%26
 return v
def consistent(plain,cipher,d):
 adj=collections.defaultdict(list)
 for a,b,r in zip(plain,cipher,d):
  a=ord(a)-97;b=26+ord(b)-97
  adj[a].append((b,r));adj[b].append((a,-r))
 vals={};components=[]
 for a in adj:
  if a in vals:continue
  vals[a]=0;queue=[a];comp=[]
  while queue:
   u=queue.pop();comp.append(u)
   for v,delta in adj[u]:
    expect=(vals[u]+delta)%26
    if v in vals:
     if vals[v]!=expect:return None
    else:vals[v]=expect;queue.append(v)
  for side in (0,1):
   positions=[vals[x] for x in comp if x//26==side]
   if len(positions)!=len(set(positions)):return None
  components.append(comp)
 return {'relative_positions':vals,'components':components}
# Independent planted 85-letter control and sliding 43-letter crib.
plain='prosimopakujtepatnastposlednychskupinvashotelegramuosemjednasedemdvaxspravunemoznodekodovat'
plain=plain[:85];rng=random.Random(37461);I=list(range(26));O=list(range(26));rng.shuffle(I);rng.shuffle(O);phase=8;sign=-1;d=shifts(len(plain),phase,sign);inv={v:chr(97+i) for i,v in enumerate(O)}
control=''.join(inv[(I[ord(x)-97]+r)%26] for x,r in zip(plain,d));crib='opakujtepatnastposlednychskupinvashotelegramu';off=plain.index(crib)
assert consistent(crib,control[off:off+len(crib)],d[off:off+len(crib)]) is not None
# Countercheck a deliberately impossible same plaintext/cipher pair with unequal shifts.
assert consistent('aa','bb',[0,1]) is None
ct=''.join((p/'transcription.txt').read_text().split()).lower()
cribs=set()
for verb in ('opakujte','zopakujte','opakovat','opakovanie'):
 for count in ('patnast','jednapat','jedenpat','jednapaet'):
  for suffix in ('poslednychskupin','poslednychskupinvashotelegramu','poslednychskupintelegramu','skupinposlednehotelegramu'):
   cribs.add(verb+count+suffix)
  for prefix in ('poslednych',''):
   cribs.add(verb+prefix+count+'skupin')
results=[];tests=0
for crib in sorted(cribs):
 for phase in range(17):
  for sign in (-1,1):
   d=shifts(len(ct),phase,sign)
   for off in range(len(ct)-len(crib)+1):
    tests+=1;res=consistent(crib,ct[off:off+len(crib)],d[off:off+len(crib)])
    if res is not None:results.append({'crib':crib,'offset':off,'phase':phase,'sign':sign,'components':len(res['components'])})
report={'control':{'plain':plain,'cipher':control,'crib':crib,'true_offset':off,'phase':8,'sign':-1,'passed':True},'crib_count':len(cribs),'tests':tests,'survivors':results,'limitation':'Necessary modular constraints only. Surviving components may conflict globally; templates are guesses, original17-step system unconfirmed.'}
# Avoid loop-variable contamination in control evidence.
report['control']['crib']='opakujtepatnastposlednychskupinvashotelegramu';report['control']['true_offset']=6
(p/'kryha-crib-results.json').write_text(json.dumps(report,indent=2)+'\n');print('cribs',len(cribs),'tests',tests,'survivors',len(results));print(collections.Counter(r['crib'] for r in results))
