from pathlib import Path
import json,random,unicodedata
from scout import connected,independent,decode,encode
b=Path(__file__).resolve().parent;r=b.parents[1];digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'];ns={'digits':digits,'unicodedata':unicodedata};s=(r/'batches/kryha-mask-sol61/prepare.py').read_text();exec(s[s.index('def prep('):s.index('train=r/')],ns);prep=ns['prep'];excluded={prep(s) for s in (r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().strip().split('\n\n')};text=''.join(prep(s) for s in (r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text().strip().split('\n\n') if prep(s) not in excluded);rng=random.Random(5350351);w=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));coords=w['unwrapped_effective_coordinates'];rows=[]
for trial,mode in enumerate(('ordinary','extra','hold-extra','independent-reset','J-extra')):
 P=rng.sample(range(26),26);O=rng.sample(range(26),26);h=sorted(rng.sample(range(52),23));start=rng.randrange(23);h=h[start:]+h[:start];k=dict(P=P,O=O,holes=h,adjacent_distances=w['adjacent_distances']);phase=rng.randrange(23);offset=rng.randrange(26);pt=text[44000+100*trial:44005+100*trial] if mode!='J-extra' else 'ujefj';presses=[1]*5 if mode in ('ordinary','independent-reset') else [rng.choice([1,2] if mode=='extra' else [0,1,2]) for _ in range(5)] if mode!='J-extra' else [1+(c=='j') for c in pt]
 # Independent absolute hole coordinates; counts machine presses, not letters.
 hh=h[phase:]+h[:phase];base=coords[hh[0]];ip={x:i for i,x in enumerate(P)};io={x:i for i,x in enumerate(O)};steps=0;ct=''
 for letter,p in zip(pt,presses):
  hole=hh[steps%23];D=offset+coords[hole]-base+(179 if hole<hh[0] else 0)+179*(steps//23);ct+=chr(97+io[(ip[ord(letter)-97]+D)%26]);steps+=p
 hole=hh[steps%23];end=((phase+steps)%23,(offset+coords[hole]-base+(179 if hole<hh[0] else 0)+179*(steps//23))%26)
 assert encode(pt,k,phase,offset,presses)==(ct,end);assert decode(ct,k,phase,offset,presses)[0]==pt
 if mode=='independent-reset':candidates=independent(ct,k)
 else:candidates=connected(ct,k,end,[1] if mode=='ordinary' else [0,1,2] if mode=='hold-extra' else [1,2])
 if mode=='J-extra':candidates=[x for x in candidates if x['J_selective_extra']]
 matches=[x for x in candidates if x['plaintext']==pt and x['start_phase']==phase and x['start_displacement']==offset and list(x['presses'])==presses];assert matches
 rows.append(dict(mode=mode,synthetic_exception_control=mode=='J-extra',genuine_TEST_offset=None if mode=='J-extra' else 44000+100*trial,TRAIN_excluded=mode!='J-extra',seed=5350351,plaintext=pt,ciphertext=ct,key=k,planted_start=[phase,offset],presses=presses,endpoint=end,candidate_count=len(candidates),unique_plaintexts=len({x['plaintext'] for x in candidates}),planted_start_and_full_prefix_recovered=True,truth_used_by_enumerator=False,independent_absolute_encoder_check=True))
(b/'controls.json').write_text(json.dumps(rows,indent=2)+'\n');print([(x['mode'],x['candidate_count'],x['unique_plaintexts']) for x in rows])
