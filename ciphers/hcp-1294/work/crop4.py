from PIL import Image, ImageOps, ImageEnhance
P='work/hires/cpc_1912-03-26_HU__HU_Jasz-Arokszalas_jolanka-12_adr.jpg'
im=Image.open(P).convert('RGB')
# row 8 cipher part x 560..1600, split in two; green channel with autocontrast, 3x
for name,box in {'r8g_a':(560,870,1090,1030),'r8g_b':(1040,870,1600,1030)}.items():
    c=im.crop(box).getchannel('G'); c=ImageOps.autocontrast(c,cutoff=1)
    c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'work/crops2/{name}.png')
# stamp lines
c=im.crop((2600,250,3150,800)).getchannel('B'); c=ImageOps.autocontrast(c,cutoff=1); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save('work/crops2/stamp_b.png')
