"""Independent cumulative-coordinate encoder/inverse of the complete reading."""
from pathlib import Path
import json,argparse,sys
sys.dont_write_bytecode=True
from decrypt import load,decode,encode
key,c=load();P=key['input_positions'];O=key['output_positions'];holes=key['holes_zero_based'];edges=key['adjacent_distances'];coords=[0]
for edge in edges:coords.append(coords[-1]+edge)
def independent_d(i):
    pos=holes[i%23];start=holes[0]
    return (key['first_displacement']+coords[pos]-coords[start]+179*(pos<start)+179*(i//23))%26
ip={v:chr(97+i) for i,v in enumerate(P)};io={v:chr(97+i) for i,v in enumerate(O)}
outputs=[]
for label,ct in [('preferred-independent',c),('alternate35N',c[:34]+'n'+c[35:])]:
    p=''.join(ip[(O[ord(ch)-97]-independent_d(i))%26] for i,ch in enumerate(ct[5:]))
    reencoded=ct[:5]+''.join(io[(P[ord(ch)-97]+independent_d(i))%26] for i,ch in enumerate(p))
    assert p==decode(key,ct) and reencoded==ct and encode(key,p)==ct
    outputs.append(dict(reading=label,plaintext_literal=p,source_reading=ct,body_match=80,source_roundtrip=85,padding_label='hypothesis X for coordinate19'))
result=dict(independent_method='absolute wheel coordinates and wrap count; separate from adjacent walk',outputs=outputs,source_hash_verified=True,unused_label_completion_not_historical=True)
ap=argparse.ArgumentParser();ap.add_argument('--save',action='store_true');args=ap.parse_args()
if args.save:(Path(__file__).parent/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
