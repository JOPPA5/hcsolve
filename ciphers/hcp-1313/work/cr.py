import sys
from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/crops/'
im=Image.open(W+'enh_full.png')
x0,y0,x1,y1=map(int,sys.argv[2:6]); s=float(sys.argv[6]) if len(sys.argv)>6 else 1
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save(W+sys.argv[1]+'.png')
