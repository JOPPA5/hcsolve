from PIL import Image, ImageOps
im=Image.open('../hires/cpc_1915-10-25_HU_Mezokovesd_HU_Szomolya_szomolya-03_adr.jpg').convert('RGB')
def c(n,b,s=3):
    x=im.crop(b); r=x.split()[0]  # red channel: blue ink dark; brown lighter? 
    g=ImageOps.autocontrast(r,cutoff=1)
    W=(b[2]-b[0])*s;H=(b[3]-b[1])*s
    x.resize((W,H),Image.LANCZOS).save(n+'.png'); g.resize((W,H),Image.LANCZOS).save(n+'_r.png')
c('l1a',(60,360,780,480),2); c('l1b',(760,360,1480,480),2)
c('l2a',(60,470,780,590),2); c('l2b',(760,470,1480,590),2)
c('l3a',(60,580,780,700),2); c('l3b',(760,580,1480,700),2)
c('l4a',(60,700,780,820),2); c('l4b',(760,700,1480,820),2)
c('l5a',(60,820,780,960),2)
