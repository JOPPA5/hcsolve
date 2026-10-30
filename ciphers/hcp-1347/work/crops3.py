from PIL import Image
m=Image.open('crops/msg.png')
B={'e':(470,420,620,500,8),'hj':(720,560,1000,660,6),'m2':(650,95,800,170,8),'m7':(460,560,600,640,8),'n2':(340,95,450,170,8),'hiu':(800,410,980,490,8),'opu':(350,480,520,580,7)}
for k,b in B.items():
    s=b[4];t=m.crop(b[:4]); t=t.resize((t.width*s,t.height*s),Image.BICUBIC); t.save(f'crops/z_{k}.png')
