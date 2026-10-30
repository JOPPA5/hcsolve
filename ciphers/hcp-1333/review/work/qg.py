from PIL import Image
im=Image.open('work/hires/pc_hcp_14_adr.JPG').convert('RGB')
b=[(125,240,175,275),(78,450,122,495),(628,315,708,352),(345,640,430,672),(280,640,345,672),(140,1000,0,0)]
b=b[:5]+[(395,560,450,600)]
W=sum((x1-x0)*5+20 for x0,y0,x1,y1 in b); s=Image.new('RGB',(W,240),'white'); x=0
for x0,y0,x1,y1 in b:
    c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*5,c.height*5),Image.LANCZOS); s.paste(c,(x,0)); x+=c.width+20
s.save('review/work/qg.png'); print(s.size)
