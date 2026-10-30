from PIL import Image, ImageOps
import numpy as np, sys
im=Image.open('rot.png')
print(im.size)
w,h=im.size
# message band: lower part
m=im.crop((0,int(h*.45),w,h))
m.save('msg.png'); print(m.size)
a=np.asarray(m).astype(float)
ink=np.clip((a[:,:,2]-a[:,:,0])*6,0,255)
Image.fromarray((255-ink).astype('uint8')).save('msg_ink.png')
