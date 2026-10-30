from PIL import Image
im=Image.open('../../work/hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg').convert('RGB')
F=3445/1024
B=[('r17 first',24,530,70,565),('r08 j',24,235,70,272),('r13 j',100,395,150,428),('r03 j',115,85,165,115),('r07 f',24,205,70,240),('r16 f',325,495,375,530),('s6 f',0,0,0,0)]
B=B[:-1]
W=[]
for n,a,b,c,d in B:
    r=im.crop((int(a*F),int(b*F),int(c*F),int(d*F)));W.append(r.resize((r.width*3,r.height*3),Image.LANCZOS))
W2=sum(i.width+12 for i in W);H=max(i.height for i in W)
m=Image.new('RGB',(W2,H),'white');x=0
for i in W: m.paste(i,(x,0));x+=i.width+12
m.save('crops/z_jf_compare.png');print(m.size)
