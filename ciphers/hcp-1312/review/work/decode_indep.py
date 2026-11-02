#!/usr/bin/env python3
"""Reviewer's independent check of hcp-1312. Own sign alphabet and own decoder, typed from the reviewer's
crops (review/work/*.png). Not blind: the solver's reading was known. Row 15 i s (Isten) and i s z o n (viszont)
are typed as the solver's hypothesis and were only tested for compatibility with the pixels, not read. Run: python3 -I review/work/decode_indep.py from the cipher dir."""
import re,unicodedata
K={'=':'a','6':'b','C':'c','E':'c','EC':'cs','/':'d','3':'e','G':'g','Y':'gy','H':'h','P':'p','I':'i','T':'j',
   'S':'k','~':'l','M':'m','N':'n','O':'o','Q':'ö','F':'r',')':'s','L':'t','X':'u','V':'v','Z':'z'}
R="""S 3 / V 3 ) T O ~ = N S = M
F 3 M 3 ~ 3 M H O Y =
S 3 / V 3 6 3 N L = ~ = ~
T = C O F = I M N = ~ X N S
N I N EC ) 3 M M I X T ) = G
H = L Q N S N 3 ~ 3 / 3 ) 3 M
V = ~ = M I X T ) = G M O ) L
M = ) L N 3 M E = S = Z = V 3 F
) 3 L / 3 3 6 3 = ~ 3 G T O 6 6
G O N / O ~ = L = I 6 3 N N 3 V = N
3 N = Z L H I ) Z 3 M 3 / 3 ) S I N EC 3 M
) = Z M = ) S 3 P 3 M I ) ~ 3 H 3 L
H O Y M I N S 3 L = Z X F I ) L 3 N
3 Y M = ) N = S L 3 F 3 M L 3 L
I ) L 3 N V 3 ~ 3 = V I ) Z O N L ~ = L = ) F ="""
mine=[''.join(K[t] for t in r.split()) for r in R.splitlines()]
key2=dict(bars2='=',six='6',lbowl='C',lbowlbar='E',opp='EC',slashd='/',bars3='3',loopg='G',gy='Y',tallH='H',tallP='P',icurve='I',
 invT='T',sect='S',wave='~',st3='M',st2='N',oloop='O',oloopdots='Q',F='F',rbowl=')',gamma='L',xcross='X',chev='V',zcross='Z')
led=[]
for l in open('work/ledger-rev2.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    led.append([key2[t.rstrip('~')] for t in l.split()[1:]])
n=0;d=0
for i,(r,l) in enumerate(zip(R.splitlines(),led),1):
    a=r.split();n+=len(a)
    if a!=l: d+=1;print('DIFF row',i,a,l)
print('rows',len(mine),'signs',n,'rows differing from solver ledger',d)
for i,m in enumerate(mine,1): print(i,m)
lit=''.join(mine)
nz=open('work/normalized-rev2.txt',encoding='utf-8').read().split('Plain')[0].split('normalized:')[1]
nz=''.join(c for c in unicodedata.normalize('NFD',nz.lower()) if c.isalpha())
def strip(s): return unicodedata.normalize('NFC',s)
print('normalized letters (no accents):',nz)
import difflib
lit2=''.join(c for c in unicodedata.normalize('NFD',lit) if c.isalpha())
for op,a,b,c,e in difflib.SequenceMatcher(None,lit2,nz,autojunk=False).get_opcodes():
    if op!='equal': print(op,repr(lit2[a:b]),'->',repr(nz[c:e]),'at',lit2[max(0,a-8):a])
