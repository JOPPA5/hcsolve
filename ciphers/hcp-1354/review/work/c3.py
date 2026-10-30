from PIL import Image, ImageOps
im=Image.open('rot.png').convert('RGB')
def cr(b,n,s=6):
    c=ImageOps.autocontrast(im.crop(b),cutoff=1); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(n); return c
A=cr((480,1110,560,1215),'x_i1.png')          # i of ifbejoh + dot
B=cr((670,1020,750,1100),'x_i2.png')          # i of dibohf + dot
C=cr((340,1400,430,1450),'x_s1.png')          # s of sfdfjwfe
D=cr((630,1110,690,1190),'x_j.png')           # j of ifbejoh + dot
E=cr((520,1380,640,1490),'x_j2.png')          # j of sfdfjwfe
W=sum(x.width for x in (A,B,C,D,E))+40; H=max(x.height for x in (A,B,C,D,E))
o=Image.new('RGB',(W,H),'white'); x=0
for p in (A,B,C,D,E): o.paste(p,(x,0)); x+=p.width+10
o.thumbnail((2000,2000)); o.save('x_cmp.png')
cr((560,1470,1000,1590),'x_xiz.png',4)
cr((330,1460,560,1590),'x_left.png',5)
cr((100,330,420,560),'x_post.png',3)
cr((80,1480,240,1660),'x_pencil.png',3)
p=Image.open('../../work/hires/pc_hcp_35_pic.JPG').convert('RGB'); print(p.size)
w,h=p.size; c=p.crop((int(w*.28),int(h*.84),int(w*.78),int(h*.93))); c=ImageOps.autocontrast(c,cutoff=1); c=c.resize((c.width*3,c.height*3)); c.save('x_cap.png')
