from PIL import Image
c=Image.open('work/crops/msg.png')
B={'w4':(70,300,250,395),'smudge':(225,290,320,370),'night':(460,215,650,300),'wet':(285,225,430,310)}
for k,b in B.items():
    r=c.crop(b); r=r.resize((r.width*6,r.height*6),Image.BICUBIC); r.save(f'work/crops/{k}.png')
