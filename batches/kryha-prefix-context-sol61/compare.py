from pathlib import Path
import json,hashlib,itertools
B=Path(__file__).resolve().parent
g374='kidah crtcs bvbpt iloiq spqho nzyhi qlxum aipot kbcey hvuiu qoqpm tlijv abave kzaxi mlemp qxmjc jslwf'.split()
c373=Path('batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip()
g373=[c373[i:i+5] for i in range(0,len(c373),5)]
variants=[]
for a,b,c in itertools.product(['crtcs','crtcg'],['spqho','spqhq'],['tlijv','tlijy']):
 g=g374.copy();g[1]=a;g[4]=b;g[11]=c;s=''.join(g)
 variants.append({'groups':g,'full_substring_start_1based':c373.find(s)+1 if s in c373 else None,'remaining80_substring_start_1based':c373.find(s[5:])+1 if s[5:] in c373 else None,'matching_group_pairs_1based':[[i+1,j+1,x] for i,x in enumerate(g) for j,y in enumerate(g373) if x==y],'last15_exact':g[-15:]==g373[-15:]})
(B/'374-preferred85.txt').write_text(''.join(g374)+'\n')
(B/'comparison.json').write_text(json.dumps({'length373':len(c373),'length374':85,'last15_373':g373[-15:],'variants':variants},indent=2)+'\n')
files=[Path('ciphers/hcp-374/source/cryptogram.jpg'),Path('ciphers/hcp-374/source/metadata.md'),Path('ciphers/hcp-374/SOURCES.md'),Path('batches/solved-context-main/373/cryptogram.jpg'),Path('batches/solved-context-main/373/SOURCES.md')]
(B/'manifest.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2)+'\n')
print('8 variants: full/remaining substring absent; last15 not identical; exact shared groups:',variants[0]['matching_group_pairs_1based'])
