from PIL import Image
im=Image.open('work/hires/cpc_1915-12-14_HU_Mezokovesd_HU_Szomolya_szomolya-11_adr.jpg').convert('RGB')
r=im.split()[0].point(lambda v:max(0,min(255,int((v-80)*255/110))))
ys=[400,450,497,550,600,655,720,790,858,930,985,1040,1085,1130,1185]
for i,y in enumerate(ys):
    Y=int(y*1.734);c=r.crop((130,Y-85,1560,Y+85));c=c.resize((c.width*7//5,c.height*7//5),Image.LANCZOS);c.save('review/work/L%02d.png'%(i+7))
