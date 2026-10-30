import sys
from PIL import Image
im=Image.open(sys.argv[1]).rotate(-90,expand=True)
out=sys.argv[2]
ys={'R02':(70,108),'R03':(102,140),'R05':(168,206),'R07':(236,274),'R08':(268,306),'R09':(300,340)}
for n,(a,b) in ys.items():
    for h,(x0,x1) in enumerate([(20,345),(330,660)]):
        c=im.crop((x0,a,x1,b)); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(f'{out}/{n}{"ab"[h]}.png')
