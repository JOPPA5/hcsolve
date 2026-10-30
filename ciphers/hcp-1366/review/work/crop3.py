from PIL import Image, ImageOps, ImageEnhance
m=Image.open('msg.png')
def z(n,b,s,con=False):
    x=m.crop(b); x=x.resize((x.size[0]*s,x.size[1]*s),Image.BICUBIC)
    if con: x=ImageOps.autocontrast(x.convert('L'),cutoff=1)
    x.save(n)
z('z_love1.png',(510,120,680,250),8)
z('z_love1c.png',(510,120,680,250),8,True)
z('z_letter.png',(420,370,660,480),6,True)
z('z_l4a.png',(30,430,340,550),4)
z('z_head.png',(10,10,530,200),3)
i=Image.open('../../work/hires/pc_hcp_47_adr.JPG').convert('RGB')
x=i.crop((1440,80,1785,440)); x.resize((x.size[0]*2,x.size[1]*2),Image.BICUBIC).save('z_stamp.png')
