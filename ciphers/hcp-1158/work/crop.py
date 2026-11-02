from PIL import Image
im=Image.open('hires/cpc_1915--12_HU_Mezokovesd_HU_Szomolya_szomolya-44_adr.jpg').convert('RGB')
f=1.734
bands=[(20,75),(255,350),(350,450),(460,575),(570,700),(695,815),(805,920),(910,1030),(1020,1125),(1115,1205)]
for i,(a,b) in enumerate(bands):
    for j,(l,r) in enumerate([(20,330),(300,620),(590,920)]):
        c=im.crop((int(l*f),int(a*f),int(r*f),int(b*f)))
        c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'crops/b{i}_{j}.png')
c=im.crop((int(760*f),int(440*f),int(870*f),int(730*f))).rotate(-90,expand=True); c=c.resize((c.width*3,c.height*3)); c.save('crops/side.png')
c=im.crop((int(1380*f),int(20*f),int(1890*f),int(190*f))); c=c.resize((c.width*2,c.height*2)); c.save('crops/pm.png')
