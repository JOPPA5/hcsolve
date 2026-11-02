from PIL import Image
im=Image.open('work/hires/cpc_1915-12-28_HU_Mezokovesd_HU_Szomolya_szomolya-13_adr.jpg').convert('RGB')
Z={'z_L2start':(75,1530,300,1640,5),'z_L6us':(280,1790,560,1890,5) ,'z_blot':(60,1690,260,1800,5),
 'z_senki':(830,1520,1120,1640,5),'z_arpad':(1320,1990,1760,2100,4),'z_marg':(1320,50,1640,140,4),
 'z_6end':(800,1680,1000,1800,0)}
for n,(a,b,c,d,s) in Z.items():
    if not s: continue
    r=im.crop((a,b,c,d)); r.resize((r.width*s,r.height*s),Image.LANCZOS).save('review/work/%s.png'%n)
# open text strips
y=[(150,320),(290,460),(430,600),(570,740),(710,880),(850,1020),(990,1160),(1130,1300),(1270,1440)]
for i,(a,b) in enumerate(y):
    r=im.crop((60,a,1640,b)); r.save('review/work/o%d.png'%i)
r=im.crop((60,2040,1400,2180)); r.save('review/work/o_date.png')
