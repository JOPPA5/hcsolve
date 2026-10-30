from PIL import Image
import numpy as np
im=Image.open('rot.png')
def ink(c):
    a=np.asarray(c).astype(float)
    i=np.clip(255-(a[:,:,2]-a[:,:,0])*7,0,255)
    return Image.fromarray(i.astype('uint8')).convert('RGB')
rows={'L1a':(340,950,760,1070),'L1b':(700,950,1090,1070),'L2':(340,1040,760,1160),'L3a':(340,1130,700,1260),'L3b':(680,1130,1060,1260),
'L4a':(340,1230,740,1390),'L4b':(720,1270,1090,1390),'L5a':(340,1330,760,1460),'L5b':(700,1340,1060,1460),'L6':(340,1420,860,1540),'L7':(720,1530,1090,1680)}
for k,b in rows.items():
    c=im.crop(b)
    s=4 if c.size[0]<450 else 3
    x=c.resize((c.size[0]*s,c.size[1]*s),Image.LANCZOS)
    y=ink(c).resize(x.size,Image.LANCZOS)
    o=Image.new('RGB',(x.size[0],x.size[1]*2+6),'red'); o.paste(x,(0,0)); o.paste(y,(0,x.size[1]+6)); o.save(k+'.png')
