from PIL import Image
c=Image.open('work/crops/msg.png')
for n,b in dict(a=(170,70,650,180),b=(160,260,560,350),c=(530,260,900,360),d=(160,340,560,430),e=(540,340,960,430),f=(150,530,960,750)).items():
    s=c.crop(b); s=s.resize((s.width*4,s.height*4),Image.LANCZOS); s.save(f'work/crops/z{n}.png')
s=c.crop((0,560,960,750)).rotate(0); s=s.resize((s.width*2,s.height*2),Image.LANCZOS); s.save('work/crops/zf.png')
