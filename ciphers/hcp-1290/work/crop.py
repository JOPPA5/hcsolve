from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_-02-_HU__HU_Jasz-Arokszalas_jolanka-92_adr.jpg').convert('RGB')
print(im.size)
# Overlapping tiles of text block, x 90-1620, y 55-2100
n=0
y=50
while y<2090:
    for i,x in enumerate((90,800)):
        c=im.crop((x,y,x+820,y+350))
        c=ImageEnhance.Contrast(c).enhance(1.6).resize((1640,700),Image.LANCZOS)
        c.save(f'crops/t{n:02d}{"LR"[i]}.jpg',quality=88)
    n+=1; y+=300
print(n)
c=im.crop((2650,200,3250,800)); c.resize((1200,1200),Image.LANCZOS).save('crops/stamp.jpg')
