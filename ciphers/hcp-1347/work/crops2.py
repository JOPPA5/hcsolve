from PIL import Image, ImageOps
m=Image.open('crops/msg.png')
B={'l3a':(330,165,680,300),'l3b':(610,170,1000,330),'l4a':(330,270,680,410),'l4b':(560,260,920,410),'l5a':(330,380,680,490),'l5b':(640,400,1000,500),'l6':(340,460,880,590),'l7a':(30,520,420,660),'l7b':(400,530,1000,660),'l2m':(600,90,1000,200)}
for k,b in B.items():
    t=m.crop(b); t=t.resize((t.width*4,t.height*4),Image.LANCZOS); t.save(f'crops/{k}.png')
