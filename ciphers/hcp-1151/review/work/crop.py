import sys,glob
from PIL import Image
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1151/'
im=Image.open(glob.glob(base+'work/hires/*_adr.jpg')[0]).convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
r=im.crop((x0,y0,x1,y1)); r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS); r.save(base+'review/work/crops/%s.png'%n)
