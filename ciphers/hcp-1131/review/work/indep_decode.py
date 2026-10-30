#!/usr/bin/env python3
"""Reviewer's independent decode of HCP1131 from the reviewer's own collation.
Grid cells numbered as on a phone keypad 1..9 (A..I standard pigpen grid);
a glyph is named by its open sides.  Dots 1/2/3 pick A-I / J-R / S-Z."""
# cell -> which sides of the cell are drawn in the standard # grid
drawn={1:'RB',2:'LRB',3:'LB',4:'TRB',5:'TRBL',6:'TLB',7:'TR',8:'TLR',9:'TL'}
def letter(sides,dots):
    s=set(sides)
    cell=[c for c,d in drawn.items() if set(d)==s][0]
    i=9*(dots-1)+cell-1
    return chr(65+i)
# reviewer's own reading: (sides drawn, dots); '/' word break
rows=[
 "TR3 TBL2 LB3 / LB1 RB1 TRBL2 / TRBL2 TBL2 LRB3",
 "TRBL3 TL2 TL1 LRB3 TRBL1 / RB3 TBL2 / TL1",
 "LB1 RB1 TRBL2 / TL2 TRBL1 RB1 TRB1 / TL1 LRB3",
 "TL1 / TRBL3+ish / TL1 / LB1 TBL2 LB3 LB2 TRB1",
 "TBL1 LB2 TR3 / TLR1 TBL2 TRB2 TRBL1",
 "TRB1 TBL2 / TR3 TBL2 LB3 / TR2 LB2 RB1 TR3",
 "TBL2 TRBL2 / LRB3 TLR1 TRBL1 / TBL2 TL2 TR1 RB1 TRBL2",
 "TL1 / RB1 TRB2 / TR2 TL2 TRBL1* LRB3 LRB3 TR3",   # * two visible dots on scan
 "LRB3 TL1^ TL2 TRBL1 TRB1",                         # ^ inserted above with caret
]
n=0;out=[]
for r in rows:
    words=[]
    for w in r.split('/'):
        s=''
        for t in w.split():
            extra='ish' if t.endswith('+ish') else ''
            t=t.replace('+ish','').rstrip('*^')
            s+=letter(t[:-1],int(t[-1]))+extra; n+=1
        words.append(s)
    out.append(' '.join(words))
print('\n'.join(out)); print(n,'glyphs')
