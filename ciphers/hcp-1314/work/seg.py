import sys
from PIL import Image
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/crops/'
n=Image.open(O+'desk.png')
# args: name x0 y0 x1 y1 [scale]
a=sys.argv[1:]
for i in range(0,len(a),6):
    nm,x0,y0,x1,y1,s=a[i],*map(float,a[i+1:i+6])
    c=n.crop((int(x0),int(y0),int(x1),int(y1)));c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(O+nm)
