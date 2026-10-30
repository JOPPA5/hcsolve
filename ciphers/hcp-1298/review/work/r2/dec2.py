# Independent decoder round 2: own table typed by reviewer, no key.json; parses ledger only as a token stream.
import sys
T=dict(zip("2BAR 3BAR SIX LBOWL LRBOWL TICKSTROKE CROSS SHOOK GYLOOP HP DOTLOOP INVT SECTION WAVE 3STROKE 2STROKE LOOP FSIGN RBOWL GAMMA XCROSS CHEVRON TAILX".split(),
"a e b c cs d f g gy H i j k l m n o r s t u v z".split()))
T['XCROSS::']='ű'
n=0;unk={}
for l in open(sys.argv[1],encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    p=l.split();o=''
    for t in p[1:]:
        n+=1
        b=t.rstrip('?')
        if b in T:o+=T[b]
        elif b.isdigit():o+=b
        elif b[0]=='[':o+='.';unk[b]=unk.get(b,0)+1
        else: o+='#';unk[b]=unk.get(b,0)+1
    print(p[0],o)
print(n,unk,file=sys.stderr)
