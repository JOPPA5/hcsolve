from PIL import Image
im=Image.open('hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg').convert('RGB')
r=im.split()[0].point(lambda v:0 if v<75 else (255 if v>150 else int((v-75)*3.4)))
c={'p1':(30,130,1600,480),'p2':(30,460,1600,1000),'p3':(30,1100,1600,1560),'p4':(30,1500,1600,1930)}
for k,b in c.items(): r.crop(b).save('crops/i_%s.png'%k)
r.crop((1400,20,2700,170)).save('crops/i_date.png')
