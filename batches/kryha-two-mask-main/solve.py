"""Exact physical two-mask realization of relative displacement differences.

This fits a relation between ciphertexts, not plaintext. Distinct realizations
may exist. Returned physical masks must be language-tested separately.
"""
from pathlib import Path
import json, sys, time
sys.path.insert(0,'/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model

dist=json.loads(Path('batches/kryha-wheel-sol61/wheel52.json').read_text())['adjacent_distances']
coords=[0]
for i in range(103):coords.append(coords[-1]+dist[i%52])

def arcs(holes):
    return [(coords[b if b>a else b+52]-coords[a]) for a,b in zip(holes,holes[1:]+holes[:1])]

def fit(delta, seconds=30):
    n=len(delta); model=cp_model.CpModel(); paths=[]; coordinates=[]
    for side in range(2):
        holes=[model.new_int_var(0,51,f'anchor{side}')]
        for j in range(1,n):holes.append(model.new_int_var(j,103-(n-j),f'h{side}_{j}'))
        holes.append(model.new_int_var(52,103,f'end{side}'))
        model.add(holes[-1]==holes[0]+52)
        for a,b in zip(holes,holes[1:]):model.add(b>a)
        cc=[]
        for j,h in enumerate(holes):
            c=model.new_int_var(0,coords[-1],f'coordinate{side}_{j}')
            model.add_element(h,coords,c);cc.append(c)
        paths.append(holes);coordinates.append(cc)
    for j,value in enumerate(delta):
        quotient=model.new_int_var(-6,6,f'multiple26_{j}')
        model.add(coordinates[1][j+1]-coordinates[1][j]-coordinates[0][j+1]+coordinates[0][j]==value+26*quotient)
    assert not model.validate()
    solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=seconds
    solver.parameters.num_search_workers=4;solver.parameters.random_seed=350351231
    t=time.monotonic();status=solver.solve(model)
    result=dict(status=solver.status_name(status),seconds=time.monotonic()-t,
                delta_mod26=delta,branches=solver.num_branches,conflicts=solver.num_conflicts,
                truth_masks_used=False,known_relation_only=True)
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        masks=[[solver.value(h)%52 for h in path[:-1]] for path in paths]
        aa,bb=map(arcs,masks)
        assert all((b-a)%26==d for a,b,d in zip(aa,bb,delta))
        assert sum(aa)==sum(bb)==179 and all(len(set(h))==n for h in masks)
        result.update(masks=masks,arc_sequences=[aa,bb],independent_arc_checks=True)
    return result
