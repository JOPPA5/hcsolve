from PIL import Image, ImageOps
im=Image.open('hires/pc_hcp_53_adr.JPG').convert('RGB')
c=im.crop((120,70,920,1080)).rotate(90,expand=True)
c.save('crops/message.png'); print(c.size)
c2=c.resize((c.width*2,c.height*2),Image.LANCZOS)
# bands by rotated y
W,H=c2.size
for i,(a,b) in enumerate([(0,600),(500,1100),(1000,1600)]):
    for j,(x,y) in enumerate([(0,1050),(950,2020)]):
        c2.crop((x,a,y,b)).save(f'crops/b{i}{j}.png')
