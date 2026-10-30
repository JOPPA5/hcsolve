from PIL import Image, ImageDraw
im=Image.open('hires/pc_hcp_14_adr.JPG').convert('RGB')
ys=[265,330,415,480,540,600,665,725,790,855,915,970,1030,1085]
for part,idx in (('a',range(0,5)),('b',range(5,10)),('c',range(10,14))):
    s=Image.new('RGB',(1660,len(idx)*330),'white');d=ImageDraw.Draw(s)
    for r,i in enumerate(idx):
        y=ys[i]
        c=im.crop((50,y-55,880,y+55)).resize((1660,220*1),Image.LANCZOS) if False else im.crop((50,y-50,880,y+50)).resize((1660,200),Image.LANCZOS)
        Y=r*330+20;s.paste(c,(0,Y));
        d.text((2,Y-16),f'L{i+1} y={y}',fill='red')
        for x in range(50,880,50):
            X=(x-50)*2;d.line((X,Y-6,X,Y),fill='red');d.text((X+2,Y-16),str(x),fill='red')
    s.save(f'resp/strip{part}.png')
