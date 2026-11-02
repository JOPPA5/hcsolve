from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_--_HU__HU_Budapest_jolanka-62_adr.jpg').convert('RGB')
def c(name,box,s):
    i=im.crop(box); i=i.resize((int(i.width*s),int(i.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(i).enhance(1.8).save('crops/'+name+'.png')
c('a1',(1600,1700,3340,2020),1.1)
c('a2',(2500,1720,3340,1990),2.2)
c('a0',(1650,380,2800,560),1.6)
c('pm',(2500,230,2980,880),1.5)
