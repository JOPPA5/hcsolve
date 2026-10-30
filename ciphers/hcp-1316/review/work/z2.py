from PIL import Image, ImageOps
im=Image.open('work/hires/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-27_adr.jpg').convert('RGB')
# blob with contrast: green channel stretched
c=im.crop((90,1730,330,1880))
g=c.split()[1]
lo=ImageOps.autocontrast(g,cutoff=1)
# gamma to open up dark range
lo2=g.point(lambda v:min(255,max(0,int((v-60)*255/90))))
s=6
W=c.width*s;H=c.height*s
o=Image.new('RGB',(W*2+10,H),'white')
o.paste(c.resize((W,H),Image.LANCZOS),(0,0)); o.paste(lo2.resize((W,H),Image.LANCZOS).convert('RGB'),(W+10,0))
o.save('review/work/crops/r17_blob.png')
