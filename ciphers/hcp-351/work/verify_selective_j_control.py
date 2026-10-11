from pathlib import Path
import json,unicodedata,random
p=Path(__file__).resolve().parent;tokens=[]
source=p.parents[2]/'batches/scoring-sol61/german/source/de_gsd-ud-test.conllu'
for line in source.read_text().splitlines():
 if line and not line.startswith('#'):
  f=line.split('\t')
  if f[0].isdigit():
   w=''.join(c for c in unicodedata.normalize('NFD',f[1].lower().replace('ß','ss'))if'a'<=c<='z')
   if w:tokens.append(w)
plain='j'.join(tokens)[:385];assert plain==(p/'selective-j-control-plain.txt').read_text().strip()
k=json.loads((p/'selective-j-control-key.json').read_text());rng=random.Random(k['rng_seed']);P=list(range(26));O=list(range(26));rng.shuffle(P);rng.shuffle(O);j=P.index(9);P=P[j:]+P[:j];O=[(x-j)%26 for x in O];assert P==k['input_slots']and O==k['output_positions']
steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9]
def enc(text,P,O):
 I={c:i for i,c in enumerate(P)};inv={i:c for c,i in enumerate(O)};d=0;at=k['phase'];out=[]
 for c in text:
  out.append(chr(97+inv[(I[ord(c)-97]+d)%26]))
  for _ in range(2 if c=='j' else 1):d=(d+k['sign']*steps[at%17])%26;at+=1
 return ''.join(out)
assert enc(plain,P,O)==(p/'selective-j-control-cipher.txt').read_text().strip()
lines=(p/'selective-j-known-output-five-result.txt').read_text().splitlines();recovered=lines[1].split()[1];RP=[int(x)for x in lines[2].split(',')if x];RO=[int(x)for x in lines[3].split(',')if x];assert recovered==plain;assert RP[0]==9;assert enc(recovered,RP,RO)==enc(plain,P,O)
result=dict(exact_plaintext=True,positions=385,literal_J_count=plain.count('j'),independent_reencryption=True,scope='known output ring only; unknown other25input assignments',scoring='frozenGerman5gram; removeALLJ only for scoring; everyJ retained in exactplaintext/encryption',quad_control_failed_370=True,key_unique_not_claimed=True)
(p/'selective-j-known-output-five-verification.json').write_text(json.dumps(result,indent=2));print(result)
