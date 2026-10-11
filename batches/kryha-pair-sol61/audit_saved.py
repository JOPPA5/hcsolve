import run_pair as r
import json
counts={'phases':0,'profile_language_candidates':0,'operative_candidates':0}
for label in ['control0','control1','control2','literal','preferred']:
 for folder in sorted((r.P/label).glob('phase*')):
  phase=int(folder.name[5:]);cts=(folder/'cipher.txt').read_text().split()
  f=folder/'reranked.json'
  if f.exists():
   rows=json.loads(f.read_text());assert len(rows)==300
   for v in rows:r.verify(v,cts,phase)
   counts['profile_language_candidates']+=len(rows)
  for name in ['result.json','result5.json']:
   f=folder/name
   if f.exists():r.verify(json.loads(f.read_text()),cts,phase);counts['operative_candidates']+=1
  if(folder/'result5.json').exists():counts['phases']+=1
counts.update(all_saved_rings_valid_permutations=True,independent_full_reencryption_both=True,independent_full_inverse_both=True,independent_ngram_boundary_scores=True)
(r.P/'saved-audit.json').write_text(json.dumps(counts,indent=2));print(counts)
