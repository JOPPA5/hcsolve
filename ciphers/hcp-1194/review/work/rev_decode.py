# Reviewer's independent decode of hcp-1194. Own sign labels from reviewer crops
# (review/work/seg0-3.png, l4start.png, feilern.png, erwarte2.png, anhaltend.png, sig_start.png).
# Labels: AST=asterisk, X=cross(stem+slant bar), RR=R-shape, DN=down arrow, DD=stem two cross bars,
# DG=diag+stem, LM=Lambda, K1=stem one branch, F2=stem two up-right branches (FH = heavy one),
# GM=Gamma/Pi, BB=B, I=stem, UP=up-arrow both barbs, HK=stem with one top hook right-down,
# FL=stem closed flag, BL=bolt, FK=fork, OV=overwritten sign
KEY = dict(AST='H',X='E',RR='R',DN='Z',DD='D',DG='A',LM='N',K1='K',F2='F',FH='W?',GM='U',
           BB='B',I='I',UP='T',HK='L',FL='G',BL='S',FK='M',OV='[N?]')
LINES = [
 "AST X RR DN . / DD DG LM K1 / F2 GM RR / BB RR I X F2 . / X RR FH DG RR UP X / F2 X I HK X RR LM",
 "DG LM FL X BL DG FL UP X LM .",
 "I LM LM I FL X LM / FL RR GM BL BL / GM . / K1 GM BL BL",
 "BL UP I FK FK GM LM FL / DG LM AST DG HK UP X LM DD .",
 "DD X I OV / RR DG BL DG",
]
from collections import Counter
c = Counter()
for ln in LINES:
    out = ''
    for t in ln.split():
        if t == '/': out += ' '
        elif t == '.': out += '.'
        else: out += KEY[t]; c[t] += 1
    print(out)
print('signs:', sum(c.values()), 'types:', len(c))
