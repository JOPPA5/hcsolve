from PIL import Image
im=Image.open('hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg')
f=1.72
C=[('z15',50,880,480,970),('z15b',440,880,920,970),('z16',50,960,500,1040),('z16b',480,960,930,1040),('z14',50,820,480,900),('z14b',460,820,900,900),('z13',50,770,480,840),('z13b',470,770,900,840)]
C+=[('z01',60,50,500,120),('z03',50,180,500,250),('z03b',440,170,860,250),('z05',50,290,480,350),('z05b',460,290,860,350),('z06',50,340,480,410),('z06b',460,340,860,420),('z07',50,405,480,470),('z07b',460,405,860,470),('z08',50,450,480,510),('z08b',460,450,900,510),('z09',50,510,480,600),('z12',50,710,500,780),('z12b',480,710,900,780),('z11',50,650,480,720),('z11b',460,650,900,720)]
for n,a,b,c,d in C:
    r=im.crop((int(a*f),int(b*f),int(c*f),int(d*f)));r=r.resize((r.width*5//2,r.height*5//2),Image.LANCZOS);r.save(f'crops/{n}.png')
# montages
def mont(names,out):
    ims=[Image.open(f'crops/{n}.png') for n in names]
    W=max(i.width for i in ims);H=sum(i.height+8 for i in ims)
    m=Image.new('RGB',(W,H),'white');y=0
    for i in ims: m.paste(i,(0,y));y+=i.height+8
    m.save(f'crops/{out}.png')
mont(['z13','z14','z15','z16'],'mA');mont(['z13b','z14b','z15b','z16b'],'mB')
mont(['z01','z03','z05','z06'],'mC');mont(['z03b','z05b','z06b'],'mD')
mont(['z07','z08','z09'],'mE');mont(['z07b','z08b'],'mF');mont(['z11','z12'],'mG');mont(['z11b','z12b'],'mH')
