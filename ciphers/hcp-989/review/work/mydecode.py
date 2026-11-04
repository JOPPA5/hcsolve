"""Reviewer's independent decode of hcp-989 line 3 using the hcp-1194/1195 sign values (own transcription)."""
# own reading of the 14 signs + 2 stops, from review/work/w1.png, w2.png, s4to9.png, s7to9.png, w2b.png
signs = ["A-diag","B-tail","fehu","cross","hook","fehu","cross","dash/stem","lambda",".",
         "bolt","arrow","gamma-hook","B-tail","cross","."]
key = {"A-diag":"A","B-tail":"B","fehu":"F","cross":"E","hook":"L","dash/stem":"I","lambda":"N",
       "bolt":"S","arrow":"T","gamma-hook":"U",".":". "}
raw = "".join(key[s] for s in signs)
print("literal sister-key output:", raw)
print("with B->P (word sense, pos 2) and F->W (word sense, pos 6):",
      raw[:1]+"P"+raw[2:5]+"W"+raw[6:])
