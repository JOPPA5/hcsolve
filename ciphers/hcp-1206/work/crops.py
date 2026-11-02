from PIL import Image
import sys
im=Image.open('hires/cpc_--_HU_Jasz_HU_Ujpest---Budapest_jolanka-61_adr.jpg')
s=3671/2000
R={'a_head':(200,170,960,330),'b1':(160,380,960,540),'b2':(160,530,1040,710),'c1':(160,710,1000,930),'c2':(160,920,1040,1190),'top':(960,100,1480,210),'stampbox':(1540,220,1830,500),'edge':(1810,150,1920,420),'addr1':(980,270,1200,390),'addr2':(1040,540,1620,700),'addr3':(1340,730,1910,820),'addr4':(980,840,1900,1040),'addr5':(1050,990,1900,1170)}
for k,b in R.items():
    c=im.crop(tuple(int(x*s) for x in b)); c=c.resize((min(c.width*2,2000),int(c.height*min(c.width*2,2000)/c.width)),Image.LANCZOS)
    c.save(f'crops/{k}.png')
im.crop(tuple(int(x*s) for x in R['edge'])).rotate(90,expand=True).resize((1340,540)).save('crops/edge_rot.png')
