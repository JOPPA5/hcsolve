from PIL import Image, ImageEnhance
im=Image.open('hires/pc_hcp_1_adr.JPG').convert('RGB').rotate(90,expand=True)
t=ImageEnhance.Contrast(im.crop((40,1330,1140,1760))).enhance(1.8)
t.resize((2200,860),Image.LANCZOS).save('crops/a3.jpg',quality=92)
