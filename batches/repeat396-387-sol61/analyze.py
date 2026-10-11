from pathlib import Path
from collections import Counter
import unicodedata,json,hashlib
P=Path(__file__).resolve().parent;R=P.parents[1];norm=lambda t:''.join(c for c in unicodedata.normalize('NFD',t.lower()) if 'a'<=c<='z');groups={}
for n in [387,396]:
 a=(P/f'ciphertext{n}.txt').read_text().split();assert a.pop(0)=='755';assert len(a)==11 and all(len(g)==5 for g in a);groups[n]=a
old=(R/'ciphers/hcp-396/work/transcription.txt').read_text().split();assert old==groups[396];rows=[]
for i,(a,b) in enumerate(zip(groups[387],groups[396])):rows.append(dict(group1=i+1,positions1=[i*5+1,i*5+5],scan387=a,scan396=b,old396=old[i],different_slots1=[j+1 for j,(x,y) in enumerate(zip(a,b)) if x!=y],confidence='moderate-high different printedreading; watermark caveat' if a!=b else 'agree'))
(P/'groups.json').write_text(json.dumps(rows,indent=2));main=norm((P/'normalized-preferred-plaintext.txt').read_text());assert len(main)==50
variants={'preferred_non_crossed':main,'tentative_pre_crossed_svojej':norm('Podajte šifrou stručnú zprávu o situácii a svojej činnosti'),'both_crossed_and_new_retained_not_preferred':norm('Podajte šifrou stručnú zprávu o situácii a svojej činnosti možnej činnosti')};results=[]
for label,p in variants.items():
 for xs in range(6):
  pt=p+'x'*xs
  for n,g in groups.items():
   for omit in range(12):
    ct=''.join(v for i,v in enumerate(g,1) if i!=omit);a=Counter(pt)-Counter(ct);b=Counter(ct)-Counter(pt);results.append(dict(source=n,plaintext_reading=label,terminal_X=xs,plaintext=pt,plaintext_length=len(pt),omitted_group1=omit or None,omitted_group=g[omit-1] if omit else None,ciphertext=ct,ciphertext_length=len(ct),missing=dict(a),surplus=dict(b),missing_count=sum(a.values()),surplus_count=sum(b.values()),exact=Counter(pt)==Counter(ct)))
(P/'inventory.json').write_text(json.dumps(results,indent=2));assert not any(r['exact'] for r in results);best=min(r['missing_count']+r['surplus_count'] for r in results);closest=[r for r in results if r['missing_count']+r['surplus_count']==best];(P/'closest-inventory.json').write_text(json.dumps(closest,indent=2));paths=[R/'batches/solved-context-main/387/cryptogram.jpg',R/'batches/solved-context-main/387/plaintext.jpg',R/'ciphers/hcp-396/source/cryptogram.jpg',R/'ciphers/hcp-396/work/transcription.txt'];manifest=dict(source_hashes={str(f.relative_to(R)):hashlib.sha256(f.read_bytes()).hexdigest() for f in paths},published_archival_context=True,independent_decipherment=False,source_unchanged=True,groups=11,letters=55,scan_agreeing_positions=53,difference_positions1=[44,54],exact_inventory_cases=0,total_inventory_cases=len(results),preferred_plaintext_letters=len(main),ciphertext_F_count={str(n):''.join(g).count('f') for n,g in groups.items()},preferred_plaintext_F_count=main.count('f'),indicator_not_established=True,key_not_recovered=True);(P/'manifest.json').write_text(json.dumps(manifest,indent=2));print(manifest);print('Closest',[(r['source'],r['plaintext_reading'],r['omitted_group1'],r['terminal_X'],r['missing'],r['surplus']) for r in closest])
