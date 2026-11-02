import sys,glob
from PIL import Image,ImageOps
f=glob.glob('hires/*_%s.jpg'%sys.argv[1])[0]
x0,y0,x1,y1=map(int,sys.argv[2:6]);s=float(sys.argv[6]);o=sys.argv[7]
rot=int(sys.argv[8]) if len(sys.argv)>8 else 0
im=Image.open(f).convert('RGB').crop((x0,y0,x1,y1))
if rot: im=im.rotate(rot,expand=True)
im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
im.save('crops/'+o+'.png')
