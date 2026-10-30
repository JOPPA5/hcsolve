# Independent reviewer decoder: reads work/transcription.json rows, applies family key
# (sister key hcp-1545/work/key.json, with H = CH, y = J), leaves {..} uncertainty tags.
import json, re, sys
base = sys.argv[1]
key = {"1":"Y","2":"U","3":"O","4":"I","5":"E","6":"A","7":"J","y":"J","8":"L","b":"P","c":"S","d":"T",
       "f":"V","g":"K","h":"R","m":"N","n":"M","p":"B","q":"Z","r":"H","s":"C","t":"D","H":"CH"}
T = json.load(open(base + "/work/transcription.json"))
unk = set()
out = []
for r in T["rows"]:
    s = ""
    for tok in re.split(r"(\{[^}]*\})", r["cipher"]):
        if tok.startswith("{"):
            s += "[" + tok[1:-1] + "]"; continue
        for ch in tok:
            if ch in key: s += key[ch]
            elif ch.isalnum(): s += "?"; unk.add(ch)
            else: s += ch
    out.append(s)
print("\n".join(out))
print("UNMAPPED:", unk, file=sys.stderr)
