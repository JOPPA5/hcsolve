# Independent decoder: own key table typed from the family key (hcp-1527), applied to transcription.json cipher strings.
import json, sys, pathlib
d = pathlib.Path(sys.argv[1])
KEY = dict(zip("12345678bcdfghmnpqrst", "YUOIEAJLPSTVKRNMBZHCD")); KEY["ř"]="CH"
fam = json.load(open(sys.argv[2])) if len(sys.argv)>2 else None
if fam: print("family key equal:", fam == KEY)
tr = json.load(open(d/"transcription.json"))
out=[]; n=0; unk=[]
for r in tr["rows"]:
    s=r["cipher"].replace("{U01}","\x00"); o=""
    for ch in s:
        if ch=="\x00": o+="[U01]"
        elif ch in KEY: o+=KEY[ch]; n+=1
        elif ch.isalnum(): unk.append((r["id"],ch)); o+="?"
        else: o+=ch
    print(f'{r["id"]}: {o}', "" if o==r["plaintext"] else "  MISMATCH vs "+r["plaintext"])
    out.append(o)
print("units:",n,"unmapped:",unk)
saved=(d/"plaintext.txt").read_text().strip().split("\n")
print("matches plaintext.txt:", saved==out)
