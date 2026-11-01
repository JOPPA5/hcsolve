from PIL import Image
adr=Image.open('work/hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg').convert('RGB')
B={'r_salut':(170,30,1300,170),'r_ha':(60,1030,1500,1150),'r_arcom':(600,1110,1500,1240),
   'r_mondd':(60,1800,1000,1930),'r_b1a':(40,1900,800,2020),'r_b1b':(750,1880,1560,2010),'r_b2a':(40,1960,800,2100),'r_b2b':(750,1960,1560,2110)}
for k,b in B.items():
    c=adr.crop(b); c.resize((c.width*2,c.height*2),Image.LANCZOS).save('review/work/%s.png'%k)
