from PIL import Image
import os
os.chdir('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1174')
im=Image.open('work/hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg').convert('RGB')
B=(760,1170,1420,1300)
c=im.crop(B); c.resize((c.width*3,c.height*3),Image.LANCZOS).save('work/crops/l_rgb.png')
r=c.split()[0]
lo=min(r.getdata());
r.point(lambda v:0 if v<60 else (255 if v>135 else int((v-60)*3.4))).resize((c.width*3,c.height*3),Image.LANCZOS).save('work/crops/l_red.png')
c2=im.crop((800,1180,1120,1295)); c2.resize((c2.width*5,c2.height*5),Image.LANCZOS).save('work/crops/l_vagi5.png')
c3=im.crop((1100,1180,1420,1295)); c3.resize((c3.width*5,c3.height*5),Image.LANCZOS).save('work/crops/l_altal5.png')
# fellow 'g' and 'a', 'n' reference: 'Margitka' not open; use 'vagyis' 'mehettem'
