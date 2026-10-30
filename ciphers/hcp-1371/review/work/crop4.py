from PIL import Image
im=Image.open('msg.png')
b={'x_e1':(650,480,720,560),'x_e2':(700,480,810,560),'x_oeje':(590,480,810,590),'x_m':(470,470,560,540)}
for k,v in b.items():
    c=im.crop(v);c=c.resize((c.width*8,c.height*8),Image.LANCZOS);c.save(k+'.png')
o=Image.open('../../work/hires/pc_hcp_52_adr.JPG').convert('RGB')
print(o.size)
c=o.crop((1200,20,1785,420));c=c.resize((c.width*2,c.height*2));c.save('x_post.png')
