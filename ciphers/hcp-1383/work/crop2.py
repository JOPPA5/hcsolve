from PIL import Image
m=Image.open('work/crops/msg.png')
b={'a':(260,40,1000,220),'b':(190,190,1000,320),'c':(160,270,1000,410),'d':(160,370,1000,520),'e':(180,460,1000,630),'f':(20,570,1000,700),'g':(20,650,1000,790)}
for k,v in b.items():
  c=m.crop(v); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'work/crops/l{k}.png')
