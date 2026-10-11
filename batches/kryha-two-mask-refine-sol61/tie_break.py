from pathlib import Path
import sys,json
B=Path(__file__).resolve().parent;R=B.parents[1];lines=Path(sys.argv[1]).read_text().splitlines();start=next(i for i,l in enumerate(lines)if l.startswith('N 6 '));end=next((i for i in range(start+1,len(lines))if lines[i].startswith('N ')),len(lines));rows=[];models={}
for n in range(2,6):
 p=R/(f'batches/kryha-mask-sol61/model{n}.tsv'if n<4 else f'ciphers/hcp-350/work/ring-{n}grams.tsv');models[n]={g:float(v)for g,v in(x.split()for x in p.read_text().splitlines())}
for i in range(start+1,end,4):
 v=lines[i].split();score=float(v[0]);texts=lines[i+2:i+4];sc=sum(w*sum(models[n].get(t[j:j+n],-n)for t in texts for j in range(len(t)-n+1))for n,w in[(2,.1),(3,.15),(4,.4),(5,.8)]);rows.append((score,sc,i,texts))
best=max(x[0]for x in rows);ties=[x for x in rows if abs(x[0]-best)<1e-8];winner=max(ties,key=lambda x:x[1]);out=B/f'{sys.argv[2]}-tiebroken.txt';out.write_text('N 6 COUNT 1\n'+'\n'.join(lines[winner[2]:winner[2]+4])+'\n');(B/f'{sys.argv[2]}-ties.json').write_text(json.dumps({'primary_pure6':best,'retained_candidates':len(rows),'equal_primary_candidates':len(ties),'secondary_baseline_score':winner[1],'tiebreaker':'frozen2..5 score only among equal pure6 maxima','no_truth_or_manual_letters':True},indent=2));print(sys.argv[2],len(ties),winner[1])
