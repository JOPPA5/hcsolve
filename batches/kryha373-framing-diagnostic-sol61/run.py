from pathlib import Path
import unicodedata,itertools,json,random,hashlib
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
text=(root/'batches/kryha373-collation-sol61/plaintext-typed.txt').read_text();before=text.split('6.000')[0];ct=(root/'batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip().lower()
def normalize(s):return ''.join(x for x in unicodedata.normalize('NFD',s.lower())if 'a'<=x<='z')
base=normalize(before);assert len(base)==93
# Architecture-only positive control: arbitrary rotor permutation conjugating a fixed-point-free reflector.
rng=random.Random(3733746012);control=[]
for x in base:
 f=rng.sample(range(26),26);inv={v:i for i,v in enumerate(f)};a=ord(x)-97;control.append(chr(97+inv[f[a]^1]))
control=''.join(control);assert all(a!=b for a,b in zip(base,control));assert any(a==b for a,b in zip(base,base))
(out/'control.json').write_text(json.dumps({'p':base,'c':control,'zero_self_matches':True,'identity_negative_rejected':True,'scope':'reflector-conjugation architecture, no historical rotor stepping/key recovery'},indent=2)+'\n')
results=[]
for retain_d,natural_i,comma in itertools.product([True,False],[False,True],['','j','x']):
 p=normalize(before.replace(',',comma))
 if not retain_d:p=p.replace('ustredni','ustreni',1)
 if natural_i:p=p.replace('j','i') if comma=='' else normalize(before.replace(',','!')).replace('ustredni','ustredni'if retain_d else'ustreni').replace('j','i') # preserve marker below
 if natural_i and comma:p=normalize(before.replace(',','Q')).replace('ustredni','ustredni'if retain_d else'ustreni').replace('j','i').replace('q',comma)
 for offset,a,b in itertools.product(range(26),['l','i'],['e','a']):
  cc=list(ct);cc[52]=a;cc[89]=b;cc=''.join(cc)[offset:offset+len(p)]
  conflicts=[{'plaintext_position_1based':i+1,'source_cipher_position_1based':offset+i+1,'letter':x}for i,(x,y)in enumerate(zip(p,cc))if x==y]
  results.append(dict(retain_handwritten_d=retain_d,natural_J_to_I=natural_i,comma_marker=comma,offset=offset,glyph53=a,glyph90=b,p=p,length=len(p),self_matches=conflicts,passes_no_self=not conflicts))
(out/'results.json').write_text(json.dumps(results,indent=2)+'\n')
passed=[r for r in results if r['passes_no_self']];summary={'cases':len(results),'necessary_condition_survivors':len(passed),'survivor_cases':passed,'literal_base93':base,'literal_comma_J94':normalize(before.replace(',','j')),'source_hashes':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()for p in [root/'batches/solved-context-main/373/plaintext.jpg',root/'batches/solved-context-main/373/cryptogram.jpg',root/'batches/kryha373-collation-sol61/plaintext-typed.txt',root/'batches/historical-context/diplomatic-ciphers-2020.pdf']}}
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('cases',len(results),'no-self survivors',len(passed));print([(r['retain_handwritten_d'],r['natural_J_to_I'],r['comma_marker'],r['offset'])for r in passed]);print('min conflicts',min(len(r['self_matches'])for r in results))
