from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent.parent
key=dict(zip('BR0 BR1 B0 B1 BL0 BL1 R0 R1 C0 C1 L0 L1 TR0 TR1 T0 T1 TL0 TL1 V0 V1 >0 >1 <0 <1 ^0 ^1'.split(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
for name,digest in json.loads((p/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest()==digest,name
count=words=ambiguous=0
for line in (p/'work/transcription.txt').read_text().splitlines():
 if line.startswith('#'):print(line);continue
 if not line.strip():continue
 out=[]
 for token in line.split():
  alternatives=token.split('/');assert all(t in key for t in alternatives)
  letters=[key[t] for t in alternatives]
  out.append(letters[0] if len(letters)==1 else '['+'/'.join(letters)+']')
  count+=1;ambiguous+=len(letters)>1
 print(''.join(out));words+=1
print(f'Encrypted positions: {count}; word units: {words}; alternative positions: {ambiguous}.')
print('Source hashes passed. Manual sign-by-sign transcript, not OCR; cancelled ink excluded and documented.')
