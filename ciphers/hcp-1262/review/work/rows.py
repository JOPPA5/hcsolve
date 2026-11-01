from PIL import Image
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1262/review/work/crops/'
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1262/work/hires/cpc_1912--15_HU__HU_Jasz-Arokszalas_jolanka-100_adr.jpg').convert('RGB')
cs=[50,85,118,150,185,212,250,285,335,365,398,430,462,495,527,560,590,617]
def crop(b,s): c=im.crop(b); return c.resize((c.width*s,c.height*s),Image.LANCZOS)
groups=[(0,4),(4,8),(8,12),(12,15),(15,18)]
for gi,(a,b) in enumerate(groups):
  for side,(x0,x1) in {'L':(80,880),'R':(840,1680)}.items():
    rs=[crop((x0,c*337//100-75,x1,c*337//100+75),2) for c in cs[a:b]]
    m=Image.new('RGB',(rs[0].width,sum(r.height+6 for r in rs)),'white');y=0
    for r in rs: m.paste(r,(0,y)); y+=r.height+6
    m.save(d+f'm{gi+1}{side}.png')
crop((2740,220,3220,780),3).save(d+'stamp.png')
