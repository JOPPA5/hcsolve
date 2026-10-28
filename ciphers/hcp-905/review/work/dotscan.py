"""Screen every solver glyph for an interior dot: count dark pixels in the central part of its bbox.
Reads the solver's transcript only for coordinates/claimed shapes (comparison), and gray.raw made by ffmpeg."""
import json, sys
W,H=1024,680
g=open(sys.argv[2],'rb').read()
d=json.load(open(sys.argv[1]))
def px(x,y): return g[y*W+x]
out=[]
for r in d['rows']:
  for w in r['words']:
    for gl in w['glyphs']:
      if gl['status']!='active': continue
      sh=gl['shape']
      if sh in ('I','V','LT','UP','UP.','SEum','Vum'): continue
      x0,y0,x1,y1=gl['bbox']; cx,cy=gl['center']
      # central window 10x10 around center
      dark=sum(1 for y in range(cy-5,cy+6) for x in range(cx-5,cx+6) if px(x,y)<110)
      out.append((gl['id'],w['notation'],sh,dark))
for i,n,s,dk in out:
  dotted=s.endswith('.')
  flag=''
  if dotted and dk<2: flag='<-- claimed dot, center empty'
  if not dotted and dk>=3: flag='<-- claimed undotted, center dark'
  if flag: print(i,n,s,dk,flag)
