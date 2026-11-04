"""hcp-1195: decode the runic-style MASC transcription. Run from repo root:
python3 -I ciphers/hcp-1195/work/decode.py"""
import hashlib, json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
HASH = {
 "source/picture-large.jpg": "c4e84f3172fd007660c853be312d81226f6cd112fb2c66b9de7db7368d8128ba",
 "source/address-large.jpg": "b9dba0d7312101ffbb6cc4575aa5577c6f540e760e8d600d460d2c9971a63b96",
 "work/hires/cpc_1900-02-25_AT_Tepi_AT_Wien_schoenfelder-01_pic.jpg": "32992918499e2216c469e2ab46e8c69d2e74f9b663101363fb81514eeae458bd",
 "work/hires/cpc_1900-02-25_AT_Tepi_AT_Wien_schoenfelder-01_adr.jpg": "d3ff202eb2441923368373a81bac87314f06daf3d53626f9366d1e13ba8ca7f6",
}
for p, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    print(("OK   " if got == h else "FAIL ") + p); 
    if got != h: sys.exit(1)
key = json.load(open(os.path.join(D, "key.json")))
# homographs resolved by word sense (the only context-dependent calls)
RESOLVE = {"{F/V}{A/O}RIGE": "VORIGE", "{F/V}ERZIEHEN": "VERZIEHEN", "{F/V}ERNEINDE": "VERNEINDE",
           "S{A/O}NNT{A/O}GS": "SONNTAGS"}
def word(tokens):
    # apply the writer's 2/1 reorder marks
    out = []
    i = 0
    while i < len(tokens):
        if tokens[i].endswith("@2") and i + 1 < len(tokens) and tokens[i+1].endswith("@1"):
            out += [tokens[i+1][:-2], tokens[i][:-2]]; i += 2
        else:
            out.append(tokens[i]); i += 1
    raw = "".join(key[t] for t in out)
    if raw in RESOLVE: return raw, RESOLVE[raw]
    res = raw.replace("{F/V}", "F")
    res = re.sub(r"\{A/O\}", lambda m: "A", res)
    return raw, res
FIX = {"{A/O}NTW{A/O}RT": "ANTWORT", "M{A/O}RGEN": "MORGEN", "{A/O}DER": "ODER", "{F/V}{A/O}LGT": "FOLGT"}
raw_lines, lines = [], []
for ln in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    if ln.startswith("#") or not ln.strip(): continue
    rw, pw = [], []
    for grp in ln.split("/"):
        toks = grp.split(); punct = [t for t in toks if t in (".", "-", "--")]
        toks = [t for t in toks if t not in (".", "-", "--")]
        r, p = word(toks)
        p = FIX.get(r, p) if r in FIX else p
        rw.append(r + "".join(" " + x for x in punct)); pw.append(p + "".join(" " + x for x in punct))
    raw_lines.append(" ".join(rw)); lines.append(" ".join(pw))
print("\n-- raw (homographs in braces) --"); print("\n".join(raw_lines))
print("\n-- plaintext as written --"); print("\n".join(lines))
