from PIL import Image
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-73_adr.jpg')
def c(n,box,s=4):
    r=im.crop(box); r.resize((r.width*s,r.height*s),Image.LANCZOS).save(f'review/work/z_{n}.png')
c('r18mid',(700,1960,1130,2130),4)   # akor d o g
c('r18end',(1250,1920,1800,2130),3)  # mikot + sele
c('r20',(1800,1890,2600,2010),2)
c('r20b',(2500,1890,3300,2010),2)
c('r3start',(70,330,430,500),4)
c('r11oval',(70,1190,420,1330),4)
c('r6end',(900,690,1650,830),2)
Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-73_pic.jpg').resize((1148,737)).save('review/work/pic.png')
