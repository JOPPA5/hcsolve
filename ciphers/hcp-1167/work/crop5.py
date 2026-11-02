from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
B={'ang':(520,930,850,1000),'mar':(30,960,540,1040),'on':(900,310,1350,410),'sok':(30,920,540,1000)}
for n,b in B.items():
    cr=im.crop(tuple(int(x*s) for x in b))
    cr=cr.resize((cr.width*3,cr.height*3),Image.LANCZOS); cr.save(f'crops/z_{n}.png')
# montage of zooms
names=['lehet7','lehem9','szoval','felm','rara','tudja','husege','soraimat','udv']
ims=[Image.open(f'crops/z_{n}.png') for n in names]
for n,i in zip(names,ims): print(n,i.size)
