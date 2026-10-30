#!/usr/bin/env python3
"""Finite dictionary constraints on manual geometry; candidates are NOT readings."""
import collections,hashlib,itertools,json,math
from pathlib import Path
P=Path(__file__).resolve().parent; ROOT=P.parents[2]
D=ROOT/'batches/scoring-sol61/german/words.tsv'
def pattern(seq):
 m={};return tuple(m.setdefault(x,len(m)) for x in seq)
def compatible(a,b):
 return all(s not in a or a[s]==v for s,v in b.items()) and all(v not in a.values() or a.get(s)==v for s,v in b.items())
def candidates(variants,index):
 out=[]
 for symbols in variants:
  for word,freq in index.get((len(symbols),pattern(symbols)),[]):
   out.append((word,dict(zip(symbols,word)),symbols,freq))
 return out

def main():
 t=json.loads((P/'transcript.json').read_text());index=collections.defaultdict(list)
 for line in D.read_text().splitlines():
  w,f=line.split('\t')
  if len(w) in {3,4,5,8}: index[len(w),pattern(w)].append((w,int(f)))
 variants=[]
 for r in t['rows']:
  options=[g['readings'] for g in r['glyphs'] if not g.get('canceled')]
  variants.append(sorted(set(itertools.product(*options))))
 # Train on groups 1,2,4,6; groups 3,5 are held out. No held-out word changes key.
 # This tests only word-separator + canceled-deletion + bijective MASC hypotheses.
 report={'manual_transcript_sha256':hashlib.sha256((P/'transcript.json').read_bytes()).hexdigest(), 'dictionary':str(D.relative_to(ROOT)), 'dictionary_sha256':hashlib.sha256(D.read_bytes()).hexdigest(),
  'scope':'All dictionary entries with lengths 3,4,5,8; fixed manual alternatives, canceled position omitted conditionally; no arbitrary transcription repair.',
  'training_groups':[1,2,4,6], 'heldout_groups':[3,5], 'directions':{}}
 for direction in ('forward','reverse'):
  vs=variants if direction=='forward' else [sorted(set(tuple(reversed(x)) for x in v)) for v in variants]
  cs=[candidates(v,index) for v in vs]
  order=[3,5,1,0];n=[0]*5;results=[];complete=0;fullpasses=0;group3passes=0
  look=[]
  for row in cs:
   allids=set(range(len(row))); by=collections.defaultdict(lambda:collections.defaultdict(set));present=collections.defaultdict(set)
   for j,(_,k,_,_) in enumerate(row):
    for sym,ch in k.items():by[sym][ch].add(j);present[sym].add(j)
   look.append((by,{sym:allids-ids for sym,ids in present.items()},allids))
  def filtered(i,key):
   by,missing,allids=look[i];ids=None
   constraints=[by[sym].get(ch,set())|missing[sym] for sym,ch in key.items() if sym in by]
   for allowed in sorted(constraints,key=len):
    ids=allowed.copy() if ids is None else ids&allowed
    if not ids:return []
   return [cs[i][j] for j in (allids if ids is None else ids) if compatible(key,cs[i][j][1])]
  def dfs(depth,key,selected):
   nonlocal complete,fullpasses,group3passes
   n[depth]+=1
   if depth==len(order):
    hold=[]
    for i in [2,4]:
     pred=set(''.join(key.get(s,'?') for s in syms) for syms in vs[i])
     poss=filtered(i,key)
     exact=sorted({w for w,k,syms,f in poss if all(s in key for s in syms)})
     compatible_words=sorted({w for w,k,syms,f in poss})
     hold.append({'group':i+1,'predictions':sorted(pred),'fully_predicted_dictionary_words':exact,'compatible_dictionary_words':compatible_words})
    # No full held-out pass unless every symbol was predicted and word matches.
    complete+=1;fullpasses+=int(all(h['fully_predicted_dictionary_words'] for h in hold));group3passes+=int(bool(hold[0]['fully_predicted_dictionary_words']))
    score=sum(math.log1p(selected[i][3]) for i in order)
    results.append({'training_frequency_score':score,'training':{str(i+1):selected[i][0] for i in order}, 'key':key,'heldout':hold,
      'full_heldout_pass':all(h['fully_predicted_dictionary_words'] for h in hold)})
    results.sort(key=lambda x:-x['training_frequency_score']);del results[25:]
    return
   i=order[depth]
   for item in filtered(i,key):
    if compatible(key,item[1]): dfs(depth+1,key|item[1],selected|{i:item})
  dfs(0,{}, {})
  report['directions'][direction]={'word_candidate_counts':list(map(len,cs)), 'training_order':[i+1 for i in order], 'states_by_depth':n,
   'complete_training_assignments':complete,'full_heldout_passes':fullpasses,'group3_fully_predicted_dictionary_passes':group3passes, 'retained':'25 highest summed log1p training word frequencies only; no held-out ranking','results':results}
 # Test the bijection guard itself and held-out prediction on an independent planted example.
 control=['ich','dabei','dich','heute','sehr','vermisst']; alpha='abcdefghijklmnopqrstuvwxyz'; cipher=alpha[7:]+alpha[:7];enc=dict(zip(alpha,cipher))
 key={enc[c]:c for i in [0,1,3,5] for c in control[i]}
 checks={'consistent_pair_accepted':compatible({'a':'x'},{'b':'y'}),
 'same_cipher_conflict_rejected':not compatible({'a':'x'},{'a':'y'}),
 'same_plain_conflict_rejected':not compatible({'a':'x'},{'b':'x'}),
 'independent_control_withheld_dich': ''.join(key.get(enc[c],'?') for c in control[2]),
 'independent_control_withheld_sehr': ''.join(key.get(enc[c],'?') for c in control[4])}
 assert all(checks[k] for k in ['consistent_pair_accepted','same_cipher_conflict_rejected','same_plain_conflict_rejected'])
 assert checks['independent_control_withheld_dich']=='dich' and checks['independent_control_withheld_sehr']=='sehr'
 report['controls']=checks
 (P/'masc-constraints.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({d:{k:v for k,v in r.items() if k!='results'} for d,r in report['directions'].items()},indent=2));print(checks)
if __name__=='__main__':main()
