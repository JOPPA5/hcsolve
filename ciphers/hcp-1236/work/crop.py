from PIL import Image
im=Image.open('hires/cpc_1912--22_HU__HU_Jasz-Arokszalas_jolanka-102_adr.jpg').convert('RGB')
# rows tops in large-scale y
s=3445/1024
tops=[20,58,95,132,172,208,240,275,312,345,385,425,460,495,535,572,600]
for i in range(len(tops)-1):
    y0=int((tops[i]-2)*s); y1=int((tops[i+1]+10)*s)
    for j,(a,b) in enumerate([(15,260),(240,505)]):
        c=im.crop((int(a*s),y0,int(b*s),y1)); c=c.resize((c.width*2//1,c.height*2//1),Image.LANCZOS) if False else c
        c.save(f'crops/r{i+1:02d}_{j}.png')
c=im.crop((int(830*s),int(40*s),int(980*s),int(190*s))); c.save('crops/stamp.png')
c=im.crop((0,int(585*s),int(600*s),int(657*s))); c.save('crops/bottom.png')
