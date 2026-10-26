"""Manual Pigpen transcript; reproduces marked reading, not OCR.
Run from any directory. Verifies original image hashes before using tokens.
"""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
j=json.loads((P/'body-shapes.json').read_text())
for name,expected in j['source_sha256'].items():
 assert hashlib.sha256((P.parent/'source'/name).read_bytes()).hexdigest()==expected,name
key=j['key']
rows=j['rows']+json.loads((P/'margin-shapes.json').read_text())['rows']
for r in rows:
 print(' / '.join(''.join(key[t] for t in w.split()) for w in r['tokens'].split('/')))
print('Position count:',sum(len(r['tokens'].replace('/','').split()) for r in rows))
print('Manual transcript; crossed mark unassigned; [M] is inferred under blot. TON and BUESSE are literal; corrections are editorial.')
