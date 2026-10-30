from PIL import Image, ImageEnhance
d='hires/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-107_'
im=Image.open(d+'adr.jpg').convert('RGB'); s=1.72
def sv(n,b,f=4,img=im,rot=0):
    c=img.crop(tuple(int(x*s) for x in b)); 
    if rot: c=c.rotate(rot,expand=True)
    c=c.resize((c.width*f,c.height*f),Image.LANCZOS); ImageEnhance.Contrast(c).enhance(1.3).save('crops/'+n+'.png')
sv('p_tas',(690,885,830,950),5)
sv('q_postmark',(900,90,1220,500),2,rot=-90)
sv('r_stamp2',(1590,300,1810,400),4)
pic=Image.open(d+'pic.jpg').convert('RGB')
sv('s_print',(1380,70,1720,1160),1,img=pic,rot=-90)
