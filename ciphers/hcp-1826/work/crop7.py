from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
c=im.crop((470,195,610,265)).rotate(180,expand=True); c.resize((c.width*6,c.height*6),Image.LANCZOS).save('work/crops/would2.png')
c=im.crop((1150,40,1420,300)); c=ImageEnhance.Contrast(c).enhance(2.2); c.resize((c.width*3,c.height*3),Image.LANCZOS).save('work/crops/pm.png')
p=Image.open('work/hires/pc_hcp_507_pic.JPG').convert('RGB')
c=p.crop((50,300,260,760)).rotate(-90,expand=True); c=ImageEnhance.Contrast(c).enhance(2.5); c.resize((c.width*3,c.height*3),Image.LANCZOS).save('work/crops/sig.png')
