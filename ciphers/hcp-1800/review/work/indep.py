"""Independent decoder: derives cell outlines from grid position (row, col) of a 3x3 Pigpen grid."""
import sys, collections
def outline(r, c):
    s = set()
    if r > 0: s.add("T")
    if r < 2: s.add("B")
    if c > 0: s.add("Lf")
    if c < 2: s.add("Rt")
    return frozenset(s)
NAMES = {"BR": {"B","Rt"}, "B": {"B","Lf","Rt"}, "BL": {"B","Lf"}, "R": {"T","B","Rt"},
         "C": {"T","B","Lf","Rt"}, "L": {"T","B","Lf"}, "TR": {"T","Rt"}, "T": {"T","Lf","Rt"}, "TL": {"T","Lf"}}
key = {}
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for blk in range(3):
    for i in range(9):
        k = blk*9+i
        if k < 26: key[(outline(i//3, i%3), blk+1)] = alpha[k]
lines = [l for l in open(sys.argv[1]).read().splitlines() if l.strip() and not l.startswith("#")]
cnt = collections.Counter(); n = 0
for l in lines:
    out = []
    for w in l.split("  "):
        if not w.strip(): continue
        s = ""
        for t in w.split():
            t = t.rstrip("?"); sh, num = t[:-1], int(t[-1])
            s += key[(frozenset(NAMES[sh]), num)]; n += 1; cnt[t] += 1
        out.append(s)
    print(" ".join(out))
print("signs:", n, "distinct tokens:", len(cnt))
