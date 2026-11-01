from PIL import Image
f='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1283/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-34_adr.jpg'
im=Image.open(f).convert('RGB').crop((50,40,1540,2110))
s=0.035
sh=im.transform((im.width,im.height+60),Image.AFFINE,(1,0,0,-s,1,0),Image.BICUBIC)
sh.save('sheared.png')
y=0;i=0
while y<sh.height-100:
    for j,(a,b) in enumerate(((0,780),(720,1490))):
        c=sh.crop((a,y,b,y+380)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save('s%02d%s.png'%(i,'ab'[j]))
    y+=340;i+=1
print(i)
