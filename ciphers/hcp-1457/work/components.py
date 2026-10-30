# Extract ink connected components from the cipher block of the address side.
import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('L')
X0,X1,Y0,Y1=35,415,225,590
px=im.load(); T=int(sys.argv[2]) if len(sys.argv)>2 else 140
seen=set(); comps=[]
for y in range(Y0,Y1):
  for x in range(X0,X1):
    if px[x,y]<T and (x,y) not in seen:
      st=[(x,y)]; seen.add((x,y)); pts=[]
      while st:
        a,b=st.pop(); pts.append((a,b))
        for dx in (-1,0,1):
          for dy in (-1,0,1):
            u,v=a+dx,b+dy
            if X0<=u<X1 and Y0<=v<Y1 and (u,v) not in seen and px[u,v]<T:
              seen.add((u,v)); st.append((u,v))
      if len(pts)>=6:
        xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
        comps.append((min(ys),max(ys),min(xs),max(xs),len(pts)))
comps.sort(key=lambda c:((c[0]+c[1])//2,c[2]))
for c in comps: print(c, 'h=',c[1]-c[0]+1)
