from pathlib import Path
import json,subprocess,time
exec((Path(__file__).parent/'run.py').read_text().split('# Algebraic orientation equivalence')[0])
log5=P/'target-postrefine5.jsonl';prior=[json.loads(x) for x in log5.read_text().splitlines()] if log5.exists() else [];done={(x['label'],x['phase']) for x in prior};source=[json.loads(x) for x in (P/'results.jsonl').read_text().splitlines()];targets=[r for r in source if r['framing_is_hypothesis']];assert len(targets)==34
for src in targets:
 label=src['label'];phase=src['phase']
 if (label,phase) in done:continue
 folder=P/'fivegram-from4-targets'/label/f'phase{phase}';folder.mkdir(parents=True,exist_ok=True);seed=folder/'seed.txt';seed.write_text(' '.join(map(str,src['input_slots']+src['output_positions']))+'\n');cipher=P/label/f'phase{phase}'/'cipher.txt';ct=cipher.read_text().strip();start=time.monotonic();(P/'postrefine5-state.json').write_text(json.dumps(dict(label=label,phase=phase,stage='pure5_joint_from_operative4winner',marker_scan=markers()))+'\n')
 with (folder/'refine.txt').open('w') as f:subprocess.run([str(P/'ring_ic_refine5'),str(M),str(cipher),str(phase),'1',str(seed)],stdout=f,check=True)
 r=parse((folder/'refine.txt').read_text());verify(r,ct,phase);r.update(label=label,seconds=time.monotonic()-start,seed_selection='all34 unchanged operative4gram final language winners, no manual key/letter correction',phase=phase,length=len(ct),marker_scan=markers(),objective='standalone frozen5gram',framing_is_hypothesis=True,source4_score=src['language_score'],source4_plaintext=src['plaintext'],restarts=8,proposals_per_restart=100000,no_IC_or_MASC_rerun=True);(folder/'result.json').write_text(json.dumps(r,indent=2)+'\n')
 with log5.open('a') as f:f.write(json.dumps(r)+'\n')
 print(label,phase,r['language_score'],r['seconds'],flush=True)
(P/'postrefine5-state.json').write_text(json.dumps(dict(stage='complete',marker_scan=markers()))+'\n')
