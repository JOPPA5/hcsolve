from PIL import Image
src='../../work/hires/cpc_1913-09-13_HU__HU_Jasz-Arokszalas_jolanka-43_adr.jpg'
im=Image.open(src).convert('RGB')
i=0
y=70
while y<2110:
    for side,(a,b) in {'L':(70,830),'R':(790,1600)}.items():
        im.crop((a,y,b,y+235)).resize(((b-a)*5//2,235*5//2),Image.LANCZOS).save(f't{i:02d}{side}.png')
    y+=205;i+=1
im.crop((2740,170,3260,720)).resize((1300,1375),Image.LANCZOS).save('stamp.png')
im.crop((1550,1850,3300,2100)).resize((1750*11//10,275),Image.LANCZOS).save('r2425right.png')
