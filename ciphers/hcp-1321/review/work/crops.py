from PIL import Image, ImageOps
im=Image.open('../../work/hires/pc_hcp_2_adr.JPG').convert('RGB')
r=im.crop((180,150,930,1100)).rotate(90,expand=True)
def s(n,b,k=8):
    c=r.crop(b); c=ImageOps.autocontrast(c,cutoff=1); c.resize((c.width*k,c.height*k),Image.LANCZOS).save(n+'.png')
s('L1a',(125,220,320,275)); s('L1amp',(385,230,455,275),12); s('L1b',(505,235,685,285))
s('L2a',(120,310,330,370)); s('L2b',(290,320,490,370)); s('L2c',(575,320,840,375),6)
s('L3',(130,405,425,465),6)
s('sig',(280,640,880,740),3); s('struck',(40,70,200,175),6)
s('addr_stamp',(0,0,1,1),1)
a=im.crop((900,250,1785,1100)); a.save('addr.png')
s2=im.crop((1250,80,1785,420)); s2.resize((s2.width*2,s2.height*2),Image.LANCZOS).save('stamp.png')
