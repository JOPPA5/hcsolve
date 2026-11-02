from PIL import Image
src='work/hires/cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40_adr.jpg'
im=Image.open(src).convert('RGB')
y=20;i=0
while y<800:
    for n,(a,b) in enumerate([(1620,2220),(2100,2700)]):
        c=im.crop((a,y,b,y+240));c=c.resize((c.width*5//2,c.height*5//2),Image.LANCZOS);c.save('work/crops/r%d%s.png'%(i,'ab'[n]))
    y+=190;i+=1
print(i)
