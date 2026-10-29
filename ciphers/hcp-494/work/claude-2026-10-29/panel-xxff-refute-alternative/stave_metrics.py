"""Stave extents and spacing from BMP crops (plain Python). Prints, for the two
heaviest near-vertical staves: their column ranges, ink row extents, height,
centre-to-centre distance, and distance/height ratio. Also checks whether any
row has continuous ink between the staves."""
import sys, struct
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(sys.argv[0])))
from inkgap import read_bmp
def metrics(path, thr, frac=0.55, xlo=None, xhi=None):
    w,h,g = read_bmp(path)
    xlo = 0 if xlo is None else xlo; xhi = w if xhi is None else xhi
    ink=[[g[y][x]<thr for x in range(w)] for y in range(h)]
    col=[sum(ink[y][x] for y in range(h)) if xlo<=x<xhi else 0 for x in range(w)]
    mx=max(col); runs=[]; cur=None
    for x in range(w):
        if col[x]>=frac*mx: cur=[x,x] if cur is None else [cur[0],x]
        elif cur: runs.append(tuple(cur)); cur=None
    if cur: runs.append(tuple(cur))
    runs=sorted(runs,key=lambda r:-sum(col[r[0]:r[1]+1]))[:2]; runs.sort()
    out=[]
    for a,b in runs:
        rows=[y for y in range(h) if any(ink[y][x] for x in range(a,b+1))]
        out.append((a,b,min(rows),max(rows)))
    print(path.split('/')[-1], 'thr',thr)
    for a,b,y0,y1 in out: print(f'  stave cols {a}-{b} (w {b-a+1}), rows {y0}-{y1}, height {y1-y0+1}')
    if len(out)==2:
        c1=(out[0][0]+out[0][1])/2; c2=(out[1][0]+out[1][1])/2
        hgt=max(out[0][3]-out[0][2], out[1][3]-out[1][2])+1
        gap=out[1][0]-out[0][1]-1
        span=[y for y in range(h) if all(ink[y][x] for x in range(out[0][1]+1,out[1][0]))]
        print(f'  centre distance {c2-c1:.0f}px, clear gap {gap}px, taller stave {hgt}px, distance/height {(c2-c1)/hgt:.2f}, gap/height {gap/hgt:.2f}')
        print(f'  rows with continuous ink across gap: {span or "NONE"}')
if __name__=='__main__':
    args=sys.argv[1:]
    metrics(args[0], int(args[1]), xlo=int(args[2]) if len(args)>2 else None, xhi=int(args[3]) if len(args)>3 else None)
