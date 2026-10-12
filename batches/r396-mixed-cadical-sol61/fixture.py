from run import *
# Separate correctness fixture only; these assumptions are never passed to calibration.
tr=json.loads((b/'control-truth.json').read_text());inp=json.loads((b/'control-input.json').read_text());names=json.loads((b/'control-names.json').read_text());formula=CNF(from_file=str(b/'control.cnf'));assumptions=[names[f'n{tr["n"]-1}']]
for st,key in enumerate(tr['keys']):
 q,r=divmod(len(inp['p']),len(key));at=0
 for col in key:assumptions.append(names[f'A{st}_{col}_{at}']);at+=q+(col<r)
assumptions.append(names[f'E{tr["injected_F_P_position1"]-1}'])
with Solver(name='cadical195',bootstrap_with=formula.clauses)as s:
 t=time.monotonic();status=s.solve(assumptions=assumptions);assert status;r=witness(s.get_model(),names,inp['p'],inp['raw'],[21,19,20],False);r.update(known_key_fixture_only=True,not_blind_recovery=True,seconds=time.monotonic()-t);(b/'known-key-fixture.json').write_text(json.dumps(r,indent=2)+'\n');print('separate fixture full50SAT',r['seconds'])
