from PIL import Image,ImageEnhance
m=Image.open('crops/msg.png')
L={'no':(20,30,200,130),'cl1':(235,395,470,490),'nz2':(170,120,320,210)}
for k,b in L.items():
    c=m.crop(b); s=1200/c.width; c=c.resize((1200,int(c.height*s)),Image.BICUBIC); c=ImageEnhance.Contrast(c).enhance(1.4); c.save(f'crops/z_{k}.png')
s=Image.open('../../hcp-1386/work/crops/band6.png'); print(s.size)
