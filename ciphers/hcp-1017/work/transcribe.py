from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
# Physical opening directions, not plaintext. Lowercase=interior dot/stroke.
legend={'A':'┌','B':'┐','C':'└','D':'┘','E':'⊏','F':'⊐','G':'⊓','H':'⊔','I':'□','J':'<','K':'>','L':'∧','M':'∨','Q':'◇','X':'uncertain/cancelled'}
rows=[
'd A i a I',
'e I i D I E / i f J / J L I K d C I C / I J L H B d b M d I H',
'L A E / f K A / i A E / L D G / D I L / H B D e / J L I B f H / E i K',
'i I G A / C A J L d I i i f E / i I C d f E / f L B A / J L e e f g / K E',
'J L e A i f K A i D H / J I A c L / f L / K E / B D I Q / J C I D d G I C',
'I J b I A H B L L K A / I i D X I g / H B D b J i I F F b H / J L A H',
'I J K I H / d D E / L I / J I C / I D Q / A i d I / I J L G I D b',
]
# Draft only: segmentation/dot classification must be rechecked before decoding claims.
tokens=sorted(set(' '.join(rows).replace('/','').split()))
enc={t:chr(97+n) for n,t in enumerate(tokens)}
assert len(enc)<=26
ct=''.join(enc[t] for row in rows for t in row.replace('/','').split())
(p/'draft-shapes.json').write_text(json.dumps({'status':'provisional manual visual transcription, no plaintext','legend':legend,'rows':rows,'positions':len(ct),'tokens':enc,'source_hashes':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in (p.parent/'source').glob('*.jpg')}},indent=2)+'\n')
(p/'draft-cipher.txt').write_text(ct+'\n')
print(len(ct),enc)
