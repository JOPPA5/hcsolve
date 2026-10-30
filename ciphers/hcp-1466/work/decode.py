"""hcp-1466: check source hashes, validate every move as English-draughts
geometry on the standard 1-32 board, print the readable plaintext.
Run from repo root:  python3 -I ciphers/hcp-1466/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {"address-large.jpg": "af3e0c12e39f6d26dd771718a32e5361c6c651fc763aa1ad75015ef8bc39f5a7",
     "picture-large.jpg": "5933195e852a66e5fca8febde68f36676b3e78feb4b93d08273430801959b742"}
for f in H:
    h = hashlib.sha256(open(os.path.join(C, "source", f), "rb").read()).hexdigest()
    print("sha256", f, "OK" if h == H[f] else "MISMATCH " + h); assert h == H[f]
def rc(n):  # square -> (row, col) ; row 0 = squares 1-4 (Black's side)
    r = (n - 1) // 4; i = (n - 1) % 4
    return r, (2 * i + 1 if r % 2 == 0 else 2 * i)
def sq(r, c): return r * 4 + c // 2 + 1
def kind(a, b):
    (r1, c1), (r2, c2) = rc(a), rc(b)
    if abs(r1 - r2) == 1 and abs(c1 - c2) == 1: return "move", None
    if abs(r1 - r2) == 2 and abs(c1 - c2) == 2: return "jump", sq((r1 + r2) // 2, (c1 + c2) // 2)
    return "ILLEGAL", None
ok = True; games = {}
for line in open(os.path.join(D, "transcription.txt")):
    if line.startswith("#") or not line.strip(): continue
    g, h, mv = line.strip().split("|"); games.setdefault(g, []).append((h, mv.split()))
print("\nDear Sir / Replies as follows:")
for g in sorted(games, key=int):
    print(f"\nGame {g}")
    for h, mv in games[g]:
        who = "large ink line" if h == "L" else "small ink line"
        out = []
        for m in mv:
            a, b = map(int, m.split("-")); k, over = kind(a, b)
            if k == "ILLEGAL": ok = False
            side = "White" if b < a else "Black"
            out.append(f"{a}-{b} [{side} {k}{' over '+str(over) if over else ''}]" if k != "move" else f"{a}-{b} [{side}]")
        print(f"  {who}: " + ", ".join(out))
print("\nYours Fraternally? / Yours Faithfully? -- \"Yours F. Fully\" E. P. Dunne")
print("\nALL MOVES GEOMETRICALLY VALID" if ok else "\nGEOMETRY ERROR"); sys.exit(0 if ok else 1)
