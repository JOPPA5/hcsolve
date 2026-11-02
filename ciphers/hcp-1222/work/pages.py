import sys
from PIL import Image, ImageDraw
d=sys.argv[1]
groups=[(i,min(i+3,21)) for i in range(1,22,4)]
for a,b in groups:
  for j in range(3):
    ims=[Image.open(f'{d}/r{i:02d}_{j}.png') for i in range(a,b+1)]
    ims=[m.resize((int(m.width*.8),int(m.height*.8))) for m in ims]
    W=max(m.width for m in ims);H=sum(m.height+22 for m in ims)
    p=Image.new('RGB',(W,H),'white');dr=ImageDraw.Draw(p);y=0
    for i,m in zip(range(a,b+1),ims):
        dr.text((5,y+4),f'row {i} col {j}',fill='red');y+=22;p.paste(m,(0,y));y+=m.height
    p.save(f'{d}/p{a:02d}_{j}.png')
