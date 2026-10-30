from PIL import Image, ImageOps, ImageChops, ImageDraw
r=Image.open('adr_ccw.png').convert('RGB')
boxes={'line1 end sign':(815,960,985,1080),'z of Nz':(435,975,500,1040),'z of Cpz':(1000,1010,1080,1060),'s gspn':(805,1390,880,1450),'s Hjsm':(880,1570,960,1640),'h line6':(820,1470,890,1560),'s gps':(490,1180,550,1230)}
s=5
for n,b in boxes.items():
    c=r.crop(b); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); ImageOps.autocontrast(c,cutoff=1).save('cmp_'+n.replace(' ','_')+'.png')
ims=[Image.open('cmp_'+n.replace(' ','_')+'.png') for n in boxes]
W=sum(i.width for i in ims)+10*len(ims);H=max(i.height for i in ims)
o=Image.new('RGB',(W,H),'white');x=0
for i in ims:o.paste(i,(x,0));x+=i.width+10
o.thumbnail((2000,2000));o.save('cmp_all.png')
