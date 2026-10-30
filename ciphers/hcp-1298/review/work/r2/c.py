from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-77_adr.jpg').convert('RGB')
def c(n,b,s=4,r=0,k=1.7):
    x=im.crop(b)
    if r: x=x.rotate(r,expand=True)
    x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(k).save('review/work/r2/'+n+'.png')
c('all',(0,0,1700,2210),0.75)
c('a11',(60,840,560,970),3.2)
c('b11',(500,830,1000,960),3.2)
c('c11',(950,800,1650,930),2.6)
c('a20',(800,1470,1650,1610),2.3)
c('a21',(60,1590,700,1720),2.8)
