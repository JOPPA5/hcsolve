# Independent check, reviewer (Claude Opus 5.5), hcp-1489. Own reading of address-large.jpg.
import random
L=["SDEOLAREUNANVOSTILAR","UGIVWIOTUTHVIXLOVAIESS","RANDLIBESTOVIWIROSHDLESOI",
   "VFXOLRZYO2VUREUBJPIRTHUS","ODPARYYYFOGROQLMIARN","WYLYONNUUVROSPIOUTWTOFE","WRIORBBKIR"]
S="".join(L)
def sub(s,p,start=0):
    pos=[];i=start
    for ch in p:
        i=s.find(ch,i)
        if i<0: return None
        pos.append(i);i+=1
    return pos
def minwin(s,p):
    best=None
    for st in range(len(s)):
        if s[st]!=p[0]: continue
        q=sub(s,p,st)
        if q is None: break
        w=q[-1]-q[0]+1
        best=w if best is None or w<best else best
    return best
PT="DEARNANWITHLOVEANDBESTWISHESFORYOURBIRTHDAYFROMYOUR"
pos=sub(S,PT)
print(len(S),"signs; plaintext found greedily:",pos is not None, "last pos",pos[-1])
print("".join(c if i in set(pos) else c.lower() for i,c in enumerate(S)))
print("tail after last signal:",S[pos[-1]+1:])
for p in ["DEAR","NAN","DEAREST","WITHLOVEANDBESTWISHESFORYOURBIRTHDAY","FROMYOUR","YOURSTRULY","LOVINGLY","XXX"]:
    print(p,"window on card:",minwin(S,p))
random.seed(1)
for p,w in [("WITHLOVEANDBESTWISHESFORYOURBIRTHDAY",73),("FROMYOUR",23),("DEAREST",15)]:
    hits=0
    for _ in range(1000):
        t=list(S);random.shuffle(t);t="".join(t)
        m=minwin(t,p)
        if m is not None and m<=w: hits+=1
    print(p,"random shuffles with window <=",w,":",hits,"/1000")
