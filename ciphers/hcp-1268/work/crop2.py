from PIL import Image
import sys
im=Image.open('hires/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_adr.jpg').convert('RGB')
s=1.72
B={'z9blot':(255,640,420,725,8),'z9b':(440,650,660,730,7),'z10a':(50,735,340,815,5),'z11a':(50,810,310,885,5),'z11b':(300,810,800,880,4),'z14b':(440,1045,870,1120,4),'z15a':(50,1105,450,1185,4),'z14end':(700,1070,880,1160,6),'z12a':(50,880,430,960,5),'z7b':(360,540,600,620,6)}
for k,(a,b,c,d,z) in B.items():
    x=im.crop((int(a*s),int(b*s),int(c*s),int(d*s))); x.resize((x.width*z//2,x.height*z//2),Image.LANCZOS).save(f'crops/{k}.png')
