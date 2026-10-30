from PIL import Image, ImageOps, ImageEnhance
im=Image.open('hires/pc_hcp_1_adr.JPG').convert('RGB').rotate(90,expand=True)
t=im.crop((40,1000,1140,1400))
t=ImageEnhance.Contrast(t).enhance(1.8)
t.crop((0,0,600,400)).resize((1800,1200),Image.LANCZOS).save('crops/a1.jpg',quality=92)
t.crop((500,0,1100,400)).resize((1800,1200),Image.LANCZOS).save('crops/a2.jpg',quality=92)
