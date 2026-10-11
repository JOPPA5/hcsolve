from pathlib import Path
from collections import Counter
import json,hashlib,unicodedata
P=Path(__file__).resolve().parent;R=P.parents[1];norm=lambda t:''.join(c for c in unicodedata.normalize('NFD',t.lower()) if 'a'<=c<='z')
a=(P/'ciphertext365.txt').read_text().split();b=(P/'ciphertext369.txt').read_text().split();assert a.pop(0)==b.pop(0)=='7115';assert len(a)==22 and len(b)==23;assert all(len(g)==5 for g in a+b)
# Fullphysicalgroupmap; bodyorderinginoriginaldiffersattwoadjacentgroups.
map365to369=[1,2,5,4]+list(range(6,24));assert len(map365to369)==22
rows=[dict(group365=i+1,group369=j,ct365=g,ct369=b[j-1],agree=g==b[j-1]) for i,(g,j) in enumerate(zip(a,map365to369))];assert all(r['agree'] for r in rows);(P/'groups.json').write_text(json.dumps(rows,indent=2));raw=(P/'plaintext.txt').read_text();sentences=[t.strip() for t in raw.split('.') if t.strip()];assert len(sentences)==2
nums={'digits_omitted':'','digit_SEDEMDVA':'sedemdva','digit_SEDEMDVE':'sedemdve','cardinal_SEDEMDESIATDVA':'sedemdesiatdva','cardinal_SEDEMDESIATDVE':'sedemdesiatdve','nonstandard_SEDEMDESATDVA':'sedemdesatdva','nonstandard_SEDEMDESATDVE':'sedemdesatdve'};results=[]
for name,n in nums.items():
 for x1 in [0,1]:
  for x2 in [0,1]:
   for filler in range(5):
    p=norm(sentences[0].replace('72',n))+'x'*x1+norm(sentences[1])+'x'*(x2+filler)
    for source,groups in [('365',a),('369',b)]:
     for omit in range(len(groups)+1):
      c=''.join(g for i,g in enumerate(groups,1) if i!=omit);missing=Counter(p)-Counter(c);surplus=Counter(c)-Counter(p);results.append(dict(source=source,numeral_model=name,first_sentence_X=x1,second_sentence_X=x2,extra_final_X=filler,plaintext=p,plaintext_length=len(p),omitted_group1=omit or None,omitted_group=groups[omit-1] if omit else None,ciphertext=c,ciphertext_length=len(c),missing=dict(missing),surplus=dict(surplus),missing_count=sum(missing.values()),surplus_count=sum(surplus.values()),exact=Counter(p)==Counter(c)))
(P/'inventory.json').write_text(json.dumps(results,indent=2));matches=[r for r in results if r['exact']];assert not matches;best=min(r['missing_count']+r['surplus_count'] for r in results);closest=[r for r in results if r['missing_count']+r['surplus_count']==best];(P/'closest-inventory.json').write_text(json.dumps(closest,indent=2));paths=[R/'batches/solved-context-main/365/cryptogram.jpg',R/'batches/solved-context-main/365/plaintext.jpg',R/'ciphers/hcp-369/source/cryptogram.jpg',R/'ciphers/hcp-369/work/transcription.txt'];manifest=dict(source_hashes={str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest() for f in paths},groups365=22,letters365=110,groups369=23,letters369=115,physical_group_agreement=22,missing_original_group='UCNIO',reordered_pair_original='WITPK ONDEX',reordered_pair_repeat='ONDEX WITPK',published_plaintext_attributed=True,numeral_models=nums,raw_alphabetic_plaintext_length=len(norm(raw)),inventory_cases=len(results),exact_inventory_matches=0,min_inventory_difference=best,source_unchanged=True,recovered_key=False,indicator_not_established=True);(P/'manifest.json').write_text(json.dumps(manifest,indent=2));print(manifest);print('Closest:',[(r['source'],r['numeral_model'],r['omitted_group1'],r['first_sentence_X'],r['second_sentence_X'],r['extra_final_X'],r['missing'],r['surplus']) for r in closest])
