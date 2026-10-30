from PIL import Image, ImageEnhance
c=Image.open('crops/msg.png')
b={'l0':(390,10,1050,110),'l1a':(390,100,760,190),'l1b':(740,95,1050,270),'l2a':(220,210,640,310),'l3a':(360,300,720,400),'l3b':(720,300,1060,420),'l4':(370,400,1000,500),'l5':(390,490,1050,600),'l6':(20,590,960,720)}
for k,v in b.items():
    x=c.crop(v); s=4 if v[2]-v[0]<450 else 3
    x=x.resize((x.width*s,x.height*s),Image.LANCZOS)
    x=ImageEnhance.Contrast(x).enhance(1.5); x.save(f'crops/{k}.png')
