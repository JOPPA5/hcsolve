from PIL import Image, ImageOps
im=Image.open('hires/cpc_1913-09-19_HU__HU_Jasz-Arokszalas_jolanka-44_adr.jpg').convert('RGB')
# left panel strips, x 90..1620, in overlapping y bands
W=im.size
ys=list(range(60,2100,190))
for i,y in enumerate(ys):
    for j,(a,b) in enumerate([(90,860),(800,1640)]):
        c=im.crop((a,y,b,y+240)).resize(((b-a)*2,480),Image.LANCZOS)
        c=ImageOps.autocontrast(c,cutoff=1)
        c.save(f'crops/b{i:02d}{"ab"[j]}.png')
print(len(ys))
