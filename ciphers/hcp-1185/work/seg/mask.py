import sys, numpy as np
from PIL import Image
im=np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(int)
r,g,b=im[...,0],im[...,1],im[...,2]
mx=im.max(2); mn=im.min(2)
sat=(mx-mn)
ink=(mx<95)&(sat<45)
Image.fromarray(((~ink)*255).astype(np.uint8)).save(sys.argv[2])
np.save(sys.argv[3],ink)
print(ink.sum())
