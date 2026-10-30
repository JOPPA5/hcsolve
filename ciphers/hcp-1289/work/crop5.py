from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1289/work/'
im=Image.open(W+'hires/cpc_--22_HU__HU_Jasz-Arokszalas_jolanka-87_adr.jpg')
S=1.72
def crop(name,x0,y0,x1,y1,z):
    c=im.crop(tuple(int(v*S) for v in (x0,y0,x1,y1)))
    c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS).save(W+'crops2/'+name+'.png')
crop('corner',1680,1150,1925,1215,4.5)
crop('r29e',1420,1160,1700,1215,4)
crop('r14',35,555,500,610,2.3)
crop('r14b',440,555,890,610,2.3)
crop('r26e',1420,1055,1600,1100,6)
