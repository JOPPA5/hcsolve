from PIL import Image
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-73_adr.jpg')
# hires row bands, overlapping
rows=[(60,420),(400,760),(740,1100),(1080,1440),(1420,1780),(1760,2130)]
for i,(a,b) in enumerate(rows):
    for j,(x0,x1) in enumerate([(70,1000),(950,1880)]):
        im.crop((x0,a,x1,b)).resize(((x1-x0)*2,(b-a)*2),Image.LANCZOS).save(f'review/work/b{i}{"LR"[j]}.png')
im.crop((1800,1900,3300,2130)).resize((3000,460)).save('review/work/br.png')
im.crop((2700,230,3200,780)).resize((1000,1100)).save('review/work/stamp.png')
