import glob
from PIL import Image, ImageOps
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1151/'
im=Image.open(glob.glob(base+'work/hires/*_adr.jpg')[0]).convert('RGB')
g=im.split()[1]
Z={'y_soka':(1250,1050,1640,1170,4),'y_r20':(30,1745,830,1830,3),'y_r21':(30,1810,830,1890,3),'y_r22':(30,1865,830,1950,3),'y_r23':(30,1920,830,2010,3),
   'y_r22b':(600,1860,1000,1960,5),'y_r22a':(40,1860,340,1950,6),'y_r23b':(830,1920,1400,2010,3)}
for n,(a,b,c,d,s) in Z.items():
    r=ImageOps.autocontrast(g.crop((a,b,c,d)),cutoff=0.3); r.resize((r.width*s,r.height*s),Image.LANCZOS).save(base+'review/work/crops/%s.png'%n)
