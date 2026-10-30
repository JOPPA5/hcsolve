from PIL import Image
m=Image.open('crops/message.png')
b={'z_date':(410,40,600,115),'z_love':(255,410,400,520),'z_love2':(320,420,530,500),'z_pxo':(150,135,300,195),'z_ftu':(430,125,600,200),'z_mm':(25,335,215,375),'z_uijt':(255,330,420,400)}
for k,v in b.items():
    c=m.crop(v); c=c.resize((c.width*7,c.height*7),Image.BICUBIC); c.save(f'crops/{k}.png')
