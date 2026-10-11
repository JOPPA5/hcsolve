from pathlib import Path
import json,collections,math
b=Path(__file__).resolve().parent;a,c=json.load(open(b/'preferred-pair.json'));rows=json.load(open(b/'ransac-results.json'))['rows'];row=rows[0];O=row['output_positions'];K=row['shifts_by_absolute_residue'];inverse={v:chr(97+i) for i,v in enumerate(O)};mismatch=[]
for i in range(21,375):
 x=a[i];y=c[i+1];pred=inverse[(O[ord(x)-97]+K[i%23])%26];preda=inverse[(O[ord(y)-97]-K[i%23])%26]
 if y!=pred:mismatch.append(dict(index350_zero=i,index351_zero=i+1,position350_one=i+1,position351_one=i+2,residue=i%23,observed350=x,observed351=y,predicted351_if350correct=pred,predicted350_if351correct=preda,group350_one=i//5+1,pos350_in_group=i%5+1,group351_one=(i+1)//5+1,pos351_in_group=(i+1)%5+1,context350=a[i//5*5:i//5*5+5],context351=c[(i+1)//5*5:(i+1)//5*5+5]))
(b/'discrepancies.json').write_text(json.dumps(mismatch,indent=2)+'\n')
print('\n'.join(f"350[{z['position350_one']}] {z['context350']} {z['observed350']}→{z['predicted350_if351correct']} OR 351[{z['position351_one']}] {z['context351']} {z['observed351']}→{z['predicted351_if350correct']}" for z in mismatch))
# All affine cycle-coordinate scales/offsets remain hypotheses; physical step sum179 is a constraint.
units=[u for u in range(26) if math.gcd(u,26)==1];choices=[]
for u in units:
 for add in range(26):
  steps=[(u*k+add)%26 for k in K];minimum=sum(v if v else 26 for v in steps)
  # Integer steps may be increased by26 only, so minimum179 is a strong necessary cycle sum.
  if minimum<=179 and (179-minimum)%26==0:choices.append(dict(multiplier=u,additive_offset=add,steps_mod26_by_absolute_residue=steps,min_positive_sum=minimum,remaining_full_turns=(179-minimum)//26))
(b/'physical-step-candidates.json').write_text(json.dumps(choices,indent=2)+'\n');print('physical sum candidates',len(choices));print(choices[:5])
