from PIL import Image
im=Image.open('../../work/hires/cpc_--09_HU__HU_Jasz-Arokszalas_jolanka-83_adr.jpg').convert('RGB')
def c(n,b,s):
    r=im.crop(b); r.resize((r.width*s,r.height*s),Image.LANCZOS).save(f'crops/{n}.png')
c('z15',(760,1340,1260,1560),3)   # row 15 mid + row 16
c('z18',(90,1680,830,1960),2)     # rows 18-19 left
c('z19',(760,1740,1500,1960),2)   # row 19 right
c('z21a',(2130,1880,2560,2090),4) # overwritten sign
c('z21b',(2500,1900,2960,2080),4) # row 21 end under stamp
c('zpm',(1950,40,3300,500),1)     # postmarks
