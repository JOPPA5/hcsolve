from PIL import Image
im=Image.open('work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-113_adr.jpg').convert('RGB')
f=2.026
ys=[(40,175),(145,285),(255,395),(370,535),(500,650),(630,770),(750,890),(860,1020)]
for i,(a,b) in enumerate(ys):
    for j,(l,r) in enumerate([(30,300),(270,540),(510,780)]):
        c=im.crop((int(l*f),int(a*f),int(r*f),int(b*f)))
        c=c.resize((int(c.width*2.6),int(c.height*2.6)),Image.LANCZOS)
        c.save(f'review/work/b{i}_{j}.png')
c=im.crop((2750,100,3100,600)); c.resize((1050,1500),Image.LANCZOS).save('review/work/corner.png')
