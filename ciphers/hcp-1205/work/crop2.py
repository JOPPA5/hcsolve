"""Usage: crop2.py a|r|p name x0 y0 x1 y1 scale -- crops of hires: a address side, r address side rotated 180, p picture side rotated 90 degrees; writes work/crops2/"""
import sys,os
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))+'/'
a=sys.argv
f='pic' if a[1]=='p' else 'adr'
im=Image.open(D+'hires/cpc_--_HU__HU_Rakos-Palota-Ujfalu_jolanka-60_%s.jpg'%f).convert('RGB')
if a[1]=='p': im=im.rotate(90,expand=True)
if a[1]=='r': im=im.rotate(180)
b=tuple(map(int,a[3:7]));s=float(a[7])
x=im.crop(b);x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS);x.save(D+'crops2/'+a[2]+'.png')
