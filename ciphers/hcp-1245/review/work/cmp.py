from PIL import Image, ImageDraw
im=Image.open('../../work/hires/cpc_1912-03-20_HU__HU_Jasz-Arokszalas_jolanka-11_adr.jpg').convert('RGB')
# hires boxes: row7 first sign (claimed sz), row7 second sz, row1 sz, row2 sz, row12 sz, row16 sz, row3 t, row8 t, row5 t
b={'r7 sign2 (disputed)':(165,835,345,965),'r7 leszek sz':(830,840,1020,970),'r1 szerelmem':(530,90,720,200),'r2 szerencse':(980,220,1160,340),
   'r10 aszerelmes':(290,1190,460,1300),'r12 latszik':(620,1400,800,1520),'r3 z of erkeztem':(1000,380,1130,500),'r8 t':(135,960,240,1080),'r9 t':(290,1120,420,1240),'r5 t':(140,710,240,820)}
W=480;H=330;n=len(b);cv=Image.new('RGB',(W*5,(H+24)*2),'white');d=ImageDraw.Draw(cv)
for i,(k,x) in enumerate(b.items()):
    c=im.crop(x);s=min(W/c.width,H/c.height);c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
    X=(i%5)*W;Y=(i//5)*(H+24);cv.paste(c,(X,Y+24));d.text((X+4,Y+6),k,fill='black')
cv.save('cmp_st.png')
