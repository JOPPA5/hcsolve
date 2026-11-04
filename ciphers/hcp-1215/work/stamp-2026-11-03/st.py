import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
out=sys.argv[2]
S=3445/1400
def c(n,x0,y0,x1,y1,z):
    b=[int(v*S) for v in (x0,y0,x1,y1)]
    r=im.crop(b); r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r.save(f'{out}/{n}.png')
    g=r.split()[1]; g.save(f'{out}/{n}_g.png')
c('box',1060,75,1270,295,2)
rows=[(88,115),(115,142),(142,170),(170,198),(198,225),(225,252),(250,280)]
for i,(a,b) in enumerate(rows,1):
    c(f'row{i}',1070,a,1260,b,4)
