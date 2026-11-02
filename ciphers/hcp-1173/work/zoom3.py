import glob
from PIL import Image, ImageOps
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
r=im.split()[0]
Z={'w1':(50,1960,700,2070),'w2':(600,1950,1250,2070),'k1':(830,350,1560,440),'j':(400,430,900,540),'r':(40,510,700,620),'d2':(1150,1440,1800,1540),'sz':(60,1900,600,1990)}
for k,b in Z.items():
    c=r.crop(b); c=ImageOps.autocontrast(c,cutoff=0.5).resize((c.width*3,c.height*3),Image.LANCZOS); 
    d=im.crop(b).resize((c.width,c.height),Image.LANCZOS)
    W=Image.new('RGB',(c.width,c.height*2+6),'white'); W.paste(d,(0,0)); W.paste(c.convert('RGB'),(0,c.height+6)); W.save(f'crops/z_{k}.png')
# postmark rotated
c=im.crop((2200,80,3000,720)); c.save('crops/z_pm.png')
