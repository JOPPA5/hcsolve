from PIL import Image,ImageOps,ImageEnhance
import sys
im=Image.open('hires/cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17_adr.jpg').convert('RGB')
S=3468/1600
# blocks y ranges in 1600-view coords; x split into two halves
blocks=[(35,160),(150,260),(250,370),(360,450),(450,540),(525,650),(640,740),(720,810),(800,880),(860,1000)]
for i,(a,b) in enumerate(blocks):
    for j,(x0,x1) in enumerate([(20,400),(380,770)]):
        c=im.crop((int(x0*S),int(a*S),int(x1*S),int(b*S)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c=ImageOps.autocontrast(c,cutoff=1)
        c.save('crops/b%d_%d.png'%(i,j))
