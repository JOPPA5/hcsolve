from PIL import Image, ImageOps
import numpy as np, glob
im=Image.open(glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1171/work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1600
c=im.crop((int(170*S),int(905*S),int(500*S),int(955*S)))
c=c.resize((c.width*5,c.height*5),Image.LANCZOS)
c.save('crops/w_col.png')
a=np.asarray(c).astype(float)
# blue-ness: b minus g suppresses olive print (b<g) and brown; keep ink where b-g high or very dark
v=a[...,2]-a[...,1]+ (a[...,2]-a[...,0])*0.6
g=255-np.clip((v-v.min())/(np.percentile(v,99.5)-v.min())*255,0,255)
ImageOps.autocontrast(Image.fromarray(g.astype('uint8'))).save('crops/w_blue.png')
