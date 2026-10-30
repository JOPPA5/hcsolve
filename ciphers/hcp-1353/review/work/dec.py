# independent decode: alphabet lookup, no arithmetic reuse from solve.py
A='abcdefghijklmnopqrstuvwxyz'
M={A[i]:A[i-1] for i in range(26)}
for g in "kvtu b mjuumf tvsqsjtf gspn Mpp".split():
    print(g,''.join(M[c] for c in g.lower()))
print(sum(len(g) for g in "kvtu b mjuumf tvsqsjtf gspn Mpp".split()))
