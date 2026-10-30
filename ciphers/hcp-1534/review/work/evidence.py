from PIL import Image, ImageDraw
up=Image.open('upright.png')
boxes=[("S13 t3s484n DOCILIM (solver: t3c6rm2 DOSAHNU)",(555,578,636,608)),
       ("L02 2bh4nm1H UPRIMNYCH (solver: 284pm1H ULIBNYCH)",(300,928,420,964)),
       ("L03 f5sm5 VECNE (solver: f5hm5 VERNE)",(30,952,110,984)),
       ("L04 qbh6f2 ZPRAVU (solver: q6p6f2 ZABAVU)",(28,974,110,1004)),
       ("U02 overinked n + m5 = MNE",(380,80,430,112)),
       ("S01 f6cg5h4 VASKERI (first vowel 6 vs 5 ambiguous)",(485,240,580,278))]
S=7; ims=[]
for lab,b in boxes:
    c=up.crop(b); c=c.resize((c.width*S,c.height*S),Image.LANCZOS)
    canvas=Image.new('RGB',(max(c.width,700),c.height+24),'white'); canvas.paste(c,(0,24))
    ImageDraw.Draw(canvas).text((4,4),lab,fill='black'); ims.append(canvas)
W=max(i.width for i in ims); H=sum(i.height+8 for i in ims)
out=Image.new('RGB',(W,H),'white'); y=0
for i in ims: out.paste(i,(0,y)); y+=i.height+8
out.save('review1-evidence.png')
