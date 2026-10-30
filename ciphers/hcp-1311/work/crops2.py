from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_adr.jpg').convert('RGB')
def c(n,box,s=4,co=1.6):
    r=im.crop(box); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); ImageEnhance.Contrast(r).enhance(co).save('crops/'+n+'.png')
c('s_r6',(1000,420,1560,520))
c('s_r11_12',(600,1010,1500,1190),3)
c('s_r14',(600,1110,1620,1210),3)
c('s_r15',(700,1200,1520,1290),3)
c('s_r20',(600,1500,1600,1640),3)
c('s_r21_23',(800,1660,1600,1860),3)
c('s_r24_26',(800,1830,1900,2190),2)
c('s_st1',(2680,350,3200,550),4,1.8)
c('s_st2',(2680,500,3200,760),4,1.8)
c('s_st3',(2780,720,3280,900),4,1.8)
