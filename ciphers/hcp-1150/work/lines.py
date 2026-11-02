from PIL import Image
src='work/hires/cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40_adr.jpg'
im=Image.open(src).convert('RGB')
ys=[130,225,320,423,518,610,718,813,908,1060,1162,1273,1372,1524,1625,1710,1812,1890,1985,2066]
for i,y in enumerate(ys,1):
    for n,(a,b) in enumerate([(20,620),(560,1160),(1100,1720)]):
        c=im.crop((a,y-85,b,y+95));c=c.resize((c.width*5//2,c.height*5//2),Image.LANCZOS);c.save('work/crops/n%02d%s.png'%(i,'abc'[n]))
