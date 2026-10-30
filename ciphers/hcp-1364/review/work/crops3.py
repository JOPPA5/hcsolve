from PIL import Image, ImageOps
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1364/'
r=Image.open(d+'work/hires/pc_hcp_45_adr.JPG').convert('RGB').rotate(90,expand=True)
# coordinates derived from crops2 at 4x
b={'n_nz':(372,985,440,1060),'n_l1':(705,985,795,1065),'n_l4':(845,1285,935,1375),'m_lett':(362,1095,450,1160),
 'cap_end':(960,975,1060,1075),'minims':(495,1105,620,1160),'m_hjsm':(695,1445,790,1500)}
ims=[]
for k,v in b.items():
    c=r.crop(v);c=c.resize((c.width*7,c.height*7),Image.LANCZOS);c=ImageOps.autocontrast(c,cutoff=1);c.save(d+'review/work/%s.png'%k);ims.append(c)
W=sum(i.width for i in ims[:4])+60;H=max(i.height for i in ims[:4])
s=Image.new('RGB',(W,H),'white');x=0
for i in ims[:4]: s.paste(i,(x,0));x+=i.width+20
s.save(d+'review/work/cap_compare.png');print(s.size)
