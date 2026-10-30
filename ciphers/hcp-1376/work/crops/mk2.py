from PIL import Image,ImageEnhance
m=Image.open('crops/msg.png')
L={'l1':(0,20,860,130),'l2':(160,110,800,210),'l3':(160,200,830,320),'l4':(190,300,760,440),'l5':(220,390,820,530),'l6':(200,490,860,630),'l7':(140,570,860,690),'l8':(230,650,800,740)}
for k,b in L.items():
    c=m.crop(b); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c=ImageEnhance.Contrast(c).enhance(1.5); c.save(f'crops/{k}.png')
