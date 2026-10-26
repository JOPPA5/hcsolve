from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parent.parent
for name,digest in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest()==digest,name
shapes=['BR','B','BL','R','C','L','TR','T','TL','V','>','<','^']
key={f'{s}{d}':chr(65+2*i+d) for i,s in enumerate(shapes) for d in (0,1)}
count=ambiguous=0
for line in (p/'work/transcription.txt').read_text().splitlines():
 if not line.strip() or line.startswith('#'): continue
 out=[]
 for token in line.split():
  if token=='|':out.append(' ');continue
  choices=token.split('/');assert all(t in key for t in choices)
  count+=1;ambiguous+=len(choices)>1
  letters=[key[t] for t in choices]
  out.append(letters[0] if len(letters)==1 else '['+'/'.join(letters)+']')
 print(''.join(out))
print(f'{count} cipher positions; {ambiguous} explicitly alternative token; other weak readings in uncertainties.json.')
print('Source hashes passed; manual image-to-token transcription, not OCR.')
print('Literal FLOWINQ retained; FLOWING is editorial. Signature probable JIM, dot uncertain.')
