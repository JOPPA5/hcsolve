import sys,glob
from PIL import Image
im=Image.open(glob.glob('work/hires/*adr*')[0]).convert('RGB')
# name x0 y0 x1 y1 scale (coords in hires)
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(int,a[i+1:i+6])
    c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save('review/work/%s.png'%n)
