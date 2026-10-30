from PIL import Image, ImageEnhance
c=Image.open('crops/msg.png')
b={'y1':(840,330,1050,500),'y2':(380,110,560,190),'y3':(570,420,720,520),'y4':(640,500,860,580)}
for k,v in b.items():
    x=c.crop(v); s=6
    x=x.resize((x.width*s,x.height*s),Image.BICUBIC)
    x=ImageEnhance.Contrast(x).enhance(1.8); x.save(f'crops/{k}.png')
