from pathlib import Path
from collections import Counter
import json,unicodedata,hashlib
B=Path(__file__).resolve().parent;old=Path('batches/repeat369-365-sol61')
norm=lambda s:''.join(ch for ch in unicodedata.normalize('NFD',s.lower())if ch in'abcdefghijklmnopqrstuvwxyz')
raw=(old/'plaintext.txt').read_text();sentences=[norm(x.replace('72','sedemdva'))for x in raw.split('.')if x.strip()];assert list(map(len,sentences))==[55,50]
rows=json.loads((old/'closest-inventory.json').read_text());seen=set();checks=[]
for row in rows:
 p=row['plaintext'];c=row['ciphertext']
 if p in seen:continue
 seen.add(p);cut=len(sentences[0])+row['first_sentence_X'];assert p[:55]==sentences[0]
 for reverse in[False,True]:
  left,right=(p[cut:],p[:cut])if reverse else(p[:cut],p[cut:]);a,b=c[:len(left)],c[len(left):]
  checks.append(dict(first_sentence_X=row['first_sentence_X'],reversed_sentence_blocks=reverse,left_length=len(left),right_length=len(right),left_missing=dict(Counter(left)-Counter(a)),left_surplus=dict(Counter(a)-Counter(left)),right_missing=dict(Counter(right)-Counter(b)),right_surplus=dict(Counter(b)-Counter(right))))
g365=(old/'ciphertext365.txt').read_text().split()[1:];g369=(old/'ciphertext369.txt').read_text().split()[1:]
payload365=[g for i,g in enumerate(g365,1)if i!=3];payload369=[g for i,g in enumerate(g369,1)if i!=5]
assert payload369==payload365[:2]+['ucnio']+payload365[2:]
preferred=next(r for r in rows if r['first_sentence_X']==1);p,c=preferred['plaintext'],preferred['ciphertext']
obj=dict(sentence_lengths=list(map(len,sentences)),distinct_X_preparations=len(seen),sentence_block_checks=checks,original_payload_groups=len(payload365),repeat_payload_groups=len(payload369),exact_group_relation='repeat payload =original firsttwo payloadgroups +UCNIO +remainingoriginalgroups',unique_letter_bridges={ch:dict(preferred_plain_position1=p.index(ch)+1,cipher_body_position1=c.index(ch)+1)for ch in ['f','b']if p.count(ch)==c.count(ch)==1},additional_word_or_glyph_changes=False)
(B/'source-check.json').write_text(json.dumps(obj,indent=2)+'\n')
paths=[Path('ciphers/hcp-369/source/cryptogram.jpg'),Path('batches/solved-context-main/365/cryptogram.jpg'),Path('batches/solved-context-main/365/plaintext.jpg'),B/'engine.py']
(B/'hashes.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths},indent=2)+'\n');print(obj['unique_letter_bridges'])
