import sys
from PIL import Image, ImageFilter, ImageOps, ImageChops
import numpy as np
src,out,x0,y0,x1,y1,s=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:8])
im=Image.open(src).convert('L')
a=np.asarray(im,dtype=np.float32)
# median-ish background via strong blur on max filter
bg=np.asarray(im.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(6)),dtype=np.float32)
n=a/np.maximum(bg,1); n=np.clip((n-0.80)/0.20,0,1)**1.6*255
r=Image.fromarray(n.astype(np.uint8)).crop((x0,y0,x1,y1))
r=ImageOps.autocontrast(r,cutoff=0.5)
r=r.resize(((x1-x0)*s,(y1-y0)*s),Image.LANCZOS)
r.save(out)
