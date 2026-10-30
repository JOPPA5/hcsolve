from PIL import Image
r=Image.open('reading.png')
b={'cjlf2':(125,245,410,400,4),'n_end':(590,490,680,560,7),'bn2':(270,155,350,225,7)}
for k,(a,b1,c1,d,s) in b.items():
    c=r.crop((a,b1,c1,d)); c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'crops/{k}.png')
