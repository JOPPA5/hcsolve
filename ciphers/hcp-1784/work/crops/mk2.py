from PIL import Image
c=Image.open('crops/rot.png')
# tiles of ambiguous signs at 6x, with contrast
boxes={'L1_2_S':(150,50,220,130),'L6_3_S':(360,725,435,800),'L5_3_x':(235,610,300,680),'L5_6':(495,600,565,670),'L3_2':(120,330,205,400),'L3_5':(455,325,545,395),'L3_6':(595,320,705,400),'L4_1':(195,460,250,540),'L6_1':(155,730,225,810),'L1_5':(475,50,545,115),'L2_3':(400,175,475,240),'L3_1':(20,320,80,395),'L3_4':(355,325,405,390)}
W=7*0+1000
sheet=Image.new('RGB',(1500,1500),'white')
from PIL import ImageDraw
d=ImageDraw.Draw(sheet)
x=y=0
for k,b in boxes.items():
    t=c.crop(b); t=t.resize((t.width*5,t.height*5),Image.LANCZOS)
    if x+t.width>1500: x=0;y+=430
    sheet.paste(t,(x,y+14)); d.text((x+2,y),k,fill='red'); x+=t.width+10
sheet.save('crops/sheet.png')
