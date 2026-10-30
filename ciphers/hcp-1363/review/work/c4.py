from PIL import Image, ImageOps, ImageChops
import datetime
print(datetime.date(1907,7,19).strftime('%A'))
r=Image.open('adr_ccw.png').convert('RGB')
def crop(n,box,s=4):
    c=r.crop(box); c=c.resize((c.width*s,c.height*s),Image.LANCZOS)
    ImageOps.autocontrast(c,cutoff=1).save(n+'.png')
    R,G,B=r.crop(box).split()
    d=ImageOps.autocontrast(ImageChops.subtract(B,R),cutoff=0.5).resize((c.width,c.height),Image.LANCZOS)
    ImageOps.invert(d).save(n+'_ink.png')
crop('h_dbset',(560,1180,800,1290))
crop('h_faint',(360,1330,760,1490),3)
crop('h_windsor_end',(600,1270,740,1370),5)
crop('h_love',(510,950,860,1060),3)
crop('h_cross',(800,1290,740+160,1320),4) if 0 else None
p=Image.open('../../work/hires/pc_hcp_44_adr.JPG').convert('RGB')
pc=r.crop((180,80,480,330)).rotate(-90,expand=True).resize((750,900),Image.LANCZOS); ImageOps.autocontrast(pc,cutoff=1).save('h_postmark.png')
