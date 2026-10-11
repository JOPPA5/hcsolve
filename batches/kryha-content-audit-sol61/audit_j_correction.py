from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parents[1];keys=json.loads((R/'batches/kryha-content-main/proposed-keys.json').read_text());key={x['number']:x for x in keys};source=R/'batches/kryha-shift23-sol61/351-pixel-strong.txt';old=source.read_text().strip();assert old[239]=='u' and old[230]=='l';crop=R/'batches/kryha-shift23-sol61/351-lvbnf-iihuu-bbxob.jpg';adj=json.loads((R/'batches/kryha-wheel-sol61/wheel52.json').read_text())['adjacent_distances']
def decode(ct,k):
 h=k['holes'];arcs=[]
 for a,b in zip(h,h[1:]+h[:1]):
  v=0;x=a
  while True:
   v+=adj[x];x=(x+1)%52
   if x==b:break
  arcs.append(v)
 assert sum(arcs)==179;d=k['initial_displacement'];pt=''
 for i,c in enumerate(ct):pt+=chr(97+k['P'][(k['O'][ord(c)-97]-d)%26]);d=(d+arcs[i%23])%26
 ip={x:i for i,x in enumerate(k['P'])};io={x:i for i,x in enumerate(k['O'])};d=k['initial_displacement'];enc=''
 for i,c in enumerate(pt):enc+=chr(97+io[(ip[ord(c)-97]+d)%26]);d=(d+arcs[i%23])%26
 assert enc==ct;return pt,enc
ct350=(R/'batches/kryha-shift23-sol61/350-pixel-strong.txt').read_text().strip();pt350,_=decode(ct350,key[350]);base,_=decode(old,key[351]);variants=[]
for label,changes in [('J-collated',{240:'j'}),('J-collated-I-alternative',{240:'j',231:'i'})]:
 letters=list(old)
 for pos,c in changes.items():letters[pos-1]=c
 ct=''.join(letters);pt,enc=decode(ct,key[351]);(B/f'351-{label}-ciphertext.txt').write_text(ct+'\n');(B/f'351-{label}-raw-prepared.txt').write_text(pt+'\n');(B/f'351-{label}-reencrypted.txt').write_text(enc+'\n');diffs=[dict(one_based=i+1,before=a,after=b)for i,(a,b)in enumerate(zip(base,pt))if a!=b];mis=[dict(position350=i+21,position351=i+22,letter350=a,letter351=b)for i,(a,b)in enumerate(zip(pt350[20:374],pt[21:375]))if a!=b];variants.append(dict(name=label,source_edits_one_based={p:{'before':old[p-1],'after':c}for p,c in changes.items()},prepared_edits=diffs,raw_prepared=pt,ciphertext_sha256=hashlib.sha256(ct.encode()).hexdigest(),exact_full385_reencryption=True,same_key_no_physical_or_ring_refitting=True,aligned_interior_discrepancies=mis,aligned_interior_discrepancy_count=len(mis),first5=pt[:5],contains_LACNEISIA='lacneisia' in pt,contains_EXISTUIE='existuie'in pt))
assert variants[0]['prepared_edits']==[dict(one_based=240,before='d',after='e')];assert variants[1]['prepared_edits']==[dict(one_based=231,before='i',after='s'),dict(one_based=240,before='d',after='e')]
assert variants[0]['contains_LACNEISIA']and variants[1]['contains_EXISTUIE'];(B/'J-correction-verification.json').write_text(json.dumps({'variants':variants,'baseline_source':str(source.relative_to(R)),'baseline_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_crop':str(crop.relative_to(R)),'source_crop_sha256':hashlib.sha256(crop.read_bytes()).hexdigest(),'J_pixel_reinspection':'last IIHUJ character clearly J; inspected after parent glyph alert','L_I_reinspection':'first glyph remains obscured; I retained only as explicit alternative','fixed_key_source':'batches/kryha-content-main/proposed-keys.json','fixed_key_sha256':hashlib.sha256((R/'batches/kryha-content-main/proposed-keys.json').read_bytes()).hexdigest(),'not_physical_refitting':True,'no_I_J_normalization_or_plaintext_cleanup':True},indent=2));print([(x['name'],x['prepared_edits'],x['aligned_interior_discrepancy_count'])for x in variants])
