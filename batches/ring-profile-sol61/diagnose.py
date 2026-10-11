from pathlib import Path
from collections import Counter
import math,json,hashlib
P=Path(__file__).resolve().parent;R=P.parents[1];M=R/'ciphers/hcp-350/work';steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9];logs=sorted(float(line.split()[1]) for line in (M/'ring-unigrams.tsv').read_text().splitlines());assert len(logs)==26;prob=[math.exp(x) for x in logs];assert abs(sum(prob)-1)<1e-9

def histogram(ct,O,phase,sign):
 n=[0]*26;d=0
 for i,c in enumerate(ct):n[(O[ord(c)-97]-d)%26]+=1;d=(d+sign*steps[(phase+i)%17])%26
 return sorted(n)
def metrics(n):
 N=sum(n);ll=sum(x*l for x,l in zip(n,logs));return dict(sorted_assignment_log_likelihood=ll,multinomial_profile_log_likelihood=math.lgamma(N+1)-sum(math.lgamma(x+1) for x in n)+ll,negative_profile_KL=ll-sum(x*math.log(x/N) for x in n if x),negative_hellinger=-sum((math.sqrt(x/N)-math.sqrt(p))**2 for x,p in zip(n,prob)),concentration=sum(x*x for x in n))
def read_candidates(file):
 return [[int(x) for x in line.split()[1].split(',') if x] for line in file.read_text().splitlines()]
sets=[];key=json.loads((M/'ring-control-key.json').read_text());sets.append(dict(label='original385',ciphertext=(M/'ring-control-cipher.txt').read_text().strip(),phase=6,sign=-1,true_output_positions=key['output_positions'],candidate_file=str(M/'ring-ic-control-candidates.txt')))
B=R/'batches/kryha-framing-sol61'
for f in B.glob('control*/phase*/result.json'):
 d=json.loads(f.read_text());k=d['planted'];sets.append(dict(label=d['label'],ciphertext=k['ciphertext'],phase=k['phase'],sign=1,true_output_positions=k['reflected_output_positions'] if k['sign']==-1 else k['output_positions'],candidate_file=str(f.parent/'ic.txt')))
results=[]
for data in sets:
 candidates=read_candidates(Path(data['candidate_file']));rows=[]
 for i,O in enumerate(candidates):
  h=histogram(data['ciphertext'],O,data['phase'],data['sign']);r=dict(candidate_index=i,output_positions=O,histogram=h,**metrics(h));rows.append(r)
 h=histogram(data['ciphertext'],data['true_output_positions'],data['phase'],data['sign']);true=metrics(h);ranks={name:1+sum(r[name]>value+1e-9 for r in rows) for name,value in true.items()};report=dict(**data,length=len(data['ciphertext']),true_histogram=h,true_metrics=true,true_rank_with_true_added=ranks,candidate_count=len(rows),ranking_uses_frozen_TRAIN_only=True)
 for name in ['sorted_assignment_log_likelihood','multinomial_profile_log_likelihood','negative_profile_KL','negative_hellinger']:
  ranked=sorted(rows,key=lambda r:r[name],reverse=True);report[name+'_top_indices']=[x['candidate_index'] for x in ranked[:20]]
  report[name+'_top_key_matches_diagnostic']=[max(sum((a+off)%26==b for a,b in zip(x['output_positions'],data['true_output_positions'])) for off in range(26)) for x in ranked[:20]]
 report['rows']=rows;results.append(report);print(data['label'],len(rows),ranks,flush=True)
(P/'diagnostic.json').write_text(json.dumps(dict(frozen_training_unigram_sha256=hashlib.sha256((M/'ring-unigrams.tsv').read_bytes()).hexdigest(),probabilities_sorted=prob,metric_note='Raw rearrangement LL optimizes unknown-letter assignment exactly but excludes histogram combinatorial factor. Profile multinomial includes N! divided by product(count!), avoiding rewarding concentration alone. KL and Hellinger use only frozenTRAIN distribution.',control_truth_diagnostic_only=True,results=results),indent=2)+'\n')
