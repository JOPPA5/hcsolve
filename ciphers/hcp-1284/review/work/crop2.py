from PIL import Image
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-74_adr.jpg').convert('RGB')
S=1.7225
def c(n,x0,x1,y0,y1,s=5):
    r=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S))); r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS).save(f'review/work/crops/{n}.png')
c('r17mid',330,640,1085,1165)
c('r13end',640,930,830,895)
c('r14start',60,330,890,965)
c('r11end',640,940,695,770)
c('r3p',230,330,175,250,8)
c('kelt',1370,1920,1080,1170,3)
c('pm1',930,1350,90,360,3)
c('pm2',1410,1560,130,270,3)
