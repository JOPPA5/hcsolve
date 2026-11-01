from PIL import Image
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-69_adr.jpg').convert('RGB')
xs=[(1500,2100),(2050,2650),(2600,3200),(2900,3400)]
for c,(x0,x1) in enumerate(xs):
    im.crop((x0,1830,x1,2190)).resize(((x1-x0)*5//2,360*5//2),Image.LANCZOS).save(f'crops/b{c}.jpg',quality=90)
# stamp area
im.crop((2640,230,3180,760)).resize((1350,1325),Image.LANCZOS).save('crops/stamp.jpg',quality=90)
# right edge rotated
r=im.crop((3120,40,3380,1900)).rotate(-90,expand=True)
w,h=r.size
for i,x0 in enumerate(range(0,w,620)):
    r.crop((x0,0,min(w,x0+680),h)).resize((min(w-x0,680)*2,h*2),Image.LANCZOS).save(f'crops/edge{i}.jpg',quality=90)
print(w,h)
