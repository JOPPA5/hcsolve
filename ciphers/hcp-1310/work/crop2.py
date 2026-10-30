from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1912-07-03_HU__HU_Jasz-Arokszalas_jolanka-28_adr.jpg').convert('RGB')
S=1.72
def c(n,l,t,r,b,z=3,con=1.4):
    x=im.crop((int(l*S),int(t*S),int(r*S),int(b*S)));x=x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(con).save('crops/'+n+'.png')
c('r12a',50,695,450,770,2.8);c('r12b',430,695,830,770,2.8)
c('r13a',50,760,450,840,2.8);c('r13b',430,760,870,840,2.8)
c('r16a',50,905,450,965,2.8);c('r16b',430,905,850,965,2.8)
c('r10',50,570,450,640,2.8);c('r10b',430,570,850,640,2.8)
c('r8b',430,455,870,520,2.8)
c('r9a',50,510,450,580,2.8);c('r9b',430,510,870,580,2.8)
c('r7a',50,405,450,460,2.8)
c('r21',50,1170,450,1225,2.8);c('r21b',430,1170,830,1225,2.8)
c('stamp0',1530,120,1790,410,3)
c('corner',1880,1100,1930,1215,4)
c('pencil',850,70,1520,140,1.7,1.6)
