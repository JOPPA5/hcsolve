from PIL import Image, ImageOps
im=Image.open('work/hires/cpc_1912-03-27_HU__HU_Jasz-Arokszalas_jolanka-13_adr.jpg').convert('RGB')
def g(n,b,s=5):
    r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.LANCZOS).split()[1]
    ImageOps.autocontrast(r,cutoff=.5).save(n)
g('work/rev2/r09.png',(90,1230,480,1370))
g('work/rev2/r07b.png',(150,970,560,1110),3)
g('work/rev2/r15.png',(90,1960,420,2085))
