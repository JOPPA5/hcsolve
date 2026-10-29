import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from components import read_bmp
from separate import classify
src=sys.argv[1]; w,h,px=read_bmp(src)
for a in sys.argv[2:]:
    n,x0,x1,y0,y1=a.split(':'); x0,x1,y0,y1=map(int,(x0,x1,y0,y1)); x1=min(x1,w-1); y1=min(y1,h-1)
    print("== %s  crop x%d-%d y%d-%d (2x2 cells; # brown, X black gloss, . paper; row label = crop y)"%(n,x0,x1,y0,y1))
    for y in range(y0,y1,2):
        line=''
        for x in range(x0,x1,2):
            cl=[classify(px[yy][xx]) for yy in (y,y+1) for xx in (x,x+1) if yy<=y1 and xx<=x1]
            line+= 'X' if cl.count('black')>=2 else ('#' if cl.count('brown')>=2 else ('+' if 'brown' in cl else '.'))
        print("%3d %s"%(y,line))
