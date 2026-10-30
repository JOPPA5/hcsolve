from PIL import Image
r=Image.open('rot.png')
im=Image.open('../../work/hires/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_adr.jpg').convert('RGB')
def s(c,n,z): c.resize((c.width*z,c.height*z),Image.LANCZOS).save(n)
s(im.crop((2920,520,3120,700)),'z_box14.png',6)
s(im.crop((2300,200,2820,420)),'z_szeprem.png',3)
a=r.crop((170,530,560,690)); b=r.crop((920,890,1160,1050)); c=r.crop((1420,880,1800,1050))
o=Image.new('RGB',(1010,170),'white');o.paste(a,(0,0));o.paste(b,(400,0));o.paste(c,(630,0));s(o,'z_Fs.png',2)
