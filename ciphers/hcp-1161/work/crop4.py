from PIL import Image
p='hires/cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12_adr.jpg'
im=Image.open(p)
R={'el':(640,1020,1350,1120,3),'tail':(30,1700,1400,1890,2),'pm':(2250,230,2950,860,2),'open':(30,860,1400,990,2)}
for k,b in R.items():
    w,h=b[2]-b[0],b[3]-b[1];s=b[4]
    im.crop(b[:4]).resize((w*s,h*s),Image.LANCZOS).save(f'crops/x{k}.png')
