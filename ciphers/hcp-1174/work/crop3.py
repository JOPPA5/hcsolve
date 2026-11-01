from PIL import Image
im=Image.open('hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg').convert('RGB')
c={'N':(780,1890,1230,2010),'L':(1380,1990,1680,2110),'FB':(370,2030,640,2130)}
for k,b in c.items():
    x=im.crop(b); x=x.resize((x.width*4,x.height*4),Image.BICUBIC); x.save('crops/y_%s.png'%k)
