from PIL import Image
im=Image.open('ciphers/hcp-1283/work/crops/sheared.png')
def c(n,x0,y0,x1,y1,s=4):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('ciphers/hcp-1283/work/crops/%s.png'%n)
c('y_r14a',20,985,520,1065)
c('y_r14b',480,970,980,1050)
c('y_r18',300,1260,800,1350)
c('y_r19',380,1330,880,1430)
c('y_r8',440,590,940,670)
c('y_r1',1000,75,1400,135)
c('y_r21',900,1540,1400,1640)
c('y_r7',900,470,1300,550)
c('y_r10',300,690,800,780)
