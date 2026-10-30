from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1912-07-03_HU__HU_Jasz-Arokszalas_jolanka-28_adr.jpg').convert('RGB')
S=1.72
def c(n,l,t,r,b,z=3,con=1.4):
    x=im.crop((int(l*S),int(t*S),int(r*S),int(b*S)));x=x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(con).save('crops/'+n+'.png')
c('s1',1545,145,1750,205,5);c('s2',1545,195,1750,255,5);c('s3',1545,250,1750,305,5);c('s4',1545,290,1750,345,5);c('s5',1545,330,1750,375,5);c('s6',1545,360,1790,410,5)
c('r18a',50,1025,450,1085,2.8);c('r18b',430,1025,830,1085,2.8)
c('r19a',50,1085,450,1140,2.8);c('r19b',430,1085,830,1140,2.8)
c('r20a',50,1130,450,1185,2.8);c('r20b',430,1130,830,1185,2.8)
