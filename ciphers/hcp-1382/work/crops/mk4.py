from PIL import Image
o=Image.open('crops/norm.png')
def c(name,box,s=5):
    x=o.crop(box); x=x.resize((x.width*s,x.height*s),Image.BICUBIC); x.save('crops/'+name+'.jpg',quality=93)
c('a1',(0,230,350,330),4); c('a2',(310,230,560,350)); c('a3',(530,200,720,340)); c('a4',(60,320,330,470),4); c('a5',(310,320,560,470),4); c('a6',(530,320,720,420)); c('b1',(30,420,330,520),4); c('b2',(400,420,790,520),3); c('t',(380,20,740,130),3); c('t2',(320,120,720,240),3)
