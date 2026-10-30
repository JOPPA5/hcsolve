import sys
from PIL import Image,ImageOps,ImageFilter
# usage crop.py out x0 y0 x1 y1 scale [rot]
out,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
rot=int(sys.argv[7]) if len(sys.argv)>7 else 0
im=Image.open('hires/pc_hcp_27_pic.JPG').convert('RGB').crop((x0,y0,x1,y1))
if rot: im=im.rotate(rot,expand=True)
im=im.resize((im.width*s,im.height*s),Image.LANCZOS)
g=ImageOps.autocontrast(im.convert('L'),cutoff=1)
g.save('crops/'+out,quality=90)
