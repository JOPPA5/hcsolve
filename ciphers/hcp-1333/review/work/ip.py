from PIL import Image
im=Image.open('work/hires/pc_hcp_14_adr.JPG').convert('RGB')
b=[(195,240,240,290),(262,240,312,290),(545,1000,600,1055),(618,1055,672,1105),(690,385,750,450),(235,395,300,450)]
s=Image.new('RGB',(sum((x1-x0)*5+20 for x0,y0,x1,y1 in b),330),'white'); x=0
for B in b:
    c=im.crop(B); c=c.resize((c.width*5,c.height*5),Image.LANCZOS); s.paste(c,(x,0)); x+=c.width+20
s.save('review/work/ip.png')
