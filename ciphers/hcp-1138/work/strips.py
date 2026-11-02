from PIL import Image, ImageEnhance
import os, math
d=os.path.dirname(os.path.abspath(__file__))
r=Image.open(d+'/crops/rot48.png')
L=[(790,415,1480,375),(690,490,1550,450),(630,550,1550,515),(560,605,1600,620),(520,660,1770,710),(440,700,1870,790),(400,745,1900,850),(340,790,1900,885),(290,830,1860,940),(240,880,1800,990),(190,925,1740,1040),(140,970,1170,1120),(350,1110,1300,1210),(270,1180,1200,1250),(240,1225,1070,1300),(290,1280,1310,1360),(345,1350,1020,1450),(380,1410,1120,1500),(440,1475,1100,1550),(560,1550,890,1590)]
S=1.361
Z=3
PW=480 # source px per piece
HH=60
for i,(a,b,c,e) in enumerate(L,1):
    a,b,c,e=[v*S for v in (a,b,c,e)]
    ln=math.hypot(c-a,e-b); ux,uy=(c-a)/ln,(e-b)/ln
    n=0; s=-20
    while s<ln:
        ox=a+ux*s; oy=b+uy*s
        # output (X,Y) -> src
        W=PW*Z; H=2*HH*Z
        t=r.transform((W,H),Image.AFFINE,(ux/Z,-uy/Z,ox+uy*HH,uy/Z,ux/Z,oy-ux*HH),Image.BICUBIC)
        ImageEnhance.Contrast(t).enhance(1.4).save(d+'/crops/L%02d_%d.png'%(i,n))
        n+=1; s+=PW-60
    print(i,n)
