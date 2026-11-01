from PIL import Image
import sys
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/'
im=Image.open(d+'work/hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
ys=[(70,300),(250,540),(490,760),(740,1000),(960,1240),(1200,1500),(1440,1780),(1700,1950)]
ys=[(70,430),(400,760),(740,1100),(1070,1430),(1400,1760),(1700,1960)]
for i,(a,b) in enumerate(ys):
    for j,(l,r) in enumerate([(80,860),(800,1600)]):
        c=im.crop((l,a,r,b)); c=c.resize((c.width*5//2,c.height*5//2),Image.LANCZOS)
        c.save(d+f'review/work/b{i}_{j}.png')
