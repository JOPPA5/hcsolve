from PIL import Image
m=Image.open('work/crops/msg.png')
b={'w1':(170,300,440,400),'w2':(620,310,1000,400),'w3':(160,380,520,480),'w4':(560,390,930,480),'w5':(200,500,430,600),'w6':(440,490,640,600),'w7':(640,510,980,620),'w8':(240,600,500,700)}
for k,v in b.items():
  c=m.crop(v); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(f'work/crops/{k}.png')
