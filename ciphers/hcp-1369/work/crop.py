from PIL import Image, ImageOps
im=Image.open('hires/pc_hcp_50_adr.JPG').convert('RGB')
s=1785/1024
r=im.crop((int(60*s),int(25*s),int(600*s),int(632*s))).rotate(90,expand=True)
print(r.size)
r.save('crops/msg.png')
H=r.size[1]
# bands in rotated coords (r px); from 2x view y/2
bands={'l1':(130,270),'l2':(235,360),'l3':(340,480),'l4':(450,590),'l5':(540,680),'l6':(650,800),'l7':(760,941)}
for k,(a,b) in bands.items():
    c=r.crop((0,a+52-0 if False else a,r.size[0],min(H,b)))
    c=ImageOps.autocontrast(c,cutoff=1)
    c.resize((c.width*2,c.height*2),Image.LANCZOS).save(f'crops/{k}.png')
bx={'b1':(320,140,1040,360),'b2':(320,355,1040,590),'b3':(320,555,1040,670),'b4':(320,665,1040,790),'b5':(560,770,860,910)}
for k,b in bx.items():
    c=ImageOps.autocontrast(r.crop(b),cutoff=1); f=4 if k=='b5' else 3
    c.resize((c.width*f,c.height*f),Image.BICUBIC).save(f'crops/{k}.png')
from PIL import ImageDraw
z={'z_nz':(330,250,440,350),'z_nl1':(690,250,880,360),'z_school':(325,360,600,490),'z_park':(480,470,720,590),'z_ebz':(350,570,530,660),'z_nal':(540,555,800,665),'z_tail':(780,555,1000,660),'z_nl2':(710,665,1000,760),'z_your':(320,670,540,790)}
for k,b in z.items():
    c=ImageOps.autocontrast(r.crop(b),cutoff=0.5)
    c.resize((c.width*6,c.height*6),Image.BICUBIC).save(f'crops/{k}.png')
c=ImageOps.autocontrast(r.crop((890,250,1050,380)),cutoff=0.5); c.resize((c.width*6,c.height*6),Image.BICUBIC).save('crops/z_cpz.png')
