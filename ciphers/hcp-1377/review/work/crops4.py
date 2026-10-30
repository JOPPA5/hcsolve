from PIL import Image, ImageOps
im=Image.open('../../work/hires/pc_hcp_58_adr.JPG').convert('RGB')
c=im.crop((1360,120,1660,430)).rotate(-90,expand=True)
c=ImageOps.autocontrast(c.convert('L'))
c.resize((c.size[0]*3,c.size[1]*3),Image.LANCZOS).save('stamp_up.png')
r=Image.open('reading.png')
c=r.crop((760,480,910,560)); c.resize((c.size[0]*8,c.size[1]*8),Image.LANCZOS).save('z_pvs.png')
