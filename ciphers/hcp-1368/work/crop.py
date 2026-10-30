import sys
from PIL import Image, ImageOps, ImageEnhance
im=Image.open('work/hires/pc_hcp_49_adr.JPG').convert('RGB').rotate(90,expand=True)
print(im.size)
# rotated: x'=y, y'=W-x
W=1785
def c(name,x0,y0,x1,y1,s=3):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r=ImageEnhance.Contrast(r).enhance(1.6); r.save('work/crops/%s.png'%name)
im.crop((60,900,1100,1730)).save('work/crops/reading.png')
for i,(a,b) in enumerate([(100,520),(480,900)]):
    pass
y=[(980,1140),(1120,1260),(1250,1400),(1380,1530),(1500,1720)]
for i,(a,b) in enumerate(y):
    c('l%da'%i,80,a,600,b,3); c('l%db'%i,560,a,1100,b,3)
# offsets: reading.png origin (60,900)
def R(name,x0,y0,x1,y1,s=4): c(name,x0+60,y0+900,x1+60,y1+900,s)
R('r_head',370,30,970,130,3)
R('r_l2',370,125,1020,225,3)
R('r_l3a',370,220,690,340,4)
R('r_l3b',660,235,1030,310,4)
R('r_l4a',390,320,720,450,4)
R('r_l4b',700,350,1030,430,4)
R('r_l5a',380,430,620,560,4)
R('r_l5b',590,410,1000,520,4)
R('r_l6a',390,510,700,630,4)
R('r_l6b',660,520,1030,610,4)
R('r_l7',630,600,970,730,4)
R('z_cards',800,240,1000,305,8)
# N comparison: (line2 Nz), (line2 NL), (line5 N), (line6 NL)
sheet=Image.new('RGB',(1500,1000),'white')
boxes=[(385,130,500,215),(675,125,830,215),(600,430,720,520),(840,530,1010,600)]
y=0
for b in boxes:
    r=im.crop((b[0]+60,b[1]+900,b[2]+60,b[3]+900)); r=r.resize((r.width*3,r.height*3),Image.LANCZOS); sheet.paste(r,(0,y)); y+=250
sheet.crop((0,0,560,1000)).save('work/crops/cmp_N.png')
R('z_dot_t',880,450,1000,520,8)
R('z_gi',690,630,860,700,8) 
