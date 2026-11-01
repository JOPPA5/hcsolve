from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1268/work/hires/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_adr.jpg').convert('RGB')
s=3445/1024
o='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1268/review/work/crops/'
def C(n,box,z=4):
    c=im.crop(tuple(int(v*s) for v in box))
    c=c.resize((c.width*z,c.height*z),Image.LANCZOS); c.save(o+n+'.png'); print(n,c.size)
C('y_stamp',(815,80,925,200),3)
C('y_r13',(20,490,445,540),1)
C('y_r12',(20,445,445,495),1)
C('y_r01',(20,20,445,62),1)
C('y_r02',(20,62,445,105),1)
C('y_r03',(20,105,445,150),1)
C('y_r04',(20,145,445,190),1)
C('y_r05',(20,185,445,225),1)
C('y_e_cmp',(45,525,445,572),1)
C('y_bottom',(470,270,980,640),1)
