# Measure ink blobs of the sign grid on the hi-res address side and test Morse-style size readings.
import sys,itertools
from PIL import Image
import numpy as np
from collections import deque
im=np.array(Image.open(sys.argv[1]).convert('RGB')).astype(int)
x0,y0,x1,y1=150,380,560,790
reg=im[y0:y1,x0:x1]
# the ink is blue-black; the watermark is neutral grey, so demand darkness
ink=reg.sum(2)<300
h,w=ink.shape; seen=np.zeros_like(ink); bl=[]
for y in range(h):
  for x in range(w):
    if ink[y,x] and not seen[y,x]:
      q=deque([(y,x)]);seen[y,x]=1;p=[]
      while q:
        a,b=q.popleft();p.append((a,b))
        for da in(-2,-1,0,1,2):
          for db in(-2,-1,0,1,2):
            c,d=a+da,b+db
            if 0<=c<h and 0<=d<w and ink[c,d] and not seen[c,d]:seen[c,d]=1;q.append((c,d))
      if len(p)>=15:
        ys=[i[0] for i in p];xs=[i[1] for i in p]
        bl.append((min(ys)+y0,min(xs)+x0,max(ys)-min(ys)+1,max(xs)-min(xs)+1,len(p)))
rows=[]
for b in sorted(bl): 
    print('top=%d left=%d h=%d w=%d area=%d'%b)
