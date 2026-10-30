from PIL import Image, ImageOps
import sys
im=Image.open('../../work/hires/pc_hcp_50_adr.JPG').convert('RGB')
s=1785/1024
r=im.crop((int(60*s),int(25*s),int(600*s),int(632*s))).rotate(90,expand=True)
z={'a_l1a':(330,240,660,350),'a_l1b':(690,240,1040,370),'a_l2a':(325,355,620,490),'a_l2b':(600,355,1000,490),
'a_l3a':(320,460,600,600),'a_l3b':(600,470,960,590),'a_l4a':(350,560,700,670),'a_l4b':(690,550,1000,670),
'a_l5a':(320,670,680,790),'a_l5b':(690,660,1010,770),'a_l6':(570,770,850,910)}
for k,b in z.items():
    c=ImageOps.autocontrast(r.crop(b).convert('L'),cutoff=0.5)
    c.resize((c.width*4,c.height*4),Image.LANCZOS).save(k+'.png')
for k,b in {'b_ppm':(480,370,640,450),'b_sm':(690,800,840,860),'b_i':(385,380,470,450)}.items():
    c=ImageOps.autocontrast(r.crop(b).convert('L'),cutoff=0.5)
    c.resize((c.width*8,c.height*8),Image.LANCZOS).save(k+'.png')
