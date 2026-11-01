from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1914-06-10_HU__HU_Jasz-Arokszalas_jolanka-54_adr.jpg').convert('RGB')
k=3445/1500
for i,(a,b) in enumerate([(30,105),(100,175),(170,245),(240,315),(310,385),(380,455)]):
    r=im.crop((int(30*k),int(a*k),int(690*k),int(b*k)))
    r=r.resize((1960,int(r.height*1960/r.width)),Image.BICUBIC)
    r=ImageEnhance.Contrast(ImageEnhance.Color(r).enhance(2)).enhance(1.3)
    r.save('crops/s%d.png'%i)
