"""Integrity check and display of saved manual readings. Not a pixel decoder."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parents[2]
ids=[int(sys.argv[1])] if len(sys.argv)>1 else [1218,1217,1216,1213,1212]
for n in ids:
 p=root/f'ciphers/hcp-{n}'
 d=json.loads((p/'work/reading.json').read_text())
 for name,expected in d['source_sha256'].items():
  actual=hashlib.sha256((p/'source'/name).read_bytes()).hexdigest()
  if actual!=expected:raise SystemExit(f'CHANGED SOURCE: {n}/{name}')
 print(f'HCP{n}: {len(d["source_sha256"])} source files unchanged; {d["status"]} manual reading')
 print(d['reading'])
 print('\nEnglish translation:\n'+d['english']+'\n')
