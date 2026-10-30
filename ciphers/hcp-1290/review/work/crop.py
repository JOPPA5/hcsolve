import sys
from PIL import Image, ImageEnhance
im=Image.open(sys.argv[1]).convert('RGB')
out=sys.argv[2]
n=0;y=40
while y<2090:
    for i,x in enumerate((80,830)):
        c=im.crop((x,y,x+800,y+250))
        c=ImageEnhance.Contrast(c).enhance(1.6).resize((1800,562),Image.LANCZOS)
        c.save(f'{out}/s{n:02d}{"LR"[i]}.jpg',quality=88)
    n+=1;y+=220
c=im.crop((2650,200,3250,800)).rotate(0)
ImageEnhance.Contrast(c).enhance(1.5).resize((1500,1500),Image.LANCZOS).save(f'{out}/stamp.jpg',quality=88)
print(n)
