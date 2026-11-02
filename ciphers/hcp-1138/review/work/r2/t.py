from PIL import Image, ImageEnhance, ImageDraw
im=Image.open('../../work/hires/cpc_1916-03-17_HU_Mezokovesd_HU_Szomolya_szomolya-23_adr.jpg').convert('RGB').crop((0,0,2300,2298))
r=im.rotate(-46,expand=True,fillcolor=(255,255,255),resample=Image.BICUBIC)
r=ImageEnhance.Contrast(r).enhance(1.5); r.save('r2/r46.png'); print(r.size)
s=r.copy(); d=ImageDraw.Draw(s)
for k in range(0,r.width,200):
    d.line([(k,0),(k,r.height)],fill=(255,0,0),width=2); d.line([(0,k),(r.width,k)],fill=(255,0,0),width=2)
    d.text((k+4,4),str(k),fill=(255,0,0)); d.text((4,k+4),str(k),fill=(255,0,0))
s.thumbnail((1400,1400)); s.save('r2/g46.png')
