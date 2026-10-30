from PIL import Image, ImageOps, ImageEnhance
im=Image.open('work/hires/cpc_1913-08-31_HU__HU_Jasz-Arokszalas_jolanka-41_adr.jpg').convert('RGB')
sc=1.72
def crop(name,box,z=2):
    b=[int(v*sc) for v in box]
    c=im.crop(b); c=c.resize((c.width*z,c.height*z),Image.LANCZOS)
    c=ImageEnhance.Contrast(ImageOps.autocontrast(c,cutoff=1)).enhance(1.3)
    c.save('work/bands/'+name+'.png')
t=70;i=0
while t<1200:
    h=62 if t<200 else 85
    crop(f'b{i:02d}a',(50,t,480,t+h)); crop(f'b{i:02d}b',(450,t,920,t+h))
    t+= 30 if t<200 else 55; i+=1
print(i)
crop('stamp',(1590,160,1860,450),3)
crop('addr_top',(940,160,1600,320),1)
# per-row bands (display y top, h)
R=[(165,60),(215,60),(262,60),(320,55),(375,60),(432,60),(490,50),(540,60),(595,50),(640,55),(688,55),(735,55),(782,50),(825,50),(870,55),(918,50),(965,50),(1012,55),(1060,55),(1110,40),(1135,55)]
for n,(t,h) in enumerate(R):
    crop(f'r{n:02d}a',(50,t,480,t+h)); crop(f'r{n:02d}b',(450,t,920,t+h))
