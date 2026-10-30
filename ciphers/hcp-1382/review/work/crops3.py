from PIL import Image
m=Image.open('review/work/norm.png')
def c(name,box,s=4):
    x=m.crop(box); x.resize((x.width*s,x.height*s),Image.BICUBIC).save('review/work/'+name+'.png')
c('r1end',(520,20,790,130));c('r3end',(400,160,700,290));c('r4a',(20,240,330,350));c('r4b',(310,220,720,350),3)
c('r5a',(70,310,430,470),3);c('r5b',(390,330,700,450),3);c('r6a',(30,420,400,530),3);c('r6b',(380,420,790,530),3);c('r7a',(40,500,440,620),3);c('r7b',(410,500,800,620),3)
