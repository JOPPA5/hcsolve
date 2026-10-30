from PIL import Image, ImageOps
im=Image.open('../../work/hires/pc_hcp_49_adr.JPG').rotate(90,expand=True).convert('L')
B={'Nz':(440,1030,520,1120),'sal':(745,1030,850,1120),'amp':(655,1320,770,1420),'close':(885,1410,1000,1500)}
W=Image.new('L',(1760,1100),255);x=y=0
for i,(k,b) in enumerate(B.items()):
    c=ImageOps.autocontrast(im.crop(b),cutoff=1); c=c.resize((c.width*8,c.height*8),Image.LANCZOS)
    W.paste(c,((i%2)*880,(i//2)*550))
W.save('cmp_N_rev.png')
