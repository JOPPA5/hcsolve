from PIL import Image, ImageOps
im=Image.open('hires/cpc_1915-11-29_HU_Mezokovesd_HU_Szomolya_szomolya-07_adr.jpg').convert('RGB')
cr={'y1':(1200,1380,1600,1500,5),'y2':(1050,750,1560,860,4),'y3':(230,2070,1000,2170,4),'y4':(1450,2060,1760,2170,5),'y5':(480,1760,900,1860,4),'y6':(2650,20,3200,110,3),
'y7':(780,1440,1000,1560,6),'y8':(40,1300,420,1420,5)}
for k,(x0,y0,x1,y1,s) in cr.items():
    c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c=ImageOps.autocontrast(c,cutoff=1); c.save(f'crops/{k}.png')
