from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_--_HU__HU_Budapest_jolanka-62_adr.jpg').convert('RGB')
def c(name,box,s=2.2):
    i=im.crop(box); i=i.resize((int(i.width*s),int(i.height*s)),Image.LANCZOS)
    i=ImageEnhance.Contrast(i).enhance(1.8); i.save('crops/'+name+'.png')
# left block in 4 horizontal bands, two columns
ys=[(70,560),(520,1010),(960,1450),(1400,2060)]
for k,(a,b) in enumerate(ys):
    c(f'b{k}L',(70,a,860,b)); c(f'b{k}R',(780,a,1640,b))
c('stamp',(2780,250,3260,720),3)
c('bottomR',(1500,1800,3300,2060),1.2)
