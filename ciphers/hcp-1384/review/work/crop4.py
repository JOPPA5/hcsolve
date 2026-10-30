from PIL import Image, ImageEnhance
r=Image.open('review/work/rot_full.png').convert('RGB')
o=Image.open('work/hires/pc_hcp_65_adr.JPG').convert('RGB')
ox,oy=155,890
def c(n,x0,y0,x1,y1,z=4,src=r,off=(ox,oy)):
    a=src.crop((off[0]+x0,off[1]+y0,off[0]+x1,off[1]+y1)); a=a.resize((a.width*z,a.height*z),Image.LANCZOS)
    ImageEnhance.Contrast(a).enhance(1.6).save(f'review/work/{n}.jpg',quality=90)
c('mfuufs_full',240,350,620,560,3)
c('blot',370,270,500,340,8)
c('flourish',580,450,840,520,4)
c('zpvs',100,630,280,740,6)
c('hjsm',750,640,950,750,6)
c('nl5',330,540,600,640,5)
c('stamp',1330,60,1600,380,4,o,(0,0))
c('stamp2',1370,180,1600,380,5,o,(0,0))
