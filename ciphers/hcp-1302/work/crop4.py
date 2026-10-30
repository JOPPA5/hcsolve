from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1302/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_adr.jpg').convert('RGB')
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1302/work/crops/'
def s(n,box,z=4):
    c=im.crop(box); c.resize((c.width*z,c.height*z),Image.LANCZOS).save(d+n+'.png')
s('v1',(1620,1880,2130,2040),3)
s('v2',(1100,1990,1560,2110),4)
s('v3',(60,1990,620,2110),3)
s('v4',(620,1990,1160,2110),3)
s('v5',(2000,1880,2520,2030),3)
s('v6',(1620,1880,1900,2030),5)
c=im.crop((2640,190,3130,770)).rotate(90,expand=True); c=c.crop((0,330,490,580)); c.resize((c.width*3,c.height*3),Image.LANCZOS).save(d+'v7.png')
s('w1',(1000,1020,2700,1860),1)
