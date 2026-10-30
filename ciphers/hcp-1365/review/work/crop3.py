from PIL import Image, ImageOps
r=Image.open('rot.png').convert('RGB')
C={'cardend':(930,1385,1110,1465,6),'thleft':(340,1350,520,1440,6),'boyend':(900,1000,1080,1090,6),'well':(370,1270,640,1360,5)}
for k,(a,b,c,d,s) in C.items():
    x=r.crop((a,b,c,d)); x=ImageOps.autocontrast(x,cutoff=1); x=x.resize((x.width*s,x.height*s),Image.BICUBIC); x.save(f'z_{k}.png')
p=Image.open('../../work/hires/pc_hcp_46_pic.JPG'); p.thumbnail((1000,1000)); p.save('pic_small.png')
