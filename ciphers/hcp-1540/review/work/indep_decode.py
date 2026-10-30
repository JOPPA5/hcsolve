"""Independent reviewer decoder: reads the solver's glyph tokens from record.json
but applies the family key from hcp-1545 (not the solver's key.json), and
applies reviewer-verified corrections to show the completed reading."""
import json, sys
root = sys.argv[1]
key = {k.lower(): v.lower() for k, v in json.load(open(root+"/ciphers/hcp-1545/work/key.json")).items()}
key["y"] = "j"; key["h_ch"] = "ch"; key["H"] = "ch"
out = {}
for line in open(sys.argv[2]):
    p = line.rstrip("\n").split("\t")
    if len(p) < 4 or not p[0][:1] in "BM" or "." not in p[0]: continue
    pos, typ, g, lit = p
    row = pos.split(".")[0]
    if typ == "glyph": s = key["H"] if g == "H" else key[g]
    elif typ == "unknown_span": s = "[?]"
    else: s = lit
    out.setdefault(row, []).append((pos, g, s))
mism = 0
for row, toks in out.items():
    print(row, "".join(t[2] if t[2] else " " for t in toks))
