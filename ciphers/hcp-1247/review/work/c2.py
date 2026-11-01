from PIL import Image, ImageOps, ImageChops
s=Image.open('c/shear.png')
im=Image.open('../../work/hires/cpc_1913-09-19_HU__HU_Jasz-Arokszalas_jolanka-44_adr.jpg').convert('RGB')
def c(n,box,sc,src=s,rot=None):
    x=src.crop(box)
    if rot: x=x.rotate(rot,expand=True)
    x=ImageOps.autocontrast(x,cutoff=1).resize((int(x.width*sc),int(x.height*sc)),Image.LANCZOS); x.save('c/'+n,quality=90)
# rows 23-26 across whole card
for i,(a,b) in enumerate([(60,900),(850,1700),(1650,2500),(2450,3300)]):
    c(f'low{i}.jpg',(a,1720,b,2130),1.9,im)
c('stamp.jpg',(2740,240,3320,760),2.8,im)
c('edge1.jpg',(3200,300,3345,1050),2.2,im,-90)
c('edge2.jpg',(3200,1000,3345,1800),2.2,im,-90)
c('r19.jpg',(60,1430,900,1600),2,s)
c('r19b.jpg',(800,1430,1660,1600),2,s)
