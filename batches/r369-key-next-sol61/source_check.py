from pathlib import Path
from collections import Counter
import json,hashlib,unicodedata
B=Path(__file__).resolve().parent
old=Path('batches/repeat369-365-sol61')
rows=json.loads((old/'closest-inventory.json').read_text())
norm=lambda s:''.join(c for c in unicodedata.normalize('NFD',s.lower()) if c in 'abcdefghijklmnopqrstuvwxyz')
base=norm((old/'plaintext.txt').read_text().replace('72','sedemdva'))
groups=(old/'ciphertext369.txt').read_text().split()[1:]
body=''.join(g for i,g in enumerate(groups,1) if i!=5)
us=[dict(body_position1=i+1,whole_position1=i+1+(5 if i>=20 else 0),group1=(i+(5 if i>=20 else 0))//5+1) for i,ch in enumerate(body) if ch=='u']
ns=[i+1 for i,ch in enumerate(base) if ch=='n']
original=(old/'ciphertext365.txt').read_text().split()[1:];originalbody=''.join(g for i,g in enumerate(original,1) if i!=3)
obj=dict(base_plaintext=base,base_length=len(base),plain_N_positions1=ns,cipher_body_U_locations=us,body_length=len(body),literal_cipher_X_count=body.count('x'),literal_plain_X_count=base.count('x'),original365_body_length=len(originalbody),original365_inventory_missing=dict(Counter(base)-Counter(originalbody)),original365_inventory_surplus=dict(Counter(originalbody)-Counter(base)),conditional110_rows=rows,primary_rules={'accent_removal':True,'sentence_X':'optional','numbers':'full names digit by digit','proper_nouns_shortcuts_time':'divided by Q','KONIEC_random_padding':'text shorter than50','U_N_normalization':'not stated'},source_error_candidates='Any one literal body U could hypothetically replace prepared N; no chosen source correction.')
(B/'source-preparation.json').write_text(json.dumps(obj,indent=2)+'\n')
obj['worked_example_padding_evidence']={'fixture_raw_letters':52,'fixture_X_count':3,'fixture_prepared_length':55,'source':'batches/r-primary-example-audit-sol61/REPORT.md','interpretation':'two sentence X plus one padding X; compatible practice, not general proved rule'}
obj['preferred_source_motivated_layout']='105 lexical/digitwise letters + two sentence X + three final padding X =110'
(B/'source-preparation.json').write_text(json.dumps(obj,indent=2)+'\n')
files=[Path('ciphers/hcp-369/source/cryptogram.jpg'),Path('batches/solved-context-main/365/cryptogram.jpg'),Path('batches/solved-context-main/365/plaintext.jpg')]
(B/'source-hashes.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2)+'\n')
print('base',len(base),'cipher X',body.count('x'),'U locations',us)
