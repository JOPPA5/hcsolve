from PIL import Image, ImageEnhance
im=Image.open('../../work/hires/cpc_1916-03-17_HU_Mezokovesd_HU_Szomolya_szomolya-23_adr.jpg').convert('RGB').crop((0,0,2300,2298))
r=im.rotate(-49.5,expand=True,fillcolor=(255,255,255),resample=Image.BICUBIC)
r=ImageEnhance.Contrast(r).enhance(1.5); r.save('r2/r.png'); print(r.size)
s=r.copy(); s.thumbnail((1500,1500)); s.save('r2/rs.png'); print(s.size)
