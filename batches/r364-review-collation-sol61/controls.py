from exact_cover_insert import solve,enc
from pathlib import Path
import json,random
B=Path(__file__).resolve().parent;rng=random.Random(3641211)
base=''.join(rng.sample('abcdefghijklmnopqrstuvwxyz',26))+''.join(rng.choice('abcdefghijklmnopqrstuvwxyz')for _ in range(38));assert len(base)==64
at=17;plain=base[:at]+'x'+base[at:];rows=[]
for label,widths,align,known in [('fresh-blind-double',[5,6],[3,3],False),('primary-known-constant',[21,19,20],[7,7,7],True),('primary-known-progressive',[21,19,20],[4,5,6],True)]:
 keys=[];cipher=plain
 for w,n in zip(widths,align):
  key=rng.sample(list(range(1,w)),w-1);key.insert(n-1,0);keys.append(key);cipher=enc(cipher,key)
 # Independent exact finite U/V ambiguity, not unknown typos.
 u=cipher.index('u');v=cipher.index('v');other=list(cipher);other[u],other[v]=other[v],other[u];other=''.join(other)
 result=solve('?'*65,cipher,widths,15000 if not known else 5000,alignments=align,known_keys=keys if known else None,backend='eager',insert_x_template=base,cipher_variants=[cipher,other]);result.update(label=label,planted_template64=base,planted_plaintext65=plain,planted_keys=keys,true_extra_x_position=at,phase_unknown_except_declared_alignment=True,known_key_encoding_check=known,known_keys_used_for_target=False);rows.append(result);(B/'controls.json').write_text(json.dumps(rows,indent=2));print(label,result['status'],result['seconds'],flush=True);assert result['status']=='sat';assert result['predicted_ciphertext']in[cipher,other]
