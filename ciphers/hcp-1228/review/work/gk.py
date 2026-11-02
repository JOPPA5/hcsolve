from PIL import Image, ImageDraw
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1228/'
im=Image.open(base+'work/hires/cpc_1913-09-07_HU__HU_Jasz-Arokszalas_jolanka-42_adr.jpg').convert('RGB')
# (label, cx, cy) centres in hires pixels located from p*.png page crops
S=[('g r02 hogy',(1330-0)/2.4+60,290/2.4+90),('g r08 igy',190/2.4+60,510/2.4+400),('g r09 magan',1360/2.4+820,640/2.4+400),
('g r12 meg?',1860/2.4+60,-1+700/2.4+710-250),('g r23 hogy',375/2.4+820,240/2.4+1640),('g r23 megnez',1060/2.4+820,190/2.4+1640),('g r24 meges',640/2.4+820,430/2.4+1640),('g r26 sirig',745/2.4+60,370/2.4+1830),
('? r14 menyeg',660+1150/3.5-0,1030+130/3.5),
('k r02 kiv',75/2.4+60,240/2.4+90),('k r04 kilo',65/2.4+820,600/2.4+90),('k r08 csak',1600/2.4+820,420/2.4+400),('k r09 kell',75/2.4+60,700/2.4+400),('k r14 nek',660+1760/3.5-20,1030+80/3.5),('k r21 nak',1470/2.4+60,630/2.4+1330),('k r24 esek',1170/2.4+820,420/2.4+1640),('k r26 kedv',1285/2.4+60,370/2.4+1830)]
W,H=170,170;cols=6;rows=(len(S)+cols-1)//cols
M=Image.new('RGB',(cols*W,rows*(H+18)),'white');d=ImageDraw.Draw(M)
for i,(l,x,y) in enumerate(S):
    c=im.crop((int(x-42),int(y-42),int(x+42),int(y+42))).resize((W,H),Image.LANCZOS)
    X,Y=(i%cols)*W,(i//cols)*(H+18);M.paste(c,(X,Y+18));d.text((X+3,Y+3),l,fill='red')
M.save(base+'review/work/gk.png')
