from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
c=im.crop((55,40,180,140)).rotate(180+40,expand=True,resample=Image.BICUBIC,fillcolor=(230,210,180))
c.resize((c.width*6,c.height*6),Image.LANCZOS).save('work/crops/corner_r.png')
c=im.crop((230,40,350,100)).rotate(180,expand=True); c.resize((c.width*7,c.height*7),Image.LANCZOS).save('work/crops/circ18.png')
