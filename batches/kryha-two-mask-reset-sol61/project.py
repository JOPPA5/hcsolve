from pathlib import Path
import json,sys
b=Path(__file__).resolve().parent;r=b.parents[1];data=json.load(open(sys.argv[1]));coord=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'))['unwrapped_effective_coordinates'];out=[];limit=int(sys.argv[4]) if len(sys.argv)>4 else 100
for line in (b/sys.argv[2]).read_text().splitlines()[1:limit+1]:
 nums=line.split();masks=[list(map(int,nums[q::2])) for q in (1,2)];messages=[]
 for q in (0,1):
  h=masks[q];ct=data['ciphertexts'][q][q:];ct=ct[:len(data['ciphertexts'][0])-1];chars=[]
  for i,c in enumerate(ct):
   dis=coord[h[i%23]]-coord[h[0]]+(179 if h[i%23]<h[0] else 0)+179*(i//23)
   chars.append(chr(97+(data['O'][ord(c)-97]-dis-(data['K'][0] if q else 0))%26))
  messages.append(''.join(chars))
 out.append(' '.join(messages))
(b/sys.argv[3]).write_text('\n'.join(out)+'\n');(b/'zero-schedule.txt').write_text(' '.join(['0']*26)+'\n');(b/'dummy-pair.txt').write_text('a\na\n')
