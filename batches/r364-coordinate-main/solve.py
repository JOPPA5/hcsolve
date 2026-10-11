"""Known-plaintext triple columnar search through letter occurrence trajectories.

No intermediate character arrays or planted key hints are used. Each source
position passes through full physical column permutations. Repeated letters
have unrestricted matching to any observed occurrence of that same letter.
"""
import sys, time
from collections import Counter
sys.path.insert(0, '/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model


def encode(text, key):
    return ''.join(text[col::len(key)] for col in key)


def solve(plain, cipher, widths, alignments=None, seconds=60):
    assert len(plain) == len(cipher) and '?' not in plain
    assert Counter(plain) == Counter(cipher)
    n = len(plain)
    model = cp_model.CpModel()
    starts = []
    for j, w in enumerate(widths):
        q, r = divmod(n, w)
        assert q > 0
        ss, intervals = [], []
        for col in range(w):
            length = q + (col < r)
            possible = set()
            for before in range(w):
                lo_count = r - (col < r)
                short_count = w-r-(col >= r)
                for lo in range(max(0, before-short_count), min(before, lo_count)+1):
                    if q*before+lo+length <= n:
                        possible.add(q*before+lo)
            s = model.new_int_var_from_domain(cp_model.Domain.from_values(sorted(possible)), f's{j}_{col}')
            ss.append(s)
            intervals.append(model.new_interval_var(s, length, s+length, f'iv{j}_{col}'))
        model.add_no_overlap(intervals)
        if alignments:
            before = []
            for col in range(1, w):
                b = model.new_bool_var(f'b{j}_{col}')
                model.add(ss[col] < ss[0]).only_enforce_if(b)
                model.add(ss[col] > ss[0]).only_enforce_if(b.Not())
                before.append(b)
            model.add(sum(before) == alignments[j]-1)
        starts.append(ss)
    positions = [list(range(n))]
    for j in range(1, len(widths)):
        positions.append([model.new_int_var(0, n-1, f'pos{j}_{i}') for i in range(n)])
    final = []
    for i, c in enumerate(plain):
        allowed = [k for k, x in enumerate(cipher) if x == c]
        final.append(model.new_int_var_from_domain(cp_model.Domain.from_values(allowed), f'end{i}'))
    positions.append(final)
    for level in positions[1:]:
        model.add_all_different(level)
    for j, w in enumerate(widths):
        for i in range(n):
            src, dst = positions[j][i], positions[j+1][i]
            if isinstance(src, int):
                model.add(dst == starts[j][src % w] + src // w)
            else:
                col = model.new_int_var(0, w-1, f'col{j}_{i}')
                row = model.new_int_var(0, (n-1)//w, f'row{j}_{i}')
                start = model.new_int_var(0, n-1, f'chunk{j}_{i}')
                model.add_allowed_assignments([src, col, row], [(k, k % w, k // w) for k in range(n)])
                model.add_element(col, starts[j], start)
                model.add(dst == start + row)
    assert not model.validate()
    engine = cp_model.CpSolver()
    engine.parameters.max_time_in_seconds = seconds
    engine.parameters.num_search_workers = 4
    engine.parameters.random_seed = 364625
    t = time.monotonic()
    status = engine.solve(model)
    result = dict(status=engine.status_name(status), seconds=time.monotonic()-t,
                  widths=widths, alignments=alignments, branches=engine.num_branches,
                  conflicts=engine.num_conflicts, truth_keys_used=False)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        keys = [sorted(range(w), key=lambda c: engine.value(ss[c])) for w, ss in zip(widths, starts)]
        predicted = plain
        for key in keys:
            predicted = encode(predicted, key)
        assert predicted == cipher
        if alignments:
            assert all(key.index(0)+1 == a for key, a in zip(keys, alignments))
        for i in range(n):
            pos = i
            for w, key in zip(widths, keys):
                col, row = pos % w, pos // w
                pos = sum(len(range(k, n, w)) for k in key[:key.index(col)]) + row
            assert pos == engine.value(final[i]) and cipher[pos] == plain[i]
        result.update(keys=keys, whole_reencrypt_exact=True, all_position_trajectories_verified=True)
    return result
