from PIL import Image
r=Image.open('review/work/rot.png')
b={'tqjo':(835,345,1010,435,6),'mjuumf':(470,340,830,430,3),'xbt_pvu_gps':(490,255,1030,350,2.5),'cpz':(650,160,1020,265,3.5),'uijt':(360,410,620,490,4),'after':(590,420,1000,520,3),
'gspn':(690,505,960,590,4),'nl':(300,510,720,600,3),'hjsm':(740,580,1030,650,4)}
for k,(a,c,d,e,s) in b.items():
    x=r.crop((a,c,d,e)); x.resize((int(x.width*s),int(x.height*s)),Image.BICUBIC).save(f'review/work/z_{k}.png')
