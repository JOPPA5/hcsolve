from PIL import Image, ImageOps
import numpy as np
from collections import deque
a=Image.open('ciphers/hcp-1331/work/hires/pc_hcp_12_adr.JPG').convert('L').rotate(90,expand=True)
S=1785/1600
A=np.array(a)
for name,(x0,y0,x1,y1) in {'l1':(270,985,720,1030),'l3':(270,1110,970,1190),'l4':(260,1205,970,1265)}.items():
    x0,y0,x1,y1=[int(v*S) for v in (x0,y0,x1,y1)]
    m=A[y0:y1,x0:x1]<110
    seen=np.zeros(m.shape,bool);r=[]
    for i,j in zip(*np.nonzero(m)):
        if seen[i,j]: continue
        q=deque([(i,j)]);seen[i,j]=1;c=[]
        while q:
            u,v=q.popleft();c.append((u,v))
            for du in(-1,0,1):
                for dv in(-1,0,1):
                    p,s=u+du,v+dv
                    if 0<=p<m.shape[0] and 0<=s<m.shape[1] and m[p,s] and not seen[p,s]: seen[p,s]=1;q.append((p,s))
        ys,xs=zip(*c); r.append((min(xs)+x0,min(ys)+y0,len(c),max(xs)-min(xs)+1,max(ys)-min(ys)+1))
    print(name,[b for b in sorted(r) if b[2]>=6])
# hook descender enhancement
o=Image.open('ciphers/hcp-1331/work/hires/pc_hcp_12_adr.JPG').convert('RGB').rotate(90,expand=True)
c=o.crop((int(470*S),int(1205*S),int(560*S),int(1280*S))).convert('L')
c=ImageOps.autocontrast(c,cutoff=1).resize((c.width*12,c.height*12),Image.BICUBIC); c.save('ciphers/hcp-1331/review/work/hook_tail.png')
d=o.crop((int(380*S),int(1215*S),int(580*S),int(1290*S)))
import PIL.ImageEnhance as E
d=E.Contrast(d).enhance(3).resize((d.width*7,d.height*7),Image.BICUBIC); d.save('ciphers/hcp-1331/review/work/hook_tail2.png')
