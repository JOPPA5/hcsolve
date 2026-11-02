from PIL import Image, ImageOps
b='work/hires/cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12_adr.jpg'
im=Image.open(b).convert('L')
for k,(x0,y0,x1,y1,s) in {'ert':(690,930,1000,1050,6),'kam':(850,40,1350,170,4),'igy':(190,1290,440,1390,6)}.items():
    c=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)),cutoff=1); c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'review/work/{k}.png')
