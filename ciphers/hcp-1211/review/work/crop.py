from PIL import Image
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
s=3421/1024
# bands in 1024-scale (top,bottom), three per image
bands=[(22,110),(95,170),(155,235),(220,295),(285,350),(340,410),(400,470),(460,530),(520,590),(580,650)]
for i,(a,b) in enumerate(bands):
    for j,(x0,x1) in enumerate([(20,210),(190,390),(370,570)]):
        c=im.crop((int(x0*s),int(a*s),int(x1*s),int(b*s)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'r{i}_{j}.jpg',quality=88)
c=im.crop((int(200*s),int(610*s),int(760*s),int(650*s)));c=c.resize((c.width*1,c.height*1));c.save('bot.jpg')
c=im.crop((int(840*s),int(40*s),int(960*s),int(200*s))).rotate(-90,expand=True);c=c.resize((c.width*2,c.height*2),Image.LANCZOS);c.save('stamp.jpg')
c=im.crop((int(570*s),int(150*s),int(1010*s),int(640*s)));c.save('addr.jpg')
