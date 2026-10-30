"""Reviewer's independent decode of hcp-1513. My own glyph transcription (read from my crops in review/work/),
my own sign->letter table derived from ANNA/DEAR crib. Run: python3 -I review/work/indep.py (from cipher dir or anywhere)."""
import json, os, collections
# glyph codes (reviewer's own): 8=D x=E(Ж) +=A R=LП N=◪ Q=□ o=O T=⧗ Y=∩ U=barred-Z C=Ↄ 5=S h=Δ k=÷ 1=I W=⊗ P=日 G=Γ m=Λ b=− v=V f=Φ
K = dict(zip("8x+RNQoTYUC5hk1WPGmbvf", "DEAGNGOTYUCSHKIWPFMBLV"))
K['R']='R'; K['Q']='G'; K['+']='A'
TXT = """8x+R +NN+ / QoT YoUR C+R8 / 5+TUR8+Y Th+Nk YoU / 1 WxNT UP To +5ToR1+ /
5+TUR8+Y +GTxRNooN / +N8 GRom ThxRx WxNT / homx QoT b+Ck hxRx +T 2 P m /
Yx5TxR8+Y +N8 +GTxR Th+T / 1 WxNT 8oWN To Thx v+kx To W+TCh b+vv Q+mx /
1 8Rx+mT +boUT YoU v+5T N1QhT W1Th vofx +NToN"""
out=[]
for w in TXT.split():
    out.append("/" if w=="/" else ("2" if w=="2" else "".join(K[c] for c in w)))
s=" ".join(out); print(s)
sol=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../work/key.json")).read()
k=json.loads(sol); k.pop("_comment")
vals=list(k.values()); print("solver key bijective:", len(vals)==len(set(vals)), len(vals),"signs")
cnt=collections.Counter(c for c in TXT if c not in " /2"); print(sorted(cnt)); print("sign tokens:",sum(cnt.values()),"distinct:",len(cnt))
