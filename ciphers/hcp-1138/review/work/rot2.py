from PIL import Image, ImageEnhance
p='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1138/work/hires/cpc_1916-03-17_HU_Mezokovesd_HU_Szomolya_szomolya-23_adr.jpg'
im=Image.open(p).convert('RGB').crop((0,0,2300,2298))
r=im.rotate(-51,expand=True,fillcolor=(255,255,255),resample=Image.BICUBIC)
r=ImageEnhance.Contrast(r).enhance(1.6)
r.save('crops/rot51w.png'); print(r.size)
