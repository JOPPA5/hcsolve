from PIL import Image, ImageOps, ImageEnhance
r=Image.open('work/hires/pc_hcp_28_adr.JPG').rotate(90,expand=True)
s=1.275
z={'hpjoh':(640,890,800,985,6),'e':(420,1095,520,1150,8),'hiu':(730,1090,860,1150,7),'m2':(495,850,620,915,7),'n2':(320,850,400,915,7),
'm7':(445,1205,600,1275,7),'hjsm':(700,1215,860,1290,7),'blot':(790,1230,860,1290,10),'zpvs':(100,1195,290,1290,6),'pxo7':(290,1190,445,1280,6)}
for k,(a,b,c,d,f) in z.items():
  x=r.crop((int(a*s),int(b*s),int(c*s),int(d*s))); x=x.resize((x.width*f,x.height*f),Image.BICUBIC)
  x.save(f'review/work/z_{k}.png'); 
  if k=='blot':
    g=ImageOps.autocontrast(x.convert('L'),cutoff=1); g=ImageEnhance.Contrast(g).enhance(2.0); g.save('review/work/z_blot_c.png')
