from PIL import Image
p='hires/cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12_adr.jpg'
im=Image.open(p)
R={'sig':(780,1985,1200,2110,5),'date':(1200,1950,2300,2130,2),'keh':(30,805,330,900,6)}
for k,b in R.items():
    w,h=b[2]-b[0],b[3]-b[1];s=b[4]
    im.crop(b[:4]).resize((w*s,h*s),Image.BICUBIC).save(f'crops/y{k}.png')
