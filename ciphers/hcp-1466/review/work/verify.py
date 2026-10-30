"""Independent reviewer check for hcp-1466: own transcription (read from review crops),
own board model (8x8 coordinates), checks steps/jumps, side alternation, capture consistency."""
import sys
# reviewer's own reading, in written order per game (large entry then small entry)
G = {1: ["22-18","15-22","25-18","6-10"], 2: ["11-16","24-19","15-24","28-19"],
     3: ["29-25","16-20"], 4: ["12-16","21-17"], 5: ["22-17","1-6"], 6: ["6-10","22-17"],
     7: ["23-16","12-19","22-18","9-14","18-9","5-14"]}
pos = {}
n = 1
for r in range(8):
    for c in range(8):
        if (r + c) % 2 == 1:          # dark squares, square 1 at row 0 col 1
            pos[n] = (r, c); n += 1
inv = {v: k for k, v in pos.items()}
bad = 0
for g, mv in G.items():
    prev_side = None; prev_to = None; out = []
    for m in mv:
        a, b = map(int, m.split("-")); (r1, c1), (r2, c2) = pos[a], pos[b]
        side = "B" if r2 > r1 else "W"
        dr, dc = abs(r2 - r1), abs(c2 - c1)
        if dr == dc == 1: t = "step"; over = None
        elif dr == dc == 2: t = "jump"; over = inv[((r1 + r2)//2, (c1 + c2)//2)]
        else: t = "ILLEGAL"; over = None; bad += 1
        note = ""
        if prev_side == side: note += " SAME-SIDE-TWICE"; bad += 1
        if t == "jump" and prev_to is not None and over != prev_to: note += f" captured {over} != last-moved {prev_to}"; bad += 1
        out.append(f"{m}:{side}:{t}{'/'+str(over) if over else ''}{note}")
        prev_side, prev_to = side, b
    print(g, " ".join(out))
print("problems:", bad); sys.exit(1 if bad else 0)
