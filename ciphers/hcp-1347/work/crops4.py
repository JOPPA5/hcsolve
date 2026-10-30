from PIL import Image, ImageOps
m=Image.open('crops/msg.png')
t=m.crop((900,570,1000,650)).convert('L'); t=ImageOps.autocontrast(t,cutoff=0.5).resize((1000,800),Image.BICUBIC); t.save('crops/z_blot.png')
t=m.crop((540,480,870,590)); t=t.resize((t.width*5,t.height*5),Image.BICUBIC); t.save('crops/z_bmpof.png')
