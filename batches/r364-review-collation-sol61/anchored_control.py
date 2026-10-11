from pathlib import Path
from exact_cover_insert import solve,enc
import json,random
B=Path(__file__).resolve().parent;data=json.loads((B/'variants.json').read_text());template=data['four_sentence_X_template64'];plain=template[:19]+'x'+template[19:];rng=random.Random(364125211920);keys=[];ct=plain
for w in [21,19,20]:
 key=rng.sample(list(range(1,w)),w-1);key.insert(10,0);keys.append(key);ct=enc(ct,key)
u=ct.index('u');v=ct.index('v');alt=list(ct);alt[u],alt[v]=alt[v],alt[u];alt=''.join(alt)
r=solve('?'*65,ct,[21,19,20],60000,alignments=[11,11,11],backend='eager',anchors=True,explicit_vocab=True,insert_x_template=template,cipher_variants=[ct,alt]);r.update(label='fresh matched quote-primary blind anchor control',planted_keys=keys,planted_plaintext=plain,source_template=template,planted_ciphertext=ct,source_variant_ambiguity=alt,keys_not_given_to_solver=True,actual_source_cipher_not_used_as_control=True,extra_x_true_boundary=19,full_plaintext_recovery_exact=r.get('conditional_plaintext')==plain,full_key_recovery_exact=r.get('keys')==keys);(B/'anchored-control.json').write_text(json.dumps(r,indent=2));print(r['status'],r['seconds'],r['full_plaintext_recovery_exact'],flush=True)
