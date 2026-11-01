"""Reviewer's independent decode of HCP1262. The rows below were transcribed by the reviewer
from enlarged crops (review/work/crops) as sign classes, before comparison with work/ledger.txt.
Key: class names and letters taken from ciphers/hcp-1216/work/graphic-key.json, read directly.
Letter = class: k section, E three bars, A two bars, D tick-left+stroke, V chevron, S right bowl,
J inverted T, O loop, L wave, N two strokes, M three strokes, B six, H tall+tick-right, G open loop,
Y low descender (always after G here), F cross, R F-like, T gamma, Z long crossed diagonal, I crossed curve,
CS opposed bowls, CC closed bowl, ? compound, ö = O with dots.
Run: python3 -I review/work/independent.py  (from the cipher directory's parent is not required)."""
import json, os, re, difflib
H = os.path.dirname(os.path.abspath(__file__))
key = json.load(open(os.path.join(H, '../../../hcp-1216/work/graphic-key.json')))
M = {'K':key['section-mark'],'E':key['three-bars'],'A':key['two-bars'],'V':key['chevron'],'S':key['right-bowl'],
     'J':key['inverted-T'],'O':key['cursive-loop'],'L':key['wave'],'N':key['two-short-strokes'],'M':key['three-short-strokes'],
     'B':key['six'],'G':key['open-loop-descender'],'Y':key['low-descender'],'F':key['cross'],'R':key['F'],'T':key['gamma'],
     'Z':key['crossed-diagonal'],'I':key['dotted-crossed-curve'],'D':'d','H':'h','CS':'cs','CC':'cs','Q':'ö','?':'?'}
rows = '''K E D V E S J O L A N K A M B E
CS E S S O R A I T M E G K A D T A M
M E J E R T F O G A D J A K Q S Z Q
N E T E M E K E D V E S E M E Z
N E M O J A N T A N CC Z I S K O
L A M I N T J O L A N K A M G O M
D ? J A I D E H O L G Y E K N E M
J A R N A K CS A K F E R F I A K
K E D V E S J O L A N K A M CC A K
N E M K I V A N J A H O G Y A K O R
G O N D O L H A S A K M A G A R A
A M I K O R M A G A K I V A N
J E M I K O R N E K E M N I N CS
O J A N O R A M H O G Y N E G O N
D O L N E K Q N R E E Z E L B E
Z A R O M S O R A I M E N I S K E
R E M H O G Y G O N D O J O N R A M
T I S Z T E L E M A K E V E S M A M A J E T
I S T E N V E L E
A V I S Z O N T
L A T A S R A
H O L N A H
CS O K O L O
S Z A M T A
L A N S Z O R'''.splitlines()
led=[]
for l in open(os.path.join(H,'../../work/ledger.txt'),encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab,*t=l.split()
    led.append((lab,''.join({'6':'b','GY':'gy','CS':'cs','E?':'E?','M?':'M?','OL?':'?','[M]':'','O:diaeresis':'ö'}.get(x,x.lower()) for x in t)))
diff=0; n=0
from collections import Counter
c=Counter()
for r,(lab,lt) in zip(rows,led):
    me=''.join(M[x] for x in r.split()); n+=len(r.split()); c.update(me)
    lt2=lt.replace('E?','e').replace('M?','m')
    flag='' if me==lt2 else '  <-- DIFF ledger: '+lt2
    if flag: diff+=1
    print(f'{lab:>3} {me}{flag}')
print('signs',n,'rows differing',diff); print(sorted(c.items()))
