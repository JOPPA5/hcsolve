import sys
from PIL import Image, ImageOps
x0,y0,x1,y1=map(int,sys.argv[1:5]); out=sys.argv[5]; s=float(sys.argv[6]) if len(sys.argv)>6 else 4
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1790/work/hires/rot.png').convert('L')
im=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)),cutoff=0.5)
im.resize((int((x1-x0)*s),int((y1-y0)*s)),Image.BICUBIC).save(out)
