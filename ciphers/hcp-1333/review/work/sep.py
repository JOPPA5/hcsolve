from PIL import Image
im=Image.open('work/hires/pc_hcp_14_adr.JPG').convert('RGB')
def sep(box,name,sc=6):
    c=im.crop(box); o=Image.new('L',c.size,255); p=c.load(); q=o.load()
    for y in range(c.size[1]):
        for x in range(c.size[0]):
            r,g,b=p[x,y]; d=b-r
            q[x,y]=max(0,min(255,255-int(d*9)))
    o.resize((c.size[0]*sc,c.size[1]*sc),Image.LANCZOS).save(name+'_sep.png')
    c.resize((c.size[0]*sc,c.size[1]*sc),Image.LANCZOS).save(name+'.png')
sep((70,1035,330,1110),'review/work/L14start')
sep((60,780,200,850),'review/work/L8start')   # adjusted below
sep((60,560,200,640),'review/work/L6start')
