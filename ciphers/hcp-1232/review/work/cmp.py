from PIL import Image
im=Image.open('../../work/hires/cpc_--24_HU__HU_Jasz-Arokszalas_jolanka-89_adr.jpg').convert('RGB')
# (label is order) reviewer sign comparison: row22 disputed sign, z signs r21/r10, v signs r07/r17/r09
boxes=[(480,1865,630,1965),(530,1790,640,1880),(120,1680,230,1790) ,(120,1680,230,1790),(1130,590,1290,700)]
boxes=[(495,1865,625,1965), # r22 disputed
       (510,1790,630,1890), # r21 z (s z o)
       (125,920,240,1005),  # r10 z
       (1225,1680,1335,1790),# placeholder
       (1210,570,1300,660), # r07 v
       (190,800,265,880)]   # r09 v
W=sum((b[2]-b[0])*4+20 for b in boxes);H=max((b[3]-b[1])*4 for b in boxes)
o=Image.new('RGB',(W,H),'white');x=0
for b in boxes:
    c=im.crop(b);c=c.resize((c.width*4,c.height*4),Image.LANCZOS);o.paste(c,(x,0));x+=c.width+20
o.save('crops/cmp.png')
