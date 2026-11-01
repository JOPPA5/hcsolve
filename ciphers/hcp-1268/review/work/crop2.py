from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1268/work/hires/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_adr.jpg').convert('RGB')
s=3445/1024
o='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1268/review/work/crops/'
def C(n,box,z=4,rot=0):
    c=im.crop(tuple(int(v*s) for v in box))
    if rot: c=c.rotate(rot,expand=True)
    c=c.resize((c.width*z,c.height*z),Image.LANCZOS); c.save(o+n+'.png'); print(n,c.size)
C('x_struck8',(190,290,240,335),6)
C('x_struck14',(275,530,335,572),6)
C('x_ov_end',(395,535,445,572),6)
C('x_row6end',(395,225,465,275),6)
C('x_b15',(25,565,70,612),6)
C('x_blot9',(125,325,175,372),6)
C('x_pm',(550,25,760,230),2)
C('x_stamp',(810,80,945,240),3,180)
C('x_s6_or',(395,225,440,275),8)
