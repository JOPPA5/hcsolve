from PIL import Image, ImageOps
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('L')
s=3445/1024
B={'r1end':(370,25,430,75),'r2end':(330,55,500,100),'r7start':(20,240,200,290),'r7mid':(170,225,350,285),
'r6end':(290,195,420,240),'r9end':(280,290,480,340),'r10end':(340,315,460,360),'r11start':(25,375,200,415),
'r11mid':(140,370,300,415),'r12start':(25,405,200,455),'r13':(25,430,240,480),'r18end':(320,555,660,600),'pm':(700,25,960,230),
'r15':(190,455,480,510),'addr':(490,100,920,530)}
for k,b in B.items():
    c=im.crop(tuple(int(v*s) for v in b)); c=ImageOps.autocontrast(c,cutoff=1)
    f=(3 if k not in('pm','addr') else 1); c=c.resize((c.width*f,c.height*f),Image.LANCZOS)
    c.save(f'crops/z_{k}.png')
# montage of small
names=['r1end','r2end','r7start','r7mid','r6end','r9end','r10end','r11start','r11mid','r12start','r13','r15']
for g,part in enumerate([names[:6],names[6:]]):
    ims=[Image.open(f'crops/z_{n}.png') for n in part]
    W=max(i.width for i in ims);H=sum(i.height+10 for i in ims)
    m=Image.new('L',(W,H),255);y=0
    for i in ims: m.paste(i,(0,y));y+=i.height+10
    m.save(f'crops/m{g}.png');print(m.size)
