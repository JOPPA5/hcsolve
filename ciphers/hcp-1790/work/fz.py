import sys
from PIL import Image
yc=int(sys.argv[1]); tag=sys.argv[2]; h=int(sys.argv[3]) if len(sys.argv)>3 else 32
x0=int(sys.argv[4]) if len(sys.argv)>4 else 180
d=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/hires/flip.png')
for i,x in enumerate(range(x0,1100,240)):
    d.crop((x,yc-h,x+260,yc+h)).resize((260*4,h*8),Image.BICUBIC).save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/crops/{tag}_{i}.png')
