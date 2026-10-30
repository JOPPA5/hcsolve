from PIL import Image, ImageOps
a=Image.open('work/hires/pc_hcp_12_adr.JPG').convert('RGB').rotate(90,expand=True)
S=1785/1600
reg={'l1':(270,960,700,1050,4),'l2':(270,1040,970,1110,3),'l3':(270,1105,970,1200,3),
'l3b':(600,1110,970,1195,5),
'l4a':(260,1190,620,1270,5),'l4b':(600,1190,970,1270,5),'l5':(260,1250,970,1340,3),'l6':(240,1320,970,1420,3),
'l7':(230,1400,870,1480,3),'l8':(80,1450,780,1530,3),'l9':(70,1500,780,1570,3),
'stamp':(170,100,420,520,3)}
for k,(x0,y0,x1,y1,z) in reg.items():
    c=a.crop(tuple(int(v*S) for v in (x0,y0,x1,y1)))
    c=c.resize((c.width*z,c.height*z),Image.LANCZOS); ImageOps.autocontrast(c,cutoff=0.5).save(f'review/work/{k}.png'); print(k,c.size)
