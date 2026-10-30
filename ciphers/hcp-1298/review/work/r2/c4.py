from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-77_adr.jpg').convert('RGB')
def g(n,b,s=6,k=1.8):
    x=im.crop(b);x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(k).save('review/work/r2/'+n+'.png')
g('w11',(350,850,800,950),4)
g('w10',(60,790,700,890),3)
g('w1',(60,60,860,190),2.4)
g('w1b',(860,60,1660,190),2.4)
g('w2',(60,140,860,260),2.4)
g('w4',(60,290,860,420),2.4)
g('w5',(60,370,860,500),2.4)
g('w8',(60,600,860,730),2.4)
