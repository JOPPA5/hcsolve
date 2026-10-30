from PIL import Image, ImageOps
im=Image.open('work/hires/pc_hcp_12_adr.JPG')
c=im.crop((50,40,240,1090)).rotate(90,expand=True)
print(c.size)
for i,(a,b) in enumerate([(0,540),(500,1050)]):
    s=c.crop((a,0,b,190)); s=ImageOps.autocontrast(s.convert('L'),cutoff=1); s=s.resize((s.width*3,s.height*3),Image.LANCZOS); s.save(f'work/crops/edge{i}.png')
# g sign
m=Image.open('work/crops/msg.png')
s=m.crop((360,340,600,420)); s=s.resize((s.width*7,s.height*7),Image.BICUBIC); s.save('work/crops/g.png')
s=im.crop((1000,480,1760,1000)); s.resize((1140,780)).save('work/crops/addr.png')
s=im.crop((1150,120,1700,500)); s.save('work/crops/pm.png')
