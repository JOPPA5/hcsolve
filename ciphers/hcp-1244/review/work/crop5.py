from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_1912-04-10_HU__HU_Jasz-Arokszalas_jolanka-16_adr.jpg').convert('RGB')
x=im.crop((1600,180,2450,700)).rotate(180)
x=ImageEnhance.Contrast(x).enhance(1.5); x.save('review/work/crops/pm180.png')
