from PIL import Image
c=Image.open('crops/message.png')
a=Image.open('hires/pc_hcp_53_adr.JPG')
items=[c.crop((300,440,520,530)),c.crop((300,20,560,110)),c.crop((780,600,1000,740)),a.crop((1120,480,1640,620))]
W=1300;H=sum(i.height*4 for i in items)
o=Image.new('RGB',(W,H),'white');y=0
for i in items:
    i=i.convert('RGB').resize((i.width*4,i.height*4),Image.BICUBIC);i=i.crop((0,0,W,i.height));o.paste(i,(0,y));y+=i.height
o.save('crops/caps.png')
