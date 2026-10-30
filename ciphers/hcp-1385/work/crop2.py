from PIL import Image
c=Image.open('work/crops/msg.png')
B={'l1':(40,100,720,215),'l2a':(40,205,400,320),'l2b':(380,205,700,320),'l3a':(40,295,360,400),'l3b':(300,290,640,370),'l4':(30,370,660,480),'l5':(240,450,700,550),'hd':(20,0,700,90)}
for k,b in B.items():
    r=c.crop(b); r=r.resize((r.width*3,r.height*3),Image.LANCZOS); r.save(f'work/crops/{k}.png')
