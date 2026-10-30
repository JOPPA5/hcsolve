#!/usr/bin/env python3
"""Reviewer's independent Pigpen decoder for hcp-1476.
Glyphs are described by my own reading of the enlarged crops (review/work/*.png):
grid cells by which sides are drawn (t,r,b,l) + dot; X wedges by the side the
vertex points to. Layout: tic-tac-toe grid A/B..Q/R row by row, X grid S/T (top
quadrant, vertex down), U/V (left quadrant, vertex right), W/X (right quadrant,
vertex left), Y/Z (bottom quadrant, vertex up); second letter of each pair = dotted."""
cells = {  # sides drawn -> pair (cell position in the # grid)
 'rb':'AB','lrb':'CD','lb':'EF','trb':'GH','tlrb':'IJ','tlb':'KL','tr':'MN','tlr':'OP','tl':'QR'}
wedges = {'down':'ST','right':'UV','left':'WX','up':'YZ'}
def dec(g):
    kind, shape, dot = g
    pair = cells[shape] if kind=='c' else wedges[shape]
    return pair[dot]
# my reading (position, glyph, note)
line1 = [('c','tr',0),('w','up',0),('c','tlr',0),
         ('w','left',0),   # drawn as '7'-like acute wedge, vertex upper RIGHT; read as W only by context
         ('c','tr',1)]
line2 = [('c','lrb',1),('c','rb',0),('c','tl',1),('c','tlb',1),('c','tlrb',0),('c','tr',1),('c','trb',0),
         ('w','down',0),('w','left',0),('c','lb',0),('c','lb',0),
         ('w','down',1),   # dot obscured by descender loop of cursive 'y' above
         ('c','trb',1),('c','lb',0),('c','rb',0),('c','tl',1),('w','down',1)]
p1=''.join(map(dec,line1)); p2=''.join(map(dec,line2))
print(p1); print(p2); print(len(line1)+len(line2),'glyphs')
# literal alternative for line-1 glyph 4 as drawn (vertex right)
alt=list(line1); alt[3]=('w','right',0); print('literal glyph-4 reading:',''.join(map(dec,alt)))
