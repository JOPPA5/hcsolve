from experiment import *
controls=json.loads((P/'controls.json').read_text());rows=[]
for kind,w in [('beam',20),('one-long',19)]:
 c=next(x for x in controls if x['length']==400 and x['width']==w);positions=sorted(random.Random(61179400+w).sample(range(400),5));ct=''.join('.'if i in positions else ch for i,ch in enumerate(c['ciphertext']));expected=inverse(ct,c['planted_readout_columns'],c['planted_start_up']);candidates=[]
 for up in [0,1]:candidates+=attack(f'control-400-{w}-5erasures',ct,w,kind,up)
 candidates.sort(key=lambda c:c['score'],reverse=True);ranks=[i for i,r in enumerate(candidates)if r['plaintext']==expected];rows.append(dict(model=kind,width=w,erased_cipher_positions_0based=positions,source_control=f'400-{w}',ciphertext=ct,expected_masked_plaintext=expected,exact_masked_best=candidates[0]['plaintext']==expected,true_ranks=ranks,candidates=candidates,all_retained_reencrypt_exact=True))
(P/'damage-controls.json').write_text(json.dumps(rows,indent=2));print([(r['model'],r['exact_masked_best'],r['true_ranks'])for r in rows])
