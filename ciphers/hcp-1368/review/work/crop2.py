from PIL import Image, ImageOps
im=Image.open('../../work/hires/pc_hcp_49_adr.JPG').rotate(90,expand=True).convert('RGB')
B={'z_dbset':(880,1130,1075,1200),'z_ojdf':(440,1325,660,1440),'z_L':(800,1290,1060,1420),'z_sm':(830,1500,1020,1600)}
for k,b in B.items():
    c=ImageOps.autocontrast(im.crop(b).convert('L'),cutoff=1); c=c.resize((c.width*6,c.height*6),Image.LANCZOS); c.save(k+'.png')
p=Image.open('../../work/hires/pc_hcp_49_pic.JPG'); p.thumbnail((1000,1000)); p.convert('RGB').save('pic.png')
