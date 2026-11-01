from PIL import Image
im=Image.open('hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg').convert('RGB')
c={'E1':(20,1920,560,2060),'E2':(520,1920,1000,2060),'E3':(980,1880,1560,2060),
'F1':(20,2020,520,2130),'F2':(500,2010,1040,2130),'F3':(1020,2010,1600,2130),
'B1':(230,1020,800,1140),'B2':(780,1020,1460,1140),'C':(680,1090,1460,1210),'D':(680,1780,1300,1930),'T':(130,30,1250,170)}
for k,b in c.items():
    x=im.crop(b); x=x.resize((x.width*3 if x.width<700 else x.width*2,x.height*3 if x.width<700 else x.height*2),Image.LANCZOS); x.save('crops/z_%s.png'%k)
