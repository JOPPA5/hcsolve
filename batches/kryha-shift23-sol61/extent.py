from pathlib import Path
import json
b=Path(__file__).resolve().parent;row=json.load(open(b/'ransac-results.json'))['rows'][0];O=row['output_positions'];K=row['shifts_by_absolute_residue'];results=[]
for label,path in [('preferred',b/'preferred-pair.json'),('pixel-strong',b/'pixel-strong-pair.json'),('pixel-strong-plus-moderate',b/'pixel-strong-plus-moderate-pair.json')]:
 a,c=json.load(open(path));cells=[dict(index350_zero=i,index351_zero=i+1,letter350=a[i],letter351=c[i+1],residue=i%23,power_observed=(O[ord(c[i+1])-97]-O[ord(a[i])-97])%26,power_modal=K[i%23],match=(O[ord(c[i+1])-97]-O[ord(a[i])-97])%26==K[i%23]) for i in range(384)];summary=[]
 for lo,hi in [(0,20),(20,21),(21,374),(374,375),(375,384),(20,374)]:
  v=cells[lo:hi];summary.append(dict(range350_zero_inclusive_exclusive=[lo,hi],matches=sum(z['match'] for z in v),cells=len(v)))
 results.append(dict(label=label,summary=summary,cells=cells))
(b/'extent.json').write_text(json.dumps(results,indent=2)+'\n');print([(z['label'],z['summary']) for z in results])
