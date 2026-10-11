"""Conditional R/XQ indicator-table consistency tests; no target plaintext scoring."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[2]
a=(root/'ciphers/hcp-395/work/transcription.txt').read_text().split()
b=(root/'ciphers/hcp-396/work/transcription.txt').read_text().split()
def digits(n):
 return [(n+i)%10 for i in range(5)] if n<10 else [int(x) for x in str(n)+'0'+str(n+1)]
def merge(groups):
 d={}
 for word,n in groups:
  for c,x in zip(word,digits(n)):
   if c in d and d[c]!=x:return None
   d[c]=x
 if any(sum(x==v for x in d.values())>3 for v in range(10)):return None
 return d
# R key length16..22 means alignment numbers1..22 are upper envelope.
possible_a=[[n for n in range(1,23) if merge([(g,n)]) is not None] for g in a]
possible_b=[[n for n in range(1,23) if merge([(g,n)]) is not None] for g in b]
pairs=[]
for ia,ga in enumerate(a,1):
 for ib,gb in enumerate(b,1):
  m=merge([(ga,9),(gb,7)])
  if m is not None:pairs.append({'group395':ia,'word395':ga,'group396':ib,'word396':gb,'partial_table':m})
# If n unknown, report potential pair counts for nominated DWJPM as396 indicator.
nominated=[]
for ia,ga in enumerate(a,1):
 ns=[]
 for na in range(1,23):
  for nb in range(1,23):
   if merge([(ga,na),('dwjpm',nb)]) is not None:ns.append([na,nb])
 nominated.append({'group395':ia,'word395':ga,'compatible_n_pairs':len(ns)})
out={'assumptions':['faithful transcription','both messages use R/XQ encoding as described in2020 paper','same digit-to-letter table where pair tested','no digit has more than3 letter alternatives'],
'header_as_alignment_9_and_7':{'pair_count':len(pairs),'pairs_with_396_group8':[p for p in pairs if p['group396']==8],'same_position_pairs':[p for p in pairs if p['group395']==p['group396']], 'counts_by_396_group':{str(i):sum(p['group396']==i for p in pairs) for i in range(1,len(b)+1)}},
'possible_n_by_group395':[dict(group=i+1,text=g,n=ns) for i,(g,ns) in enumerate(zip(a,possible_a))],
'possible_n_by_group396':[dict(group=i+1,text=g,n=ns) for i,(g,ns) in enumerate(zip(b,possible_b))],
'unknown_alignments_nominated396_group8':nominated}
(root/'batches/analysis-395-396/indicator-constraints.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out['header_as_alignment_9_and_7'],indent=2))
print('396 impossible groups for every n1..22:',[i+1 for i,n in enumerate(possible_b) if not n])
print('395 impossible groups:',[i+1 for i,n in enumerate(possible_a) if not n])

example_columns={1:'xuf',2:'rn',3:'yzw',4:'ed',5:'ba',6:'qci',7:'jop',8:'kg',9:'hvl',0:'smt'}
example_decode={c:k for k,v in example_columns.items() for c in v}
example_results={}
for label,groups in [('395',a),('396',b)]:
 example_results[label]=[{'group':i+1,'text':g,'digits':[example_decode[c] for c in g], 'valid_n':[n for n in range(1,23) if digits(n)==[example_decode[c] for c in g]]} for i,g in enumerate(groups)]
(root/'batches/analysis-395-396/example-table-check.json').write_text(json.dumps({'warning':'1939 manual example table, NOT an established 1944 target key','columns':example_columns,'results':example_results},indent=2)+'\n')
print('Example-table valid indicators:',{k:[z for z in v if z['valid_n']] for k,v in example_results.items()})
