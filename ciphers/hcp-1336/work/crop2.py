from PIL import Image, ImageOps
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/'
out=base+'hcp-1336/work/crops/'
s=1785/1024
def crop(n,file,b,z=5):
    im=Image.open(base+file); c=im.crop([int(x*s) for x in b]); c=c.resize((c.width*z,c.height*z),Image.LANCZOS); c.save(out+n+'.png')
a='hcp-1336/work/hires/pc_hcp_17_adr.JPG'
crop('s_l2_mid',a,(140,305,305,375))
crop('s_l3_end',a,(290,380,460,440))
crop('s_l4_a',a,(85,440,190,500))
crop('s_l1_b',a,(350,235,470,295))
crop('below',a,(60,530,460,630),3)
crop('c_1338_l2',f'hcp-1338/work/hires/pc_hcp_19_adr.JPG',(120,310,440,365),3)
crop('c_1338_l3',f'hcp-1338/work/hires/pc_hcp_19_adr.JPG',(105,375,450,500),3)
crop('c_1339_l2',f'hcp-1339/work/hires/pc_hcp_20_adr.JPG',(100,305,460,415),3)
crop('c_1339_l4',f'hcp-1339/work/hires/pc_hcp_20_adr.JPG',(100,440,440,490),3)
crop('c_1334_b',f'hcp-1334/work/hires/pc_hcp_15_adr.JPG',(170,590,330,630),4)
