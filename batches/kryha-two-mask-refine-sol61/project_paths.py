from pathlib import Path
import json,sys
B=Path(__file__).resolve().parent;R=B.parents[1];data=json.load(open(sys.argv[1]));rows=Path(sys.argv[2]).read_text().splitlines()[1:];P=list(map(int,Path(sys.argv[3]).read_text().split()));coord=json.loads((R/'batches/kryha-wheel-sol61/wheel52.json').read_text())['unwrapped_effective_coordinates'];label=sys.argv[4];pro=[];mas=[]
for rank,row in enumerate(rows):
 nums=row.split();hs=[list(map(int,nums[q::2]))for q in (1,2)];texts=[]
 for q,h in enumerate(hs):
  ct=data['ciphertexts'][q][q:][:len(data['ciphertexts'][0])-1];out=''
  for i,c in enumerate(ct):d=coord[h[i%23]]-coord[h[0]]+(179 if h[i%23]<h[0]else 0)+179*(i//23)+(data['K'][0]if q else 0);out+=chr(97+(data['O'][ord(c)-97]-d)%26)
  texts.append(out)
 pro.append(' '.join(texts));mas.extend([f'{rank} {nums[0]}',' '.join(map(str,P))]+[''.join(chr(97+P[ord(c)-97])for c in t)for t in texts])
(B/f'{label}-projected.txt').write_text('\n'.join(pro)+'\n');(B/f'{label}-fixedP.txt').write_text('\n'.join(mas)+'\n')
