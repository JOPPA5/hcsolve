from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1302/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_adr.jpg').convert('RGB')
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1302/work/crops/'
def s(n,box,z=2):
    c=im.crop(box); c.resize((c.width*z,c.height*z),Image.LANCZOS).save(d+n+'.png')
s('t1',(60,60,900,300)); s('t2',(860,60,1660,300))
s('t3',(60,270,900,520)); s('t4',(860,270,1700,520))
s('t5',(60,500,900,750)); s('t6',(860,500,1660,750))
s('t7',(60,740,900,1000)); s('t8',(860,740,1700,1000))
s('u1',(70,1470,900,1760)); s('u2',(860,1470,1700,1760))
s('u3',(70,1700,900,2000)); s('u4',(860,1700,1700,2000))
s('u5',(60,1850,900,2140)); s('u6',(860,1850,1700,2140))
s('u7',(1650,1880,2500,2140)); s('u8',(2450,1880,3300,2140))
