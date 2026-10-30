#!/usr/bin/env python3
"""Caesar -1 on the manually frozen transcript (work/transcription.json); not OCR.
Text inside {braces} is a literal abbreviation and is printed unshifted."""
import hashlib,json,re,string
from pathlib import Path
r=Path(__file__).resolve().parents[1]
for name,h in json.loads((r/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((r/'source'/name).read_bytes()).hexdigest()==h,name
key={c:chr((ord(c)-ord('A')-1)%26+ord('A')) for c in string.ascii_uppercase}
enc={v:k for k,v in key.items()}
def dec(s):
 out=[];n=0
 for part in re.split(r'(\{[^}]*\})',s):
  if part.startswith('{'): out.append('['+part[1:-1].upper()+']')
  else:
   out.append(''.join(key.get(c.upper(),c) for c in part)); n+=sum(c.isalpha() for c in part)
 return ''.join(out),n
t=json.loads((r/'work/transcription.json').read_text())
body=0
print('BODY')
for s in t['body_cipher_lines']:
 p,n=dec(s);body+=n;print(' ',s.ljust(26),'->',p)
print('CLOSING')
clos=0
for f in t['closing']:
 if f['status'] in ('frozen','probable'):
  p,n=dec(f['raw']);assert p==f['plain'],(p,f)
  assert ''.join(enc[c] for c in p)==f['raw'].upper()
  clos+=n;print(' ',f['raw'].ljust(26),'->',p,'' if f['status']=='frozen' else '(probable)')
 elif f['status']=='literal': print(' ',f['raw'].ljust(26),'->',f'[{f["raw"].upper()}] (literal abbreviation)')
 else: print(' ',f['raw'].ljust(26),'->',f['plain'],'(contextual restoration)')
print(f'{body} shifted letters in body, {clos} in closing; literal abbreviations not counted.')
# Reading assembled from the decoded transcript (not hard-coded); dots between words dropped, brackets kept.
def norm(x):
 x=re.sub(r'\[([^\]]*)\]',lambda m:'['+m.group(1).replace('.','\x00')+']',x)
 x=x.replace('.','').replace('\x00','.')
 return ' '.join(x.split())
bodytxt=' '.join(norm(dec(s)[0]) for s in t['body_cipher_lines'])
closetxt=' '.join(f['plain'] if f['status']=='restored' else norm(dec('{'+f['raw']+'}' if f['status']=='literal' else f['raw'])[0]) for f in t['closing'])
print('Reading (computed):',bodytxt,'/',closetxt)
assert bodytxt=='MY OWN [E. L.] BOY I AM SO SORRY I CAN\'T WRITE LETTER "TO-NIGHT"',bodytxt
assert closetxt=='MY [N. & L.] YOUR [OWN] [E. L.] GIRL',closetxt
print('Source hashes pass.')
