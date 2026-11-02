from PIL import Image, ImageEnhance
p='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1138/work/hires/cpc_1916-03-17_HU_Mezokovesd_HU_Szomolya_szomolya-23_adr.jpg'
im=Image.open(p).convert('RGB').crop((0,0,1600,2200))
r=im.rotate(-51,expand=True,fillcolor=(255,255,255),resample=Image.BICUBIC)
r=ImageEnhance.Contrast(r).enhance(1.6)
r.save('crops/rot51.png'); print(r.size)
s=r.copy(); s.thumbnail((1400,1400)); s.save('crops/rot51_small.png')
