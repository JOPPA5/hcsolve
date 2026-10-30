from PIL import Image, ImageDraw
im=Image.open('work/hires/cpc_--22_HU__HU_Jasz-Arokszalas_jolanka-87_adr.jpg').convert('RGB')
Z={'z_r2end':(1440,120,1640,230),'z_r4de':(800,250,1000,350),'z_r10end':(1180,650,1420,730),'z_r18o':(420,1215,620,1310),
'z_r28S':(640,1950,860,2040),'z_r29vale':(1230,2020,1470,2110),'z_r12':(60,830,240,920),'z_r8t':(900,500,1060,590),
'z_r17merr':(1240,1170,1460,1250),'z_r4m':(1240,250,1420,330),'z_r27el':(150,1890,330,1960),'z_r7':(1040,450,1180,520),
'z_r8d':(820,510,940,590),'z_r22a':(860,1510,1020,1590),'z_r29end':(3000,2020,3320,2100),'z_r4blot':(1330,250,1480,330)}
for k,b in Z.items():
    c=im.crop(b); s=5 if c.width<260 else 4; c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'review/work/c/{k}.png')
names=list(Z)
for gi in range(0,len(names),4):
    g=names[gi:gi+4]; ims=[Image.open(f'review/work/c/{n}.png') for n in g]
    W=max(i.width for i in ims)*2+10; H=sum(max(ims[j].height,ims[j+1].height if j+1<len(ims) else 0)+24 for j in range(0,len(ims),2))
    m=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(m);y=0
    for j in range(0,len(ims),2):
        x=0
        for q in range(j,min(j+2,len(ims))):
            d.text((x+2,y+4),g[q],fill='black');m.paste(ims[q],(x,y+20));x+=W//2
        y+=max(ims[j].height,ims[j+1].height if j+1<len(ims) else 0)+24
    m.save(f'review/work/c/m{gi//4}.png');print(m.size)
