from PIL import Image,ImageEnhance
m=Image.open('crops/msg.png')
L={'pz':(320,120,600,210),'ju':(170,215,330,310),'xbt':(330,215,500,290),'hrs':(290,310,450,380),'clearing1':(235,395,470,520),'clearing2':(440,410,810,530),'jut':(220,500,450,610),'zpvs':(620,590,860,680),'girl':(470,680,760,740),'cf':(440,300,640,440)}
for k,b in L.items():
    c=m.crop(b); s=1500/c.width; c=c.resize((1500,int(c.height*s)),Image.BICUBIC); c=ImageEnhance.Contrast(c).enhance(1.4); c.save(f'crops/z_{k}.png')
