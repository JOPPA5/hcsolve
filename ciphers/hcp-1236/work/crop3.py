from PIL import Image
im=Image.open('hires/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_adr.jpg').convert('RGB')
s=3445/1024
def c(n,a,b,y0,y1,z=2):
    r=im.crop((int(a*s),int(y0*s),int(b*s),int(y1*s))); r.resize((r.width*z,r.height*z),Image.LANCZOS).save(f'crops/{n}.png')
c('z1a',20,270,590,650); c('z1b',260,560,590,650)
c('z13',230,350,455,495,3)
c('z8',270,330,380,425,3)
