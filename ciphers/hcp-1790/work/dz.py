import sys
from PIL import Image
yc=int(sys.argv[1]); tag=sys.argv[2]; h=int(sys.argv[3]) if len(sys.argv)>3 else 30
d=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/hires/desk.png')
for i,x in enumerate(range(80,1130,250)):
    d.crop((x,yc-h,x+270,yc+h)).resize((270*4,h*8),Image.BICUBIC).save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/crops/{tag}_{i}.png')
