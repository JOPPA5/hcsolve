from pathlib import Path
import json,math,collections
b=Path(__file__).resolve().parent;units=[u for u in range(26) if math.gcd(u,26)==1];allrows=0;checks=[];raw=json.load(open(b/'ransac-results.json'))['rows'][0]['output_positions']
for label,pairfile,resultfile in [('preferred','preferred-pair.json','ransac-results.json'),('pixel-strong','pixel-strong-pair.json','pixel-strong-ransac.json'),('pixel-strong-plus-moderate','pixel-strong-plus-moderate-pair.json','pixel-strong-plus-moderate-ransac.json')]:
 a,c=json.load(open(b/pairfile));result=json.load(open(b/resultfile));scores=[];equiv=[]
 for row in result['rows']:
  O=row['output_positions'];assert sorted(O)==list(range(26)) and O[0]==0;K=row['shifts_by_absolute_residue'];ring=[O.index(i) for i in range(26)];T={chr(97+x):chr(97+ring[(O[x]+1)%26]) for x in range(26)};x='a';visited=[]
  for i in range(26):visited.append(x);x=T[x]
  assert x=='a' and len(set(visited))==26
  matches=0
  for i in range(21,375):
   y=a[i]
   for _ in range(K[i%23]):y=T[y]
   matches+=y==c[i+1]
  assert matches==row['matched_cells'];scores.append(matches);u=[u for u in units if all(v==u*w%26 for v,w in zip(O,raw))];assert u;equiv+=u;allrows+=1
 checks.append(dict(label=label,rows=len(result['rows']),matched_cells=scores,unit_equivalences=equiv))
# Human review cycle compared only after independent fit, never read by RANSAC.
external='dvsagpqxwlfmhectizkjubrnyo';ext={c:i for i,c in enumerate(external)};comparison=[(u,k) for u in units for k in range(26) if all(raw[ord(c)-97]==(u*ext[c]+k)%26 for c in external)];assert comparison
control=json.load(open(b/'control-verification.json'));assert control['recovered_equivalent_output_ring'];report=dict(status='Verified shifted periodic common-cycle structure; plaintext and physical keys remain unknown',ring_and_residue_power_rows_checked=allrows,checks=checks,external_review_cycle_comparison_after_fit=comparison,positive_control=control,source_variants=json.load(open(b/'pixel-manifest.json')),extent_summary=[dict(label=z['label'],summary=z['summary']) for z in json.load(open(b/'extent.json'))],no_full_target_plaintext_or_reencryption_claim=True)
(b/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print('rows',allrows,'comparison',comparison);print([(z['label'],max(z['matched_cells'])) for z in checks])
