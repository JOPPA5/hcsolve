from PIL import Image, ImageOps
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1364/'
r=Image.open(d+'work/hires/pc_hcp_45_adr.JPG').convert('RGB').rotate(90,expand=True)
b={'hd':(400,880,1075,985),'l1':(370,975,700,1075),'l1b':(690,975,1030,1075),
'l2a':(360,1090,700,1190),'l2b':(690,1080,1030,1190),
'l3a':(370,1180,700,1290),'l3b':(680,1180,1020,1290),
'l4a':(370,1280,700,1400),'l4b':(610,1280,1040,1400),
'l5':(480,1430,800,1540)}
for k,v in b.items():
    c=r.crop(v);c=c.resize((c.width*4,c.height*4),Image.LANCZOS);c=ImageOps.autocontrast(c,cutoff=1);c.save(d+'review/work/%s.png'%k)
