#!/usr/bin/env python3
"""Caesar -1 on manually reread body; explicit unresolved fields."""
import json,hashlib,string
from pathlib import Path
r=Path(__file__).resolve().parents[1]
for name,h in json.loads((r/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((r/'source'/name).read_bytes()).hexdigest()==h,name
key={c:chr((ord(c)-ord('A')-1)%26+ord('A')) for c in string.ascii_uppercase}
def dec(s):return ''.join(key.get(c.upper(),c) for c in s)
t=json.loads((r/'work/transcription.json').read_text())
print('Upper fields unresolved:',t['header'],t['upper_short_line'])
count=0
for s in t['body_cipher_lines']:
 print(dec(s));count+=sum(c.isalpha() for c in s)
print('Ambiguous word alternatives:',dec('Jibwf'),'/',dec('Jibuf'))
print('Closing unresolved:',t['closing'])
print(f'{count} body letters mapped; 1 body position ambiguous. Wholecard remains partial.')
print('Source hashes pass. Manual transcript, not pixel-to-text validation.')
