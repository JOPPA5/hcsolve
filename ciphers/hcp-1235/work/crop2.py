from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1912--20_HU__HU_Jasz-Arokszalas_jolanka-101_adr.jpg').convert('RGB')
rows={5:(600,690),6:(690,760)}
tops=[60,120,185,250,320,395,460,525,590,650,720,785,845,905,965,1030,1085,1130]
tops=[75,125,190,258,330,400,470,535,590,650,725,795,855,915,975,1030,1088,1135]
for i,t in enumerate(tops,1):
    y0=int((t-12)*1.72); y1=int((t+ (70 if i<18 else 70))*1.72)
    for j,(a,b) in enumerate([(60,600),(560,1050),(1000,1720)]):
        c=im.crop((a,y0,b,y1)); c=ImageEnhance.Contrast(c).enhance(1.4)
        c=c.resize((c.width*3,c.height*3),Image.LANCZOS)
        c.save(f'crops/r{i:02d}_{j}.png')
# montage per row: stacked three segments
for i in range(1,19):
    ims=[Image.open(f'crops/r{i:02d}_{j}.png') for j in range(3)]
    H=sum(x.height for x in ims); W=max(x.width for x in ims)
    m=Image.new('RGB',(W,H),'white'); y=0
    for x in ims: m.paste(x,(0,y)); y+=x.height
    m.save(f'crops/row{i:02d}.png')
