from PIL import Image
P='work/hires/cpc_1912-03-26_HU__HU_Jasz-Arokszalas_jolanka-12_adr.jpg'
im=Image.open(P).convert('RGB')
W=1700
rows=[(60,190),(170,300),(285,410),(400,525),(520,690),(650,770),(760,900),(880,1020),(990,1125),(1100,1235),(1200,1330),(1310,1435),(1430,1555),(1540,1700),(1710,1850)]
for i,(a,b) in enumerate(rows,1):
    im.crop((60,a,1650,b)).save(f'work/crops2/row{i:02d}.png')
