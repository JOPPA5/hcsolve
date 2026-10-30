from PIL import Image
im=Image.open('work/hires/cpc_1912-05-15_HU__HU_Jasz-Arokszalas_jolanka-21_adr.jpg').convert('RGB')
# bands of ~3 rows, three columns, 3x
ys=[(50,290),(230,470),(410,650),(590,830),(770,1010),(950,1190),(1130,1370),(1310,1550),(1490,1730),(1670,1910),(1850,2110)]
for i,(a,b) in enumerate(ys):
    for j,(l,r) in enumerate([(60,640),(590,1170),(1120,1720)]):
        c=im.crop((l,a,r,b)); c.resize((c.width*3,c.height*3),Image.LANCZOS).save(f'review/work/crops/r{i:02d}{"abc"[j]}.png')
