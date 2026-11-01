"""Reviewer's independent decode. Rows below are MY shape readings from review/work crops,
entered as shape names, decoded through a map taken from ../hcp-1216/work/graphic-key.json
(not from the solver's decode.py), with h on this card = tall+short (the family's h/p shape)
and d = short+long. Run from ciphers/hcp-1274: python3 -I review/work/verify.py"""
import json,collections,re
fam=json.load(open('../hcp-1216/work/graphic-key.json'))
A={'=':'two-bars','E':'three-bars','K':'section-mark','W':'wave','M':'three-short-strokes','N':'two-short-strokes',
   'O':'cursive-loop','R':'F','S':'right-bowl','T':'gamma','X':'x','V':'chevron','I':'dotted-crossed-curve',
   'J':'inverted-T','Z':'crossed-diagonal','G':'open-loop-descender','B':'six','f':'cross'}
K={c:fam[n] for c,n in A.items()}
K.update({'D':'d','H':'h','Y':'y','Q':'gy','C':'cs','P':'ny','L':'ly','?':'{a/e}'})   # D short+long, H long+short, Q gy, C cs, P ny, L ly
ROWS="""K E D V E S J O W = N K = M
S = J N = W = # T T = W K E W T X
D = T N O M H O Q = V I S Z O N T
W = T = S O" R O" M E I T K E P
T E W E N V = Q O K E Q H E T
T E W O D = B H = S Z T = N I
E D E S E M M O S T C I N = W X N K
= R O" f O" S K E S K E R E S K E D O"
N E K B E R E N D E Z E S T E S M =
K E W E T V O W N = K E S Z W E N
N I E M I = T V = Q O K K E P
T E W E N E W # H = W = S Z T =
N I = Z T = B O W D O G S = G O T
M E L E T O W D = W = M E W
W E E W V E Z H E T T E M V O W
N = M X W = S S O N J O W E D E
S E M E S G O W J O" R = M = K I
M E G = K O R D O G O Z I K M I K O T
S E T = W N I K E W E N ?
I S T E N V E W E E D E S E M
X" D V O" Z O" W V E = T = V O W
B O W""".split('\n')
mine=[]
for r in ROWS:
    s=''
    for t in r.split():
        if t=='#': s+='[x]'
        elif t.endswith('"'):
            b=K[t[0]]; s+={'o':'ö','u':'ü'}[b]
        else: s+=K[t]
    mine.append(s)
sol=[]
import unicodedata
for l in open('work/ledger.txt',encoding='utf-8'):
    if not l.strip() or l[0]=='#': continue
    s=''
    for t in l.split()[1:]:
        b,_,a=t.partition(':')
        if b=='[X]': s+='[x]';continue
        s+={'d':{'O':'ö','U':'ü'}.get(b,b.lower()),'':b.lower(),'a':b.lower()}[a]
    sol.append(s)
assert len(mine)==len(sol)==22
d=0
for i,(m,s) in enumerate(zip(mine,sol),1):
    flag='' if m==s else '  <-- differs: solver '+s
    d+=bool(flag); print(f'{i:02d} {m}{flag}')
print('rows differing:',d)
toks=[t.split(':')[0] for l in open('work/ledger.txt',encoding='utf-8') if l.strip() and l[0]!='#' for t in l.split()[1:]]
print('signs:',len(toks),'struck:',toks.count('[X]'))
print(sorted(collections.Counter(toks).items(),key=lambda x:-x[1]))
