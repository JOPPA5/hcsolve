import json,subprocess
from pathlib import Path
p=Path(__file__).parent
controls=json.loads((p/'quag1-exact-controls.json').read_text());assert all(x['exact'] for x in controls)
held=json.loads((p/'quag1-heldout-controls.json').read_text());coverage=[]
for x in held:
 lines=(p/f"quag1-heldout-{x['T']}-result.txt").read_text().splitlines();K=[int(v) for v in lines[1].split(',') if v];R=[int(v) for v in lines[2].split(',') if v];ct=(p/f"quag1-heldout-{x['T']}.txt").read_text().strip();neighbors=[]
 for a in range(26):
  for b in range(a,26):
   k=K[:];k[a],k[b]=k[b],k[a];found=''.join('?' if c=='?' else chr(97+k[(ord(c)-97-R[i%len(R)])%26]) for i,c in enumerate(ct))
   if found==x['plaintext']:neighbors.append([a,b])
 coverage.append(dict(T=x['T'],exact_best=x['exact'],true_in_blind_all_swap_neighborhood=bool(neighbors),diagnostic_matching_swaps=neighbors))
(p/'quag1-heldout-neighborhood-coverage.json').write_text(json.dumps(coverage,indent=2));assert all(x['true_in_blind_all_swap_neighborhood'] for x in coverage)
rows=[]
for phase in range(5):
 f=p/f'target-phase-{phase}.txt';ct=f.read_text().strip()
 for T in range(1,6):
  out=subprocess.check_output([str(p/'quag1_exact'),str(p/'quadgrams.tsv'),str(f),str(T)],text=True);(p/f'quag1-target-{phase}-{T}-result.txt').write_text(out);lines=out.splitlines();score=float(lines[0].split()[0]);plain=lines[0].split()[1];K=[int(v) for v in lines[1].split(',') if v];R=[int(v) for v in lines[2].split(',') if v];neighbors=[]
  for a in range(26):
   for b in range(a,26):
    k=K[:];k[a],k[b]=k[b],k[a];found=''.join('?' if c=='?' else chr(97+k[(ord(c)-97-R[i%T])%26]) for i,c in enumerate(ct));neighbors.append(dict(swap=[a,b],alphabet_key=k,plaintext=found))
  (p/f'quag1-target-{phase}-{T}-neighbors.json').write_text(json.dumps(neighbors,indent=2));rows.append(dict(second_gap_position=90+phase,T=T,score=score,plaintext=plain,alphabet_key=K,phase_offsets=R,neighbors_file=f'quag1-target-{phase}-{T}-neighbors.json',enumeration=lines[3]));(p/'quag1-target-summary.json').write_text(json.dumps(rows,indent=2));print(phase,T,score,plain,flush=True)
