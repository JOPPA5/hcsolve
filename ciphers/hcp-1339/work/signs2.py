from PIL import Image, ImageOps
im=Image.open('work/hires/pc_hcp_20_adr.JPG').convert('RGB')
b=[(270,775,330,870),(570,770,690,860),(190,875,260,980),(275,870,330,960),(340,350,0,0)][:4]
s=Image.new('RGB',(1500,560),'white');x=0
for q in b:
    c=im.crop(q); c=ImageOps.autocontrast(c,cutoff=1).resize((c.width*5,c.height*5),Image.LANCZOS); s.paste(c,(x,0)); x+=c.width+15
s.save('work/crops/doubtful2.png')
