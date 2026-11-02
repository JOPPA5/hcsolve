import sys,glob
from PIL import Image, ImageOps
im=Image.open(glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1214/work/hires/*adr.jpg')[0]).convert('RGB')
print(im.size)
im.resize((1400,int(1400*im.height/im.width))).save('full.png')
r=im.rotate(-0,expand=False)
# left half tiles
W=1800
for i,(y0,y1) in enumerate([(0,450),(350,800),(700,1150),(1050,1500),(1400,1850),(1750,2210)]):
    c=im.crop((0,y0,W,y1)); c=ImageOps.autocontrast(c,cutoff=0.5); c=c.resize((c.width,c.height)); c.save(f't{i}.png')
