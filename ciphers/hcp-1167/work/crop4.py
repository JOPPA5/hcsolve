from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
# name:(x0,y0,x1,y1) thumb coords
B={'lehet7':(560,325,840,370),'lehem9':(540,420,780,470),'hacsak':(540,420,680,470),'szoval':(40,570,240,625),'felm':(490,465,820,520),'rara':(760,270,850,315),'tudja':(100,320,220,370),'husege':(60,830,230,880),'soraimat':(40,670,240,725),'udv':(390,715,560,770),'mpm':(40,420,60,470)}
for n,b in B.items():
    cr=im.crop(tuple(int(x*s) for x in b))
    cr=cr.resize((cr.width*4,cr.height*4),Image.LANCZOS); cr.save(f'crops/z_{n}.png')
