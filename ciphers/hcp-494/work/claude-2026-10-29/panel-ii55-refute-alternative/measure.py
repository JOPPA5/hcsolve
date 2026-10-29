import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from components import read_bmp
from separate import classify
src=sys.argv[1]; w,h,px=read_bmp(src)
print("glyph        box(x0-x1,y0-y1)      brown bbox            height width")
for a in sys.argv[2:]:
    n,x0,x1,y0,y1=a.split(':'); x0,x1,y0,y1=map(int,(x0,x1,y0,y1))
    pts=[(y,x) for y in range(y0,y1+1) for x in range(x0,x1+1) if classify(px[y][x])=='brown']
    if not pts: print(n,'none'); continue
    ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
    # also trimmed extent: rows with >=2 brown px (ignore specks)
    rows=[y for y in range(y0,y1+1) if sum(1 for x in range(x0,x1+1) if classify(px[y][x])=='brown')>=2]
    print("%-12s x%4d-%4d y%3d-%3d   x%4d-%4d y%3d-%3d   h=%3d (rows>=2px: %3d-%3d h=%3d) w=%3d"%(n,x0,x1,y0,y1,min(xs),max(xs),min(ys),max(ys),max(ys)-min(ys)+1,min(rows),max(rows),max(rows)-min(rows)+1,max(xs)-min(xs)+1))
