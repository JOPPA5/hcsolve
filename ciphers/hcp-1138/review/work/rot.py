from PIL import Image, ImageEnhance
import sys
p='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1138/work/hires/cpc_1916-03-17_HU_Mezokovesd_HU_Szomolya_szomolya-23_adr.jpg'
im=Image.open(p).convert('RGB').crop((0,0,1600,2200))
r=im.rotate(-46,expand=True,fillcolor=(255,255,255),resample=Image.BICUBIC)
r=ImageEnhance.Contrast(r).enhance(1.5)
r.save('crops/rot46.png'); print(r.size)
s=r.copy(); s.thumbnail((1500,1500)); s.save('crops/rot46_small.png')
