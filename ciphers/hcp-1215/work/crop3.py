from PIL import Image, ImageOps, ImageChops
f='hires/cpc_1914-11-28_HU__HU_helyben-(locally)-Budapest_jolanka-57_adr.jpg'
im=Image.open(f).convert('RGB')
def c(n,b,s=3.0,col=False):
    r=im.crop(b).resize((int((b[2]-b[0])*s),int((b[3]-b[1])*s)),Image.LANCZOS)
    if col: r=ImageOps.autocontrast(r,cutoff=0.5); r.save('crops/'+n+'.png');return
    ImageOps.autocontrast(r.split()[0],cutoff=1).save('crops/'+n+'.png')
c('z5a',(760,300,1320,470));c('z5b',(1250,320,1700,500))
c('z6a',(60,410,620,540));c('z6b',(560,410,1120,540));
c('zszeret',(1250,900,1720,1010))
c('zdate',(1150,430,1760,620),2.5)
c('zhogy',(1450,1560,1760,1760),3)
c('zend',(1000,1980,1500,2060),3)
c('stampc',(2740,250,3200,780),3,True)
