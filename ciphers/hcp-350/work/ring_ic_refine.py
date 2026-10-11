from pathlib import Path
import json,subprocess
p=Path(__file__).resolve().parent;rows=json.loads((p/'ring-ic-control-reranked.json').read_text());plain=(p/'ring-control-plain.txt').read_text().strip();results=[]
for i,row in enumerate(rows[:40]):
 # Operative ranking uses language_score only, NEVER control_match_count or planted ring closeness.
 key=p/f'ring-ic-refine-seed-{i:03}.txt';key.write_text(' '.join(map(str,row['input_slots']+row['output_positions']))+'\n');out=subprocess.check_output([str(p/'ring_ic_refine'),str(p),str(p/'ring-control-cipher.txt'),'6','-1',str(key)],text=True);(p/f'ring-ic-refine-result-{i:03}.txt').write_text(out);lines=out.splitlines();r=dict(seed_language_rank=i,ic_candidate_index=row['ic_candidate_index'],language_score=float(lines[0].split()[0]),plaintext=lines[0].split()[1],input_slots=[int(x)for x in lines[1].split(',')if x],output_positions=[int(x)for x in lines[2].split(',')if x]);r['control_match_count']=sum(x==y for x,y in zip(r['plaintext'],plain));r['exact_control']=r['plaintext']==plain;results.append(r);print(i,r['language_score'],r['control_match_count'],r['exact_control'],flush=True);(p/'ring-ic-control-refined.json').write_text(json.dumps(sorted(results,key=lambda r:r['language_score'],reverse=True),indent=2))
 if r['exact_control']:break
