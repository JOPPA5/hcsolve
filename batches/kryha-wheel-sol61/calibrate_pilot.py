from pathlib import Path
import json,random
p=Path(__file__).resolve().parent;folder=p/'control-m26';plain=(folder/'plaintext.txt').read_text().strip();ct=(folder/'ciphertext.txt').read_text().strip();key=json.loads((folder/'key.json').read_text());g=json.loads((p/'wheel52.json').read_text());coords=g['unwrapped_effective_coordinates'];lines=(folder/'masc-results.txt').read_text().splitlines();rows=[]
for i in range(0,len(lines),4):
 header=lines[i].split();r=dict(candidate_index=int(header[0]),concentration=int(header[1]),phase=int(header[2]),active_holes=[int(x)for x in header[3].split(',')if x],language_score=float(lines[i+1].split()[0]),plaintext=lines[i+1].split()[1],input_slots=[int(x)for x in lines[i+2].split(',')if x],output_positions=[int(x)for x in lines[i+3].split(',')if x]);r['matches_diagnostic_only']=sum(a==b for a,b in zip(plain,r['plaintext']));rows.append(r)
rows.sort(key=lambda r:r['language_score'],reverse=True);(folder/'language-reranked.json').write_text(json.dumps(rows,indent=2))
def concentration(O,stops,phase):
 N=[0]*26;m=len(stops);origin=coords[stops[phase]-1]
 for i,c in enumerate(ct):D=coords[stops[(phase+i)%m]-1]+179*((phase+i)//m)-origin;N[(O[ord(c)-97]-D)%26]+=1
 return sum(x*x for x in N)
rng=random.Random(5217902);null=[]
for _ in range(1000):
 O=list(range(26));rng.shuffle(O);stops=sorted(rng.sample(range(1,53),26));null.append(concentration(O,stops,rng.randrange(26)))
truth=concentration(key['output_positions'],key['active_holes'],key['active_phase_index']);report=dict(scope='unknown outputring, active mask andphase; stopCOUNT26 supplied inthispilot only',IC_restarts=100,IC_proposals_per_restart=10000,model_selection_truth_free=True,candidates=len(rows),MASC_budget_each='8x30000',true_concentration=truth,null_min=min(null),null_max=max(null),null_mean=sum(null)/len(null),null_ge_truth=sum(x>=truth for x in null),optimized_concentration_min=min(r['concentration']for r in rows),optimized_concentration_max=max(r['concentration']for r in rows),top_language_score=rows[0]['language_score'],top_language_match=rows[0]['matches_diagnostic_only'],diagnostic_best_matches=max(r['matches_diagnostic_only']for r in rows),full_plaintext_recovered=any(r['plaintext']==plain for r in rows))
(folder/'pilot-calibration.json').write_text(json.dumps(report,indent=2));print(report)
# Operative seed ONLYhighest language score; no comparison to plantedkey/plain.
r=rows[0];(folder/'joint-seed.txt').write_text(' '.join(map(str,r['input_slots']+r['output_positions']+[h-1 for h in r['active_holes']]+[r['phase']]))+'\n')
