from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1828/work/hires/pc_hcp_509_adr.JPG').convert('RGB')
s=1785/1014
x,y=127,592
c=im.crop((int((x-20)*s),int((y-26)*s),int((x+40)*s),int((y+26)*s)))
r=c.split()[0]; r=r.point(lambda v:0 if v<90 else min(255,int((v-90)*255/120)))
W=Image.new('L',(c.width*10,c.height*5*2+10),255)
W.paste(c.convert('L').resize((c.width*5,c.height*5),Image.BICUBIC),(0,0))
W.paste(r.resize((c.width*5,c.height*5),Image.BICUBIC),(0,c.height*5+10))
W=W.crop((0,0,c.width*5,W.height)); W.save('crops/r10_redchannel.png')
f=im.crop((int(35*s),int(70*s),int(350*s),int(150*s))); f=f.resize((f.width*2,f.height*2)); f.save('crops/flourish.png')
