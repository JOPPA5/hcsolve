from pathlib import Path
import json,itertools,collections
b=Path(__file__).resolve().parent;r=json.load(open('batches/kryha-two-mask-refine-sol61/actual-row5-pure6-r7-full.json'))[0];P=r['P'];inv={v:i for i,v in enumerate(P)};v=[''.join(chr(97+inv[ord(c)-97]) for c in s) for s in r['plaintexts']];(b/'projected.txt').write_text(' '.join(v)+'\n');(b/'seed.txt').write_text('0 0\n'+' '.join(map(str,P))+'\n'+'\n'.join(r['plaintexts'])+'\n');letters='ijgqx';out=[];blocks=[]
for num,perm in enumerate(itertools.permutations(letters)):
 rem={ord(a)-97:ord(bb)-97 for a,bb in zip(letters,perm)};key=[rem.get(x,x) for x in P];pts=[''.join(chr(97+key[ord(c)-97]) for c in s) for s in v];out.append(dict(id=num,mapping=dict(zip(letters,perm)),P=key,plaintexts=pts));blocks.append('0 0\n'+' '.join(map(str,key))+'\n'+'\n'.join(pts))
(b/'rare120.json').write_text(json.dumps(out,indent=2));(b/'rare120-seeds.txt').write_text('\n'.join(blocks)+'\n');locations={c:[dict(index=i,residue23=i%23,context=r['plaintexts'][0][max(0,i-12):i+13]) for i,x in enumerate(r['plaintexts'][0]) if x==c] for c in letters};(b/'locations.json').write_text(json.dumps(locations,indent=2))
