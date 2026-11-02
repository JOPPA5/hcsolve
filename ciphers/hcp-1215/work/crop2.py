from PIL import Image, ImageOps
f='hires/cpc_1914-11-28_HU__HU_helyben-(locally)-Budapest_jolanka-57_adr.jpg'
p='hires/cpc_1914-11-28_HU__HU_helyben-(locally)-Budapest_jolanka-57_pic.jpg'
im=Image.open(f).convert('RGB')
def c(n,b,s=2.0,src=im,rot=0):
    r=src.crop(b)
    if rot: r=r.rotate(rot,expand=True)
    r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS)
    # green channel suppresses little; use red channel: green ink dark in red
    g=ImageOps.autocontrast(r.split()[0],cutoff=1)
    g.save('crops/'+n+'.png')
c('a1',(60,230,900,560));c('a2',(860,230,1720,560))
c('b1',(60,500,900,800));c('b2',(860,500,1720,800))
c('c1',(60,740,900,960));c('c2',(860,740,1720,960))
c('lastL',(60,1880,1000,2060));c('lastM',(900,1880,1900,2060));c('lastR',(1800,1880,3350,2060),1.2)
c('r5',(60,1230,1720,1400),1.15)
c('istvan',(1750,1720,3350,1920),1.2)
c('urlean',(1750,1120,3000,1420),1.4)
c('onagy',(1600,100,2300,330),2)
pic=Image.open(p).convert('RGB')
c('pic_full',(0,0,3445,2210),0.55,pic,90)
