from PIL import Image, ImageEnhance
import glob,sys
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
s=2.1675
def c(n,x0,y0,x1,y1,z=2.2):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=ImageEnhance.Contrast(r).enhance(1.6)
    r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS); r.save('crops/%s.png'%n); print(n,r.size)
rows=[('r0',20,20,400,85),('r0b',380,20,780,85),
('r3a',20,165,410,225),('r3b',390,165,790,225),
('r4a',20,225,410,285),('r4b',390,225,790,285),
('r5a',20,280,410,340),('r5b',390,280,790,340),
('r6a',20,330,410,395),('r6b',390,330,790,395),
('r7a',20,385,410,450),('r7b',390,385,790,450),
('r8a',20,440,410,505),
('o1',30,75,790,175),('o2',30,515,790,700),('o3',30,690,790,850),('o4',30,840,790,1000)]
for r in rows:
    c(*r, z=(1.3 if r[0][0]=='o' else 2.2))
