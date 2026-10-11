import run_pair as r
import json
controls=[]
for j in range(3):
 p=json.loads((r.P/f'control{j}/plant.json').read_text());rows={}
 for tag,filename in [('fourgram','result.json'),('fivegram','result5.json')]:
  f=r.P/f'control{j}/phase{p["phase"]}'/filename
  if f.exists():
   v=json.loads(f.read_text());r.verify(v,p['ciphertext_messages'],p['phase']);rows[tag]={k:v.get(k)for k in ['language_score','exact_plaintext_both','matches_per_message','independent_reencryption_exact_both','independent_inverse_exact_both','truth_used_for_selection']}
 controls.append(dict(label=f'control{j}',phase=p['phase'],sign=p['sign'],phase_supplied_in_control=True,results=rows))
targets={};allcomplete=True
for label in ['literal','preferred']:
 rows=[];cts=[(r.P/f'{label}-{n}.txt').read_text().strip()for n in [350,351]]
 for phase in range(17):
  folder=r.P/label/f'phase{phase}'
  if not(folder/'result5.json').exists():allcomplete=False;continue
  v=json.loads((folder/'result5.json').read_text());r.verify(v,cts,phase);four=json.loads((folder/'result.json').read_text());r.verify(four,cts,phase);rows.append(dict(phase=phase,fourgram_score=four['language_score'],fivegram_score=v['language_score'],fivegram_plaintext_messages=v['plaintext_messages'],independent_reencryption_exact_both=True,independent_inverse_exact_both=True,full_key_file=str(folder/'result5.json')))
 targets[label]=dict(completed_phases=len(rows),requested_phases=17,ranked=sorted(rows,key=lambda x:x['fivegram_score'],reverse=True))
out=dict(complete=allcomplete,controls=controls,targets=targets,model='shared mixed rings and original fixed17 phase with per-message displacement/step-index reset',direction='negative stepping included by exact ring reflection equivalence',warnings=['shared key, old fixed17 sequence, one press per character, common phase and source chronology all conditional','controls tested at supplied phases; optimizer is probabilistic','frozen Slovak language model and constructed preparation may not match actual texts','no target family exclusion follows from failure','three original source-preferred glyph alternatives fixed before search'])
(r.P/'summary.json').write_text(json.dumps(out,indent=2));print('complete',allcomplete,[(k,v['completed_phases'])for k,v in targets.items()])
