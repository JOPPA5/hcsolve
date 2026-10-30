from PIL import Image, ImageOps
im=Image.open('rot.png').convert('RGB')
b={'even':(850,1015,1105,1080),'F':(340,1340,440,1480),'G':(570,1560,650,1630),'f2':(430,1150,540,1290),'stamp':(100,120,400,400)}
for k,x in b.items():
    c=im.crop(x); c=c.resize((c.width*6,c.height*6),Image.BICUBIC); ImageOps.autocontrast(c,cutoff=0.3).save(f'y_{k}.png')
s=[Image.open(f'y_{k}.png') for k in ('F','G','f2')]
W=sum(i.width for i in s)+40; H=max(i.height for i in s)
o=Image.new('RGB',(W,H),'white'); x=0
for i in s: o.paste(i,(x,0)); x+=i.width+20
o.save('y_compare.png')
