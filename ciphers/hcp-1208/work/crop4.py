from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg').convert('RGB')
def c(name,box,s=3):
    r=im.crop(box); r=ImageEnhance.Color(r).enhance(3.0); r=ImageEnhance.Contrast(r).enhance(1.5)
    r=r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC); r.save('crops/%s.png'%name)
for i,y in enumerate(range(280,2060,250)):
    for n,x in (('A',80),('B',560),('C',860)):
        c('r%d%s'%(i,n),(x,y,x+680,y+300))
