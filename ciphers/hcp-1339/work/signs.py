# 6x crops of the doubtful signs on hcp-1339, from the un-converted original.
from PIL import Image, ImageOps
im=Image.open('work/hires/pc_hcp_20_adr.JPG').convert('RGB')
boxes={'L1s3_4':(395,420,540,520),'L2s4':(460,530,540,640),'L3s1_2':(195,665,345,780),'L3s7_8':(610,670,800,760),'L4s2':(270,775,330,870),'L4s6_7':(570,770,690,860),'L5s1':(190,875,260,980)}
ims=[]
for k,b in boxes.items():
    c=im.crop(b); c=ImageOps.autocontrast(c,cutoff=1).resize((c.width*5,c.height*5),Image.LANCZOS); ims.append(c)
W=1800;x=y=0;row=0
s=Image.new('RGB',(W,1200),'white')
for c in ims:
    if x+c.width>W: x=0;y+=row+15;row=0
    s.paste(c,(x,y));x+=c.width+15;row=max(row,c.height)
s.crop((0,0,W,y+row)).save('work/crops/doubtful.png')
