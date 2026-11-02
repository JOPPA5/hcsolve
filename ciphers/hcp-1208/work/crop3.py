from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg').convert('RGB')
def c(name,box,s=3):
    r=im.crop(box); r=ImageEnhance.Color(r).enhance(3.0); r=ImageEnhance.Contrast(r).enhance(1.5)
    r=r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC); r.save('crops/%s.png'%name)
y=260
for i in range(4):
    c('c%d'%i,(850,y,1530,y+300)); y+=170
