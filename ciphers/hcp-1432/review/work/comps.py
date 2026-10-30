import sys
from PIL import Image
src=sys.argv[1]; x0,y0,x1,y1=map(int,sys.argv[2:6]); thr=int(sys.argv[6]) if len(sys.argv)>6 else 120
im=Image.open(src).convert('RGB').rotate(180)
W,H=x1-x0,y1-y0
px=im.load()
mask=[[False]*W for _ in range(H)]
for y in range(H):
  for x in range(W):
    r,g,b=px[x0+x,y0+y]
    L=0.299*r+0.587*g+0.114*b
    if L<thr and b-r>-15: mask[y][x]=True
seen=[[False]*W for _ in range(H)]
comps=[]
for y in range(H):
  for x in range(W):
    if mask[y][x] and not seen[y][x]:
      st=[(x,y)];seen[y][x]=True;pts=[]
      while st:
        a,c=st.pop();pts.append((a,c))
        for dx in(-1,0,1):
          for dy in(-1,0,1):
            nx,ny=a+dx,c+dy
            if 0<=nx<W and 0<=ny<H and mask[ny][nx] and not seen[ny][nx]:
              seen[ny][nx]=True;st.append((nx,ny))
      xs=[p[0] for p in pts];ys=[p[1] for p in pts]
      if len(pts)>=3: comps.append((min(xs)+x0,max(xs)+x0,min(ys)+y0,max(ys)+y0,len(pts)))
comps.sort()
for c in comps:
  w=c[1]-c[0]+1;h=c[3]-c[2]+1
  kind='slash' if h>=12 else ('dash' if w>=7 else 'dot')
  print(f"x{c[0]:4d}-{c[1]:4d} y{c[2]:3d}-{c[3]:3d} w{w:2d} h{h:2d} n{c[4]:3d} {kind}")
