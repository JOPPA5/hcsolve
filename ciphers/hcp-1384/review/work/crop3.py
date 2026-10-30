from PIL import Image, ImageEnhance
r=Image.open('review/work/rot_full.png').convert('RGB')
ox,oy=155,890
def c(n,x0,y0,x1,y1,z=4):
    a=r.crop((ox+x0,oy+y0,ox+x1,oy+y1)); a=a.resize((a.width*z,a.height*z),Image.LANCZOS)
    a=ImageEnhance.Contrast(a).enhance(1.6); a.save(f'review/work/{n}.jpg',quality=90)
c('r1a',200,130,600,240); c('r1b',580,130,950,240)
c('r2a',230,235,600,350); c('r2b',520,235,950,350)
c('r3a',230,350,620,450); c('r3b',600,350,850,450)
c('r4',240,450,620,550)
c('r5a',190,540,540,640); c('r5b',520,530,900,640)
c('r6a',10,620,520,770,3); c('r6b',500,630,950,750)
