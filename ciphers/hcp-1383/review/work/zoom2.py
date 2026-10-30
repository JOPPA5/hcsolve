from PIL import Image
m=Image.open('msg.png').convert('RGB')
Z={'nz':(285,175,400,255,5),'hj':(690,720,960,840,4),'kvtu':(205,260,420,330,4),'come':(420,250,690,370,4),'back':(700,270,960,350,4),
'found':(310,350,700,440,3),'here':(590,420,860,520,3),'l6':(240,640,700,740,3),'pxo2':(680,620,880,720,4)}
for k,(a,b,c,d,s) in Z.items():
    r=m.crop((a,b,c,d)); r.resize((r.width*s,r.height*s),Image.LANCZOS).save(f'z_{k}.png')
