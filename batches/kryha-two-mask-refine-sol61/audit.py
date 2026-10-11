from pathlib import Path
import json,math,unicodedata,hashlib
from collections import Counter
B=Path(__file__).resolve().parent;R=B.parents[1];S=R/'batches/kryha-two-mask-language-sol61'
ns={'digits':['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'],'unicodedata':unicodedata};src=(R/'batches/kryha-mask-sol61/prepare.py').read_text();exec(src[src.index('def prep('):src.index('train=r/')],ns);prep=ns['prep']
train=R/'ciphers/hcp-393/work/sk_snk-ud-train.conllu';blocks=train.read_text().strip().split('\n\n');texts=[prep(x)for x in blocks[:int(.8*len(blocks))]]
models={n:Counter(g for t in texts for g in (t[i:i+n]for i in range(len(t)-n+1)))for n in range(2,8)}
models={n:{g:math.log(c)for g,c in d.items()}for n,d in models.items()}
(B/'model-provenance.json').write_text(json.dumps({'source':str(train),'sha256':hashlib.sha256(train.read_bytes()).hexdigest(),'TRAIN_fraction':.8,'preparation':'Q proper names; X sentences; digits spelled; accent strip','counts':{n:len(d)for n,d in models.items()},'test_or_control_not_used_in_model':True},indent=2))
for n in (6,7):
 (B/f'model{n}.tsv').write_text(''.join(f'{g} {v}\n' for g,v in models[n].items()))
neighbors=json.loads((S/'control-neighbors.json').read_text());records=[]
for i,c in enumerate(neighbors):
 scores={n:sum(models[n].get(t[k:k+n],-n)for t in c['plaintexts']for k in range(len(t)-n+1))for n in models}
 base=sum(scores[n]*w for n,w in [(2,.1),(3,.15),(4,.4),(5,.8)])
 records.append(dict(index=i,profile_rank=c['profile_rank'],swap=c['swap'],P=c['P'],scores=scores,baseline=base,extension=base+scores[6]*.8+scores[7]*.8,pure6=scores[6],pure7=scores[7]))
# This file is fully frozen before any truth read.
(B/'blind-ranked.json').write_text(json.dumps(sorted(records,key=lambda x:-x['extension']),indent=2))
truth=json.loads((S/'control-truth.json').read_text());truept=truth['plaintexts'][0][:-1];exact=[r for r in records if neighbors[r['index']]['plaintexts']==[truept,truept]]
out={'candidates':len(records),'exact_candidates':[{'index':c['index'],'profile_rank':c['profile_rank'],'swap':c['swap'],'ranks':{k:1+sum(r[k]>c[k]for r in records)for k in ['baseline','extension','pure6','pure7']},'scores':c}for c in exact], 'truth_read_only_after_blind_ranking_saved':True}
for metric in ['baseline','extension','pure6','pure7']:
 r=max(records,key=lambda x:x[metric]);pts=neighbors[r['index']]['plaintexts'];out[metric+'_winner']={'index':r['index'],'profile_rank':r['profile_rank'],'swap':r['swap'],'matches':[sum(a==b for a,b in zip(t,truept))for t in pts],'score':r[metric]}
(B/'control-score-audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
