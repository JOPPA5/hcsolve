import glob,sys
from PIL import Image,ImageOps
f=glob.glob('hires/*adr.jpg')[0]
im=Image.open(f).convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
c=im.crop((x0,y0,x1,y1));c=c.resize((c.width*s,c.height*s),Image.BICUBIC);c.save(f'crops/{n}.png')
