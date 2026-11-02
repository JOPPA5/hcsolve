from PIL import Image
im=Image.open('hires/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-26_adr.jpg').convert('RGB')
s=1.72
k=0.035
# shear: output(x,y) <- input(x, y - k*x)
W,H=int(1050*s),int(1240*s)
sh=im.crop((0,0,W,H)).transform((W,H),Image.AFFINE,(1,0,0, -k,1,0),Image.BICUBIC)
sh.save('crops/shear.png')
ys=[95,155,215,272,338,395,442,495,547,600,645,692,752,812,870,925,975,1030,1080,1125,1170]
for i,y in enumerate(ys,1):
    for j,(a,b) in enumerate([(40,380),(340,680),(640,1040)]):
        r=sh.crop((int(a*s),int((y-42)*s),int(b*s),int((y+42)*s)))
        r=r.resize((r.width*3,r.height*3),Image.LANCZOS)
        r.save(f'crops/r{i:02d}{"abc"[j]}.png')
# montage per chunk
for start in range(0,21,3):
    for j in 'abc':
        ims=[Image.open(f'crops/r{i:02d}{j}.png') for i in range(start+1,min(start+4,22))]
        w=max(x.width for x in ims); h=sum(x.height for x in ims)+6*len(ims)
        m=Image.new('RGB',(w,h),'white'); y=0
        for x in ims: m.paste(x,(0,y)); y+=x.height+6
        m.save(f'crops/m{start+1:02d}{j}.png')
