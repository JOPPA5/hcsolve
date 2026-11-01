from PIL import Image, ImageOps, ImageChops
im=Image.open('hires/cpc_1913-09-19_HU__HU_Jasz-Arokszalas_jolanka-44_adr.jpg').convert('RGB')
r,g,b=im.split()
d=ImageChops.subtract(b,g,1,60)   # purple high
d=ImageOps.invert(ImageOps.autocontrast(d,cutoff=0.2))
d.save('crops/purple.png')
def c(n,box,sc=2.6,rot=None,src=d):
    x=src.crop(box)
    if rot: x=x.rotate(rot,expand=True)
    x=x.resize((int(x.width*sc),int(x.height*sc)),Image.LANCZOS); x.save('crops/'+n)
c('p1.png',(2200,1740,2800,1930)); c('p2.png',(2750,1740,3340,1930))
c('p3.png',(2200,1900,2800,2090)); c('p4.png',(2750,1900,3340,2090))
c('p5.png',(1500,1880,2300,2090),2.4)
c('e1.png',(3200,1000,3345,1800),2.4,-90); 
c('e2.png',(3200,300,3345,1050),2.4,-90)
c('e1c.png',(3200,1000,3345,1800),2.4,-90,im); 
c('e2c.png',(3200,300,3345,1050),2.4,-90,im)
c('st.png',(2780,420,3240,720),3.6,None,im)
c('st0.png',(2780,420,3240,720),3.6)
