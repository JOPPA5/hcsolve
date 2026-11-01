import sys
from PIL import Image
im=Image.open('hires/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_adr.jpg').convert('RGB')
rows=[(50,120),(110,195),(190,262),(255,340),(335,412),(410,495),(495,580),(570,645),(640,715),(715,785),(778,848),(845,915),(915,990),(980,1055),(1045,1115),(1095,1155),(1135,1205)]
f=1.72
for i,(a,b) in enumerate(rows,1):
  for k,(l,r) in enumerate([(40,320),(300,590),(570,880)]):
    c=im.crop((int(l*f),int(a*f),int(r*f),int(b*f)));c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
    c.save(f'crops/r{i:02d}_{k}.png')
