from pathlib import Path
from collections import Counter
import json,hashlib,unicodedata,re
P=Path(__file__).resolve().parent;R=P.parents[1]
files={'391cipher':R/'batches/solved-context-main/391/cryptogram.jpg','391plaintext':R/'batches/solved-context-main/391/plaintext.jpg','399cipher':R/'ciphers/hcp-399/source/75391655400592-large.jpg','399working':R/'ciphers/hcp-399/work/transcription.txt'}
def norm(t):return ''.join(c for c in unicodedata.normalize('NFD',t.lower()) if 'a'<=c<='z')
a=(P/'transcription391-preferred.txt').read_text().split();b=(P/'transcription399-preferred.txt').read_text().split();old=files['399working'].read_text().split();assert a[0]==b[0]==old[0]=='5245';a=a[1:];b=b[1:];old=old[1:];assert len(a)==len(b)==49 and all(len(g)==5 for g in a+b)
uncertainties={1:'Both readings retain L in PJN[L/I]Y; fourth glyph lacks reliable dot distinction at current scan.',9:'Both scans favor KAMLO; A/E remains secondary uncertainty. Original work KEMLO.',22:'391 OSAUC versus399 OSEUC: A/E unresolved; independent typed sheets, no key-selected correction.',24:'391 ZKETI secondglyph masked by vertical watermark, L possible;399 clearerK.',33:'391 PETTA versus399 PETTE: finalA/E uncertain.',35:'DMREN preferred in both; terminalglyph stronglyN, archivalinkartifact can resembleH.',38:'391 CEEKM versus399 AEEKM: initialC/A uncertain underwatermark.',41:'Both favor AOUOU; originalwork AOHOU, U/H remains a localreading uncertainty.',43:'391 KJACJ versus399 KJEAJ: middleA/E andfourthC/A uncertain.',46:'391 REHUL versus399 KEHUL: initialR/K partlycovered.'}
rows=[]
for i,(x,y,z) in enumerate(zip(a,b,old),1):rows.append(dict(group=i,start_position1=(i-1)*5+1,scan391=x,scan399=y,old399=z,scan_differences=[j+1 for j,(v,w) in enumerate(zip(x,y)) if v!=w],uncertainty=uncertainties.get(i,'')))
(P/'groups.json').write_text(json.dumps(rows,indent=2));l=['| Group | positions1 |391 preferred|399 preferred|Old399work|Uncertainty|','|---:|---|---|---|---|---|']
for z in rows:l.append(f"|{z['group']}|{z['start_position1']}–{z['start_position1']+4}|{z['scan391']}|{z['scan399']}|{z['old399']}|{z['uncertainty']}|")
(P/'groups.md').write_text('\n'.join(l)+'\n')
raw=(P/'plaintext391.txt').read_text();digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'];variants={'literal_letters_digits_omitted':norm(raw),'literal_each_digit_spelled':norm(''.join(digits[int(c)] if c.isdigit() else c for c in raw))}
inv=[]
for cname,groups in [('391',a),('399',b)]:
 for name,p in variants.items():
  for omit in range(50):
   ct=''.join(g for j,g in enumerate(groups,1) if j!=omit);surplus=Counter(ct)-Counter(p);deficit=Counter(p)-Counter(ct);inv.append(dict(cipher=cname,plaintext_model=name,plaintext_length=len(p),ciphertext_length=len(ct),omitted_group=omit or None,missing_count=sum(deficit.values()),missing=dict(deficit),surplus_count=sum(surplus.values()),surplus=dict(surplus)))
(P/'inventory.json').write_text(json.dumps(inv,indent=2));manifest=dict(provenance_parent='batches/solved-context-main/391/SOURCES.md',portal391='https://crypto.hcportal.eu/dashboard/cryptograms/391',portal399='https://crypto.hcportal.eu/dashboard/cryptograms/399',access_date='2026-10-11',hashes={k:hashlib.sha256(f.read_bytes()).hexdigest() for k,f in files.items()},group_count=49,ciphertext_letters=245,preferred_agreeing_letters=sum(v==w for v,w in zip(''.join(a),''.join(b))),preferred_differing_letters=sum(v!=w for v,w in zip(''.join(a),''.join(b))),differences_uncertain=True,published_plaintext_not_independently_deciphered=True,exact_prepared_known_pair_established=False,source_immutable=True)
(P/'manifest.json').write_text(json.dumps(manifest,indent=2));print(manifest);print({k:len(v) for k,v in variants.items()})
