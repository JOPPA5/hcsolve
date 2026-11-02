from PIL import Image,ImageOps
im=Image.open('hires/cpc_1912-04-_HU__HU_Jasz-Arokszalas_jolanka-104_adr.jpg').convert('RGB')
g=im.split()[1]
ys=[(60,500),(480,960),(940,1420),(1400,1760),(1720,2000)]
for k,(a,b) in enumerate(ys):
    for j,(x0,x1) in enumerate(((60,880),(840,1680))):
        c=ImageOps.autocontrast(g.crop((x0,a,x1,b)),cutoff=0.3)
        c=c.resize((int(c.width*1.8),int(c.height*1.8)),Image.LANCZOS); c.save('rev2/row%d_%d.png'%(k,j))
