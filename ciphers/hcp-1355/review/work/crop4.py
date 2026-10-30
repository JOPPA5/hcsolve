from PIL import Image, ImageOps
im=Image.open('rot.png').convert('RGB')
b={'gps':(590,1160,790,1260),'stroll':(900,1190,1090,1290),'love':(330,1545,540,1650),'e':(450,1475,600,1550),'even':(830,985,1085,1045),'margin':(90,1520,300,1640),'gG':(340,1370,420,1480),'Gfrom':(620,1590,800,1660)}
for k,x in b.items():
    c=im.crop(x); c=c.resize((c.width*8,c.height*8),Image.BICUBIC); ImageOps.autocontrast(c,cutoff=0.3).save(f'z_{k}.png')
p=Image.open('../../work/hires/pc_hcp_36_pic.JPG').convert('RGB'); print(p.size)
p2=p.copy(); p2.thumbnail((1000,1000)); p2.save('pic_small.png')
