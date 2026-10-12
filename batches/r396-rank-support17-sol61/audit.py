from run import *
tr=json.loads((b/'control-truth.json').read_text());s,ranks,clauses=build(tr['p'],tr['c']);assumptions=[ranks[st][col][rank]for st,key in enumerate(tr['keys'])for rank,col in enumerate(key)];s.set(timeout=5000);t=time.monotonic();status=s.check(*assumptions);assert status==z3.sat
rng=random.Random(396171763)
for case in range(200):
 key=rng.sample(range(17),17);rank={col:r for r,col in enumerate(key)};short=rank[16];mapping=[3*rank[i%17]-int(short<rank[i%17])+i//17 for i in range(50)];assert sorted(mapping)==list(range(50));p=''.join(chr(97+i%26)for i in range(50));direct=['']*50
 for i,j in enumerate(mapping):direct[j]=p[i]
 assert ''.join(direct)==enc(p,key)and inv(''.join(direct),key)==p
(b/'audit.json').write_text(json.dumps(dict(known_key_fixture_status=str(status),fixture_seconds=time.monotonic()-t,fixture_only_keys_not_blind_input=True,random_position_map_bijection_encoder_inverse_cases=200,seed=396171763),indent=2)+'\n');print('fixture SAT and200independentmap/encoder/inverse cases exact')
