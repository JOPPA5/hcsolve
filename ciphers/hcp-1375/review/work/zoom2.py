from PIL import Image, ImageOps
r=Image.open('review/work/rot.png')
b={'tq_hook':(860,385,960,460,8),'hook_mj':(530,370,640,450,6),'hook_ui':(370,450,470,520,6),'hook_af':(660,450,770,520,6),
'nz1':(340,160,470,260,6),'nz2':(290,510,430,600,5),'pxo2':(370,575,560,640,5),'nl2':(430,510,720,600,4)}
for k,(a,c,d,e,s) in b.items():
    x=ImageOps.autocontrast(r.crop((a,c,d,e)),cutoff=1); x.resize((x.width*s,x.height*s),Image.BICUBIC).save(f'review/work/y_{k}.png')
