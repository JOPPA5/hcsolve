from PIL import Image
m=Image.open('work/crops/msg.png')
b={'p1':(400,120,580,210),'p2':(690,570,880,680),'nl':(20,570,260,670),'el1':(600,130,780,210),'el2':(840,600,1000,680),'t':(680,670,960,790),'end':(860,320,1000,470)}
for k,v in b.items():
  c=m.crop(v); c=c.resize((c.width*5,c.height*5),Image.LANCZOS); c.save(f'work/crops/z{k}.png')
