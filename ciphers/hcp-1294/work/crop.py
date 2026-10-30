from PIL import Image
import sys
im=Image.open('work/hires/cpc_1912-03-26_HU__HU_Jasz-Arokszalas_jolanka-12_adr.jpg').convert('RGB')
# display-coord row bands (y0,y1)
rows=[(40,105),(100,170),(170,235),(235,300),(305,395),(380,440),(445,520),(515,585),(580,650),(645,715),(700,770),(765,830),(835,900),(895,985),(1000,1070)]
for i,(a,b) in enumerate(rows,1):
    for j,(x0,x1) in enumerate([(50,500),(460,940)]):
        c=im.crop((int(x0*1.72),int(a*1.72),int(x1*1.72),int(b*1.72)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'work/crops/r{i:02d}_{"ab"[j]}.png')
c=im.crop((2600,250,3150,800)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save('work/crops/stamp.png')
