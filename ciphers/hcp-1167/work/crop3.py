from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
for n,b in {'open':(30,920,860,1110),'addr':(880,330,1740,1060),'pm':(1250,160,1700,450)}.items():
    cr=im.crop(tuple(int(x*s) for x in b))
    if n=='open': cr=cr.resize((int(cr.width*1.2),int(cr.height*1.2)))
    cr.save(f'crops/{n}.png')
