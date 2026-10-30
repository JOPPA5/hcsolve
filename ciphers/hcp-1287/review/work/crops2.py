from PIL import Image
P='work/hires/cpc_1912-05-15_HU__HU_Jasz-Arokszalas_jolanka-21_'
im=Image.open(P+'adr.jpg').convert('RGB')
def s(n,box,k):
    c=im.crop(box); c.resize((c.width*k,c.height*k),Image.LANCZOS).save(f'review/work/crops/{n}.png')
s('stamp',(2640,230,3180,760),3)
s('szep',(1680,470,2700,720),2)
s('addr',(1650,850,3250,1800),1)
s('r5end',(1560,450,1780,640),5)
s('r12end',(1330,1120,1740,1420),4)
s('r22end',(1420,1950,1720,2110),5)
s('r09mid',(180,1010,460,1200),5)
s('r10f',(380,1020,1000,1220),3)
im2=Image.open(P+'pic.jpg').convert('RGB'); print(im2.size); im2.thumbnail((1400,1400)); im2.save('review/work/crops/pic.png')
