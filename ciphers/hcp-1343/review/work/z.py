from PIL import Image, ImageOps
import sys
im=Image.open('work/hires/pc_hcp_24_adr.JPG').convert('L')
def c(n,b,z=6):
    r=ImageOps.autocontrast(im.crop(b),cutoff=0.5); r.resize((r.width*z,r.height*z),Image.LANCZOS).save('review/work/%s.png'%n)
# coordinates in the 1785 frame; card 1024 preview -> ×1.743
f=1785/1024
def d(n,x0,y0,x1,y1,z=6): c(n,tuple(int(v*f) for v in (x0,y0,x1,y1)),z)
d('zF',30,592,240,622,6)
d('zF2',140,592,240,622,12)
d('zNO',30,592,110,622,12)
d('zH',380,350,450,385,10)
d('zH2',30,440,240,470,6)
d('zN',170,455,330,490,8)
d('zD',40,232,130,250,12)
d('zR',40,440,120,470,12)
d('zT5',30,125,420,165,5)
d('zT5R',420,145,750,175,5)
d('zT6',440,160,560,185,8)
r=im.crop((int(450*f),int(205*f),int(482*f),int(640*f))).rotate(-90,expand=True)
r=ImageOps.autocontrast(r,cutoff=0.5)
for i in range(2):
    w=r.width//2+30; x=i*(r.width//2-30)
    q=r.crop((x,0,x+w,r.height)); q.resize((q.width*5//2,q.height*5//2),Image.LANCZOS).save('review/work/zS%d.png'%i)
d('zCARD',440,110,640,155,7)
