from PIL import Image, ImageOps
im=Image.open('work/hires/cpc_1915-12-28_HU_Mezokovesd_HU_Szomolya_szomolya-13_adr.jpg').convert('RGB')
b={'y_kam':(1300,60,1640,170),'y_blob':(60,1700,300,1800),'y_tagy':(600,440,1100,560),'y_rama':(40,1000,1700,1100),
'y_slav':(60,430,1000,520),'y_mar':(40,1960,560,2060),'y_mar2':(40,1920,800,2030),'y_most':(40,1370,1700,1480),'y_bev':(950,1090,1700,1180)}
b={'y_kam':(1300,60,1640,170),'y_blob':(60,1700,300,1800),'y_tagy':(40,420,1150,540),'y_rama':(40,860,1700,960),'y_slav':(40,340,1100,440),'y_most':(40,1370,1700,1470),'y_mar2':(40,1990,800,2090),'y_bev':(40,850,1700,960)}
for n,bx in b.items():
    r=im.crop(bx); s=2 if bx[2]-bx[0]>900 else 4; r.resize((r.width*s,r.height*s),Image.LANCZOS).save(f'work/crops/{n}.png')
