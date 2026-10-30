from PIL import Image, ImageOps
im=Image.open('hires/pc_hcp_28_adr.JPG').convert('RGB')
m=im.crop((130,100,800,1110)).rotate(90,expand=True)
m.save('crops/msg.png')
print(m.size)
W,H=m.size
# 2 x 3 tiles at 3x
for i,x0 in enumerate(range(0,W-1,340)):
  for j,(y0,y1) in enumerate([(0,240),(200,450),(420,670)]):
    t=m.crop((x0,y0,min(W,x0+400),y1)); t=t.resize((t.width*3,t.height*3),Image.LANCZOS)
    t=ImageOps.autocontrast(t,cutoff=1); t.save(f'crops/t{j}{i}.png')
