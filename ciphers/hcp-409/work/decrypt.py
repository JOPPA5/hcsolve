"""Source-bound manual transcription decoder. No OCR or editorial repairs."""
from pathlib import Path
import json,hashlib,argparse
w=Path(__file__).resolve().parent
k=json.loads((w/'key.json').read_text())
for name,digest in k['source_hashes'].items():assert hashlib.sha256((w.parent/'source'/name).read_bytes()).hexdigest()==digest,name
assert hashlib.sha256((w/'transcription.txt').read_bytes()).hexdigest()==k['transcription_sha256']
ct=''.join((w/'transcription.txt').read_text().lower().split());P=k['input_positions'];O=k['output_positions'];h=k['holes_zero_based'];e=k['adjacent_distances'];invP={p:chr(97+i)for i,p in enumerate(P)};invO={o:chr(97+i)for i,o in enumerate(O)}
d=k['first_displacement'];p='';re=''
for i,c in enumerate(ct):
 x=invP[(O[ord(c)-97]-d)%26];p+=x;re+=invO[(P[ord(x)-97]+d)%26]
 a=h[i%len(h)];b=h[(i+1)%len(h)]
 while a!=b:d+=e[a];a=(a+1)%52
assert re==ct
if '--json' in __import__('sys').argv: print(json.dumps(dict(ciphertext_length=len(ct),decoded_length=len(p),plaintext=p,reencryption_equal=True,prefix_omitted=0,label_limits=k['label_limits']),indent=2))
else:print(p.upper())
