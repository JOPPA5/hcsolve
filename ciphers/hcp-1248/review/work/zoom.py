from PIL import Image
im=Image.open('../../work/hires/cpc_1913-09-13_HU__HU_Jasz-Arokszalas_jolanka-43_adr.jpg').convert('RGB')
C={'z_r10_ttan':(1240,760,1570,870),'z_r13_mijen':(70,1080,420,1180),'z_r12_first':(80,905,230,1010),'z_r18_itt':(80,1400,420,1500),'z_r18_end':(1330,1370,1620,1480),'z_r20_lann':(640,1570,820,1670),'z_r9_azt':(1330,690,1520,770),'z_r6_end':(1380,465,1520,535)}
s=5
for k,b in C.items():
    c=im.crop(b); c.resize((c.width*s,c.height*s),Image.LANCZOS).save(k+'.png')
# montage of all
W=1700; tiles=[Image.open(k+'.png') for k in C]
for k,t in zip(C,tiles): pass
post=im.crop((2300,200,3150,1000)); post.resize((1275,1200),Image.LANCZOS).save('z_postmark.png')
