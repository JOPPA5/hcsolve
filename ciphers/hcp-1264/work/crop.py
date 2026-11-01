from PIL import Image
import sys
im=Image.open('hires/cpc_-02-04_HU__HU_Jasz-Arokszalas_jolanka-93_adr.jpg').convert('RGB')
s=1.72
# (name, x0,y0,x1,y1 display coords)
y=[50,175,300,425,550,675,800,925,1050,1215]
for i in range(len(y)-1):
    for j,(a,b) in enumerate([(35,490),(450,940)]):
        c=im.crop((int(a*s),int(y[i]*s),int(b*s),int((y[i+1]+15)*s)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'crops/b{i}{"ab"[j]}.png')
c=im.crop((int(1590*s),int(165*s),int(1860*s),int(460*s)));c=c.resize((c.width*3,c.height*3),Image.LANCZOS);c.save('crops/stamp.png')
