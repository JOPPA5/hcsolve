import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
c=im.crop((105,300,240,2210)).rotate(90,expand=True)  # width 1910 height 135
c=ImageEnhance.Contrast(c).enhance(1.6)
W=c.width; seg=520; step=480
xs=list(range(0,W-60,step)); sc=1420/seg; H=int(135*sc)
for p in range(0,len(xs),4):
    part=xs[p:p+4]; o=Image.new('RGB',(1420,len(part)*(H+8)),'white')
    for i,x in enumerate(part):
        s=c.crop((x,0,min(W,x+seg),135)); o.paste(s.resize((int(s.width*sc),H),Image.LANCZOS),(0,i*(H+8)))
    o.save(D+f'/crops/Mg{p//4}.png')
print(len(xs))
T={'p1':(1560,1240,2060,1420),'p2':(1000,1260,1560,1440),'p3':(140,1380,700,1540),'p4':(640,1400,1200,1560),
's4':(2760,600,3320,760),'s5':(2760,720,3320,890)}
for k,b in T.items(): crop('V'+k,b,1400/(b[2]-b[0]))
