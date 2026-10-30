#!/usr/bin/env python3
"""Read-only standard-library decoder of a manually read, explicitly incomplete record."""
from pathlib import Path
import csv,hashlib,json,re
W=Path(__file__).resolve().parent;ROOT=W.parents[2]
fixed={'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','8':'l','q':'z','g':'k','f':'v','h':'r','t':'d','r':'h','c':'s','s':'c','n':'m','m':'n','p':'b','b':'p','d':'t','y':'j','H':'ch'}
for name,digest in json.loads((W/'integrity.json').read_text()).items():
 assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,f'Hash mismatch: {name}'
# Root may extend the multi-target guard. Only this target's original entries are relevant.
guard=json.loads((ROOT/'batches/easy-2026-10-28/cz230-next-source-sha256.json').read_text())
for name in ['address.jpg','picture.jpg','metadata.md']:
 path=f'ciphers/hcp-1549/source/{name}'
 assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==guard[path]
assert json.loads((W/'key.json').read_text())==fixed
assert json.loads((ROOT/'ciphers/hcp-1520/work/key.json').read_text())==fixed
inverse={p:g for g,p in fixed.items()};assert len(inverse)==len(fixed)
def decode(s):return ''.join(fixed[c].upper() if c in fixed else c for c in s)
def encode(s):
 s=s.lower();i=0;out=''
 while i<len(s):
  if s[i:i+2]=='ch':out+=inverse['ch'];i+=2
  elif s[i].isalpha():out+=inverse[s[i]];i+=1
  else:out+=s[i];i+=1
 return out
rec=json.loads((W/'transcription.json').read_text());assert rec['manual'] is True
assert [r['id'] for r in rec['rows']]==[f'{p}{i:02d}' for p,n in [('T',5),('B',5),('L',11),('R',3)] for i in range(1,n+1)]
unc=rec['uncertainties'];token=re.compile(r'\{(U1|A1|A2)\}|(.)',re.S)
text='';expected=[];idx=known=ch=bounded=unknown=0;summary={}
for r in rec['rows']:
 s=r['cipher'];parts=re.split(r'(\{(?:U1|A1|A2)\})',s);out=''
 for part in parts:
  if part.startswith('{'):
   u=unc[part[1:-1]]
   if u['kind']=='bounded_alternative':
    assert len(u['candidates'])==2
    for c in u['candidates']:assert len(c)==1 and c in fixed and encode(decode(c))==c
    assert u['plain']=='['+'|'.join(decode(c) for c in u['candidates'])+']'
   else:assert u['kind']=='unknown_length_region' and u['plain']=='[UNK:U1]'
   out+=u['plain']
  else:
   assert all(c in fixed or c in ' ,.!?-' for c in part),r['id']
   plain=decode(part);assert encode(plain)==part,(r['id'],part);out+=plain
 text+=out+'\n';j=0;rk=rc=0
 for m in token.finditer(s):
  if m[1] or m[2] in fixed:
   idx+=1;j+=1;label=m[1] or m[2];kind=unc[label]['kind'] if m[1] else 'known'
   if kind=='known':known+=1;rk+=1;ch+=label=='H';rc+=label=='H'
   elif kind=='bounded_alternative':bounded+=1
   else:unknown+=1
   expected.append([str(idx),r['id'],str(j),kind,label,unc[label]['plain'] if m[1] else fixed[label].upper()])
 summary[r['id']]={'known_units':rk,'known_CH':rc}
assert text==(W/'literal.txt').read_text(),'Literal equality failed'
with (W/'indexed.csv').open() as f:
 reader=csv.reader(f);assert next(reader)==['record_index','row','row_token_position','kind','glyph_or_region','plain'];assert list(reader)==expected
print(text,end='')
print(f'CHECKED: {len(rec["rows"])} rows; {known} known cipher units; {ch} known CH units; {known+ch} known base letters; {bounded} bounded single-unit alternatives; {unknown} unknown-length region.')
print('Record/source/reference hashes, root source guard, indexed positions, actual fixed-key inverse and literal equality agree. Manual transcription is not OCR; these checks do not prove handwriting truth.')
print('ROW COUNTS: '+json.dumps(summary,separators=(',',':')))
