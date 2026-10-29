import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from components import read_bmp
from separate import classify
src=sys.argv[1]; w,h,px=read_bmp(src)
for a in sys.argv[2:]:
    n,x0,x1,y0,y1=a.split(':'); x0,x1,y0,y1=map(int,(x0,x1,y0,y1))
    prof=[sum(1 for x in range(x0,x1+1) if classify(px[y][x])=='brown') for y in range(y0,y1+1)]
    # longest run of rows with >=2 brown px, allowing gaps of <=2 rows
    runs=[];s=None;gap=0
    for i,c in enumerate(prof):
        if c>=2:
            if s is None: s=i
            gap=0; e=i
        elif s is not None:
            gap+=1
            if gap>2: runs.append((s,e)); s=None
    if s is not None: runs.append((s,e))
    best=max(runs,key=lambda r:r[1]-r[0]) if runs else None
    print("%-10s box x%d-%d y%d-%d  main ink run rows %d-%d  HEIGHT=%d   profile:%s"%(n,x0,x1,y0,y1,y0+best[0],y0+best[1],best[1]-best[0]+1,''.join('#' if c>=6 else ('+' if c>=2 else '.') for c in prof)))
