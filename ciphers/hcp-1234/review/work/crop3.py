from PIL import Image, ImageEnhance
P='../../work/hires/cpc_1913-12-16_HU__HU_Jasz-Arokszalas_jolanka-45_'
im=Image.open(P+'adr.jpg').convert('RGB')
def s(n,b,k=4,ct=1.5,rot=0,src=im):
    c=src.crop(b); c=ImageEnhance.Contrast(c).enhance(ct)
    if rot: c=c.rotate(rot,expand=True,fillcolor=(230,200,150))
    c.resize((c.width*k,c.height*k),Image.LANCZOS).save(f'crops/{n}.png')
s('b5',(380,490,620,610),6)
s('b6',(670,580,830,700),6)
s('b8',(1000,790,1340,910),4)
s('b12',(940,1240,1140,1350),6)
s('st3b',(2920,430,3190,540),6)
s('pmdate',(2020,300,2360,800),3,1.6,rot=-70)
pic=Image.open(P+'pic.jpg').convert('RGB')
s('verse',(120,340,460,1000),3,1.3,rot=-90,src=pic)
