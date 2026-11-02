from PIL import Image, ImageOps
import glob
im=Image.open(glob.glob('work/hires/*_adr.jpg')[0]).convert('RGB')
P={'z1_koronabol':(690,1180,1000,1290),'z2_adose':(1270,1170,1480,1280),'z3_egy':(750,1370,920,1480),'z4_jutni':(690,700,880,800),
'z5_anyukad':(560,810,800,900),'z6_ilyen':(980,130,1140,220),'z7_sirig':(2940,1960,3290,2090),'z8_elsz':(1090,1790,1720,1930),'z9_csok':(1040,1960,1400,2080),'z10_ud':(380,1970,560,2070),'z11_ral':(30,1500,300,1610),'z12_ritkan':(120,220,420,330)}
W=[]
for n,b in P.items():
    x=im.crop(b); x=x.resize((x.width*4,x.height*4),Image.BICUBIC); x=ImageOps.autocontrast(x,cutoff=0.3); x.save(f'work/crops/{n}.png'); W.append(x)
# contact sheet
y=0; H=sum(i.height+10 for i in W[:6]); s=Image.new('RGB',(1400,H),'white')
for i in W[:6]: s.paste(i.crop((0,0,1400,i.height)),(0,y)); y+=i.height+10
s.save('work/crops/sheet1.png')
y=0; H=sum(i.height+10 for i in W[6:]); s=Image.new('RGB',(2600,H),'white')
for i in W[6:]: s.paste(i,(0,y)); y+=i.height+10
s.save('work/crops/sheet2.png')
