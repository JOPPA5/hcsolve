from PIL import Image, ImageOps
import numpy as np
im=Image.open('rot.png')
def hi(c):
    g=ImageOps.autocontrast(c.convert('L'),cutoff=1); a=np.asarray(g).astype(float)
    return Image.fromarray(np.clip((a-120)*2.2,0,255).astype('uint8')).convert('RGB')
for k,b,s in [('L2b',(690,1040,1090,1160),4),('z_windsor',(600,1240,780,1400),7),('z_amp_L',(360,1340,640,1460),5),('z_tdots',(620,1340,790,1450),7)]:
    c=im.crop(b); x=c.resize((c.size[0]*s,c.size[1]*s),Image.LANCZOS)
    y=hi(c).resize(x.size,Image.LANCZOS)
    o=Image.new('RGB',(x.size[0],x.size[1]*2+6),'red'); o.paste(x,(0,0)); o.paste(y,(0,x.size[1]+6)); o.save(k+'.png')
