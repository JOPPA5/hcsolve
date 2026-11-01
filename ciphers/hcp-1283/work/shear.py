from PIL import Image, ImageDraw
f='ciphers/hcp-1283/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-34_adr.jpg'
im=Image.open(f).convert('RGB').crop((50,40,1520,2110))
s=0.035
sh=im.transform((im.width,im.height+60),Image.AFFINE,(1,0,0,-s*0+0,1,0),Image.BICUBIC) if 0 else im.transform((im.width,im.height+60),Image.AFFINE,(1,0,0,-s,1,-30+30),Image.BICUBIC)
sh.save('ciphers/hcp-1283/work/crops/sheared.png'); print(sh.size)
sh2=sh.resize((sh.width*2,sh.height*2),Image.LANCZOS)
d=ImageDraw.Draw(sh2)
i=0;y=0
while y<sh2.height-100:
    for j,(a,b) in enumerate(((0,1540),(1400,2940))):
        c=sh2.crop((a,y,b,y+460)); c.save('ciphers/hcp-1283/work/crops/T%02d%s.png'%(i,'ab'[j]))
    y+=400;i+=1
print(i)
