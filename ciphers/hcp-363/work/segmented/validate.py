from pathlib import Path
import json
p=Path(__file__).resolve().parent;controls=json.loads((p.parent/'controls.json').read_text());result={}
def dec(ct,key):
 w=len(key);h,r=divmod(len(ct),w);cols=['']*w;at=0
 for col in key:
  n=h+(col<r);cols[col]=ct[at:at+n];at+=n
 return ''.join(cols[col][row] for row in range(h+1) for col in range(w) if row<len(cols[col]))
for width in [19,22]:
 name=f'control-{width}';line=(p/f'control{width}-v3-results.txt').read_text().splitlines()[0];parts=line.split();key=[int(x) for x in parts[2].removeprefix('key=').split(',') if x];plain=parts[3]
 assert plain==controls[name]['plaintext'];assert key==controls[name]['keys'][0]
 assert dec((p.parent/(name+'.txt')).read_text().strip(),key)==plain
 assert ''.join(plain[j::width] for j in key)==(p.parent/(name+'.txt')).read_text().strip()
 result[name]={'exact_plaintext':True,'exact_key':True,'independent_inverse':True,'reencryption':True,'result':line}
(p/'control-v3-validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
