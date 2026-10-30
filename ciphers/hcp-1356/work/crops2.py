from PIL import Image
m=Image.open('crops/message.png')
b={'head':(0,20,600,125),'l1a':(15,115,370,230),'l1b':(340,115,725,215),'l2a':(15,215,360,290),'l2b':(260,220,715,330),'l3a':(25,300,370,380),'l3b':(420,320,715,430),'l4a':(10,395,300,520),'l4b':(250,400,540,520),'l4c':(520,410,715,530),'l5a':(50,470,300,600),'l5b':(260,500,590,670)}
for k,v in b.items():
    c=m.crop(v); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(f'crops/{k}.png')
