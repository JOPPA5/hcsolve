"""Test A1Z26 numeric reading (direct/reversed, all 26 shifts) on the
numeric groups of HCP1455 as transcribed 2026-10-30 (Claude Opus 5.5).
None yields English beyond the trivial 24 24 24 -> XXX at shift 0."""
seqs = {"L1 (m3=13)": [24,24,24,20,13,2,3], "L1 (m3=23)": [24,24,24,20,23,2,3],
        "L2": [9,5,4,23], "sig": [7,4,4,3,4], "L3": [7]}
for k in range(26):
    d = " | ".join("".join(chr(65+(n-1+k)%26) for n in s) for s in seqs.values())
    r = " | ".join("".join(chr(90-(n-1+k)%26) for n in s) for s in seqs.values())
    print(f"{k:2d} {d}   rev: {r}")
