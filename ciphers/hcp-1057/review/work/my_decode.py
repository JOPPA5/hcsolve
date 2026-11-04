# Independent reviewer decode of hcp-1057: own reading of the cipher block (reviewer transcription).
import sys, collections
ROWS = ["H1tt2 g291d2 73ch","8 2h 9 d32 z23t 83ch z5 b2-","d17k27, d1 85ßt2","G2f17g272 3ch g623ch","1b h4627",
        "83t 23728 T917sp49t.","B3s z59 St57d2 30t 74ch","16620 b238 16t27.","S27d2 7ä ch0t270","23727 B93f"]
# derive key from pattern words only: einen/einem, beim, alles, nicht? -> build table, then check all
K = {}
def learn(c,p):
    for a,b in zip(c,p):
        if a.isdigit():
            assert K.get(a,b)==b,(a,b,K.get(a)); K[a]=b
learn("23727","einen"); learn("23728","einem"); learn("b238","beim"); learn("16620","alles")
learn("z59","zur"); learn("74ch","noch"); learn("T917sp49t","Transport"); learn("85ßt2","mußte")
print("key:",dict(sorted(K.items())))
n=0
for r in ROWS:
    r=r.replace("8 2h 9","82h9")
    n+=sum(ch.isdigit() for ch in r)
    print(r.ljust(28),"->","".join(K.get(c,c) for c in r))
print("digit signs:",n, "unmapped:",[c for r in ROWS for c in r if c.isdigit() and c not in K])
