from PIL import Image
im=Image.open('ciphers/hcp-1233/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-67_adr.jpg').convert('RGB')
b=[(95,1335,150,1415),(70,175,125,255),(75,365,130,445),(1075,1450,1165,1560),(85,1660,155,1760)]
H=330;x=0;t=[]
for q in b:
    c=im.crop(q);c=c.resize((c.width*H//c.height,H),Image.LANCZOS);t.append(c)
o=Image.new('RGB',(sum(c.width+12 for c in t),H),'white')
for c in t:o.paste(c,(x,0));x+=c.width+12
o.save('ciphers/hcp-1233/work/resp/cmp_k_b.png')
c=im.crop((2820,1850,3240,1960));c.resize((c.width*4,c.height*4),Image.LANCZOS).save('ciphers/hcp-1233/work/resp/row18_tail.png')
