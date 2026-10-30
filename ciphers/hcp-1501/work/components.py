import sys, json
from PIL import Image
im=Image.open(sys.argv[1]).getchannel('R')
W,H=im.size; p=im.load()
T=int(sys.argv[2]) if len(sys.argv)>2 else 125
seen=set(); comps=[]
for y in range(30,650):
  for x in range(30,990):
    if p[x,y]<T and (x,y) not in seen:
      st=[(x,y)]; seen.add((x,y)); pts=[]
      while st:
        a,b=st.pop(); pts.append((a,b))
        for dx in(-1,0,1):
          for dy in(-1,0,1):
            q=(a+dx,b+dy)
            if 0<=q[0]<W and 0<=q[1]<H and q not in seen and p[q]<T:
              seen.add(q); st.append(q)
      xs=[a for a,b in pts]; ys=[b for a,b in pts]
      mn=min(p[q] for q in pts)
      comps.append(dict(mn=mn,x0=min(xs),x1=max(xs),y0=min(ys),y1=max(ys),n=len(pts),cx=sum(xs)/len(xs),cy=sum(ys)/len(ys)))
json.dump(comps,open(sys.argv[3],'w'))
print(len(comps))
