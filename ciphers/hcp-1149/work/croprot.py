import sys,glob,os
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))
im=Image.open(glob.glob(D+'/hires/*_adr.jpg')[0]).convert('RGB')
s=3468/1800
n,x0,y0,x1,y1,z,r=sys.argv[1],*map(float,sys.argv[2:8])
c=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s))).rotate(r,expand=True)
c=c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS)
c.save(D+'/crops/%s.png'%n);print(c.size)
