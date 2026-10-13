"""Decode manually observed shape tokens, bound to the archived scan.
No OCR; glyph uncertainty is preserved. No plaintext-to-token generation.
"""
from pathlib import Path
import json,hashlib,sys,unicodedata
ROOT=Path(__file__).resolve().parents[3]
n=int(sys.argv[1]);p=ROOT/f'ciphers/hcp-{n}'
manifest=json.loads((p/'work/as-seen-provenance.json').read_text())
assert hashlib.sha256((p/'source/address.jpg').read_bytes()).hexdigest()==manifest['address_sha256']
key={'DIGIT3':'3','A':'a','E':'e','F':'r','T':'t','D':'d','N':'n','M':'m','H':'{h|p}','I':'i','J':'j','K':'k','L':'l','O':'o','G':'g','Y':'y','GY':'gy','CS':'cs','V':'v','Z':'z','X':'u','6':'b','+':'f',')':'s','(':'c','.':'.',',':',','BLOT':'{blot}','BLOT-H':'{h?}','N4':'{nn?}','OVERWRITE-F/T':'{r|t}','END-I/O':'{i|o?}','BARS2/3':'{a|e?}','UNKNOWN':'{?}','UNCLEAR-F/T':'{r|t?}'}
acc={'acute':'\u0301','diaeresis':'\u0308','double-acute':'\u030b'}
for line in (p/'work'/manifest.get('ledger_file','as-seen.txt')).read_text().splitlines():
 if not line or line.startswith('#'):continue
 row,*tokens=line.split();letters=[]
 for t in tokens:
  base,_,accent=t.partition(':')
  char=key[base]
  if accent:char=unicodedata.normalize('NFC',char+acc[accent])
  letters.append(char)
 print(row+': '+''.join(letters))
