# Independent reviewer decoder for HCP 1512. Key typed from the table in SOLUTION.md
# plus the reviewer's addition 8=P; '%' marks the Phi-shaped variant read as A.
import sys
glyph = "P I c 2 R 3 S 4 T 5 6 V N W Q Y 0 Z A B J E 8 %".split()
plain = "A B C D E F G H I J L M N O R S T U V W Y Z P A".split()
key = dict(zip(glyph, plain))
punct = set(" .,'")
text = open(sys.argv[1]).read().rstrip("\n").split("\n")
n = 0; unk = set(); used = set()
for line in text:
    out = []
    for ch in line:
        if ch in punct: out.append(ch); continue
        if ch not in key: unk.add(ch); out.append("?"); continue
        out.append(key[ch]); n += 1; used.add(ch)
    print("".join(out))
inv = {}
for g, p in key.items():
    inv.setdefault(p, []).append(g)
print(f"# positions={n} glyph types used={len(used)} unknown={sorted(unk)}")
print("# plain letters with >1 glyph:", {p: g for p, g in inv.items() if len(g) > 1})
