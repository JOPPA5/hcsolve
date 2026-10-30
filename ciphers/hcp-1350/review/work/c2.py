from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1350/work/hires/pc_hcp_31_adr.JPG').rotate(90,expand=True)
ims={'x_pxo':(510,1040,570,1085),'x_xibu':(330,1125,400,1175),'w_wfsz':(350,1395,430,1440),'w_mpwjoh':(480,1500,540,1530),'v_vofy':(715,1130,770,1180)}
W=Image.new('RGB',(1200,1100),'white');y=0
for k,b in ims.items():
    c=im.crop(b);c=c.resize((c.width*5,c.height*5),Image.LANCZOS);W.paste(c,(0,y));y+=c.height+10;print(k,c.size)
W.save('cmp.png')
c=im.crop((470,1200,700,1330));c.resize((c.width*7,c.height*7),Image.LANCZOS).save('z3.png')
