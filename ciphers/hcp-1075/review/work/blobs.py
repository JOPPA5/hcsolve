import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert("L"); s=3468/1024
x0,y0,x1,y1=[int(float(v)*s) for v in sys.argv[2:6]]
c=im.crop((x0,y0,x1,y1)); W,H=c.size; px=c.load()
thr=int(sys.argv[6]) if len(sys.argv)>6 else 120
seen=set(); out=[]
for x in range(W):
  for y in range(H):
    if px[x,y]<thr and (x,y) not in seen:
      st=[(x,y)]; seen.add((x,y)); pts=[]
      while st:
        a,b=st.pop(); pts.append((a,b))
        for da in (-1,0,1):
          for db in (-1,0,1):
            u,v=a+da,b+db
            if 0<=u<W and 0<=v<H and (u,v) not in seen and px[u,v]<thr:
              seen.add((u,v)); st.append((u,v))
      if len(pts)>15:
        xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
        out.append((min(xs)+x0,max(xs)-min(xs)+1,sum(ys)/len(ys)+y0,len(pts),min(px[p] for p in pts)))
for o in sorted(out): print("x=%d w=%d ycen=%.0f n=%d min=%d"%o)
