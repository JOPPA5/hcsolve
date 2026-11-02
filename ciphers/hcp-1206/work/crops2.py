from PIL import Image, ImageOps
im=Image.open('hires/cpc_--_HU_Jasz_HU_Ujpest---Budapest_jolanka-61_adr.jpg')
s=3671/2000
def c(n,b,z=3,rot=0):
    x=im.crop(tuple(int(v*s) for v in b)); 
    if rot: x=x.rotate(rot,expand=True)
    x=ImageOps.autocontrast(x.convert('L'),cutoff=1).resize((x.width*z,x.height*z),Image.LANCZOS); x.save(f'crops/{n}.png'); print(n,x.size)
c('l1a',(180,1040,600,1130),3)
c('l1b',(560,1040,1010,1130),3)
c('l2a',(180,1100,620,1190),3)
c('l2b',(600,1100,1170,1190),3)
c('v',(170,630,860,710),2+1)
c('edgeR',(1820,150,1915,410),4,90)
c('edgeL',(1820,150,1915,410),4,-90)
c('ret',(170,500,960,590),2)
