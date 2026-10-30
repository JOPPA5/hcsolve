from PIL import Image, ImageOps, ImageEnhance
import sys
c=Image.open('crops/full_rot.png').convert('RGB')
g=c.split()[0]  # red: watermark grey & pencil; paper bright
lo,hi=120,225
g=g.point(lambda v:max(0,min(255,int((v-lo)*255/(hi-lo)))))
g.save('crops/full_c.png')
