from PIL import Image, ImageEnhance
c=Image.open('crops/msg.png')
b={'z1':(740,100,900,240),'z2':(860,100,1020,200),'z3':(800,190,1020,260),'z4':(640,230,890,300),'z5':(720,310,900,420),'z6':(860,320,1050,400)}
for k,v in b.items():
    x=c.crop(v); s=6
    x=x.resize((x.width*s,x.height*s),Image.BICUBIC)
    x=ImageEnhance.Contrast(x).enhance(1.4); x.save(f'crops/{k}.png')
