import sys
from PIL import Image
im=Image.open('source/address-large.jpg')
x0,y0,x1,y1=map(int,sys.argv[1:5]);z=int(sys.argv[5]) if len(sys.argv)>6 else 6
im.crop((x0,y0,x1,y1)).resize(((x1-x0)*z,(y1-y0)*z),Image.LANCZOS).save(sys.argv[-1])
