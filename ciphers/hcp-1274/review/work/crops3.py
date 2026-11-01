from PIL import Image
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-73_adr.jpg')
def c(n,box,s=6):
    r=im.crop(box); r.resize((r.width*s,r.height*s),Image.LANCZOS).save(f'review/work/z_{n}.png')
c('kelene',(1530,2010,1790,2130),6)
c('mikotT',(1640,1930,1800,2030),8)
c('isten',(1960,1885,2180,1985),7)
c('oval',(200,1270,340,1400),7)
