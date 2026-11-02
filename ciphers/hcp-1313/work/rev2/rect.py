from PIL import Image, ImageDraw
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/'
enh=Image.open(W+'crops/enh_full.png')
rows={6:(745,808),7:(885,920),8:(1013,1033),9:(1133,1143),10:(1255,1262)}
for n,(a,b) in rows.items():
    m=(b-a)/1400
    for k,x0 in enumerate(range(50,1650,520)):
        w=580;h=170
        y0=a+m*(x0-100)-h/2
        c=enh.transform((w,h),Image.AFFINE,(1,0,x0,m,1,y0),Image.BICUBIC).resize((w*3,h*3),Image.LANCZOS).convert('L')
        d=ImageDraw.Draw(c)
        for t in range(0,w,100): d.text((t*3+2,2),str(x0+t),fill=0)
        c.save(W+f'rev2/R{n}_{k}.png')
