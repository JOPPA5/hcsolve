from PIL import Image, ImageOps
r=Image.open('adr_ccw.png').convert('RGB')
a=ImageOps.autocontrast(r.crop((640,950,980,1070)).resize((1020,360),Image.LANCZOS),cutoff=1)
b=Image.open('../../../hcp-1366/work/crops/w1.png').convert('RGB'); b=b.crop((930,0,1750,330))
c=Image.open('../../../hcp-1360/work/crops/f_w3tail.png').convert('RGB')
c.thumbnail((1020,500))
o=Image.new('RGB',(1040,a.height+b.height+c.height+20),'white');y=0
for i in (a,b,c):o.paste(i,(0,y));y+=i.height+10
o.save('slot_compare_1363_1366_1360.png')
pm=r.crop((110,70,480,350)).rotate(-90,expand=True);pm=pm.resize((pm.width*2,pm.height*2));ImageOps.autocontrast(pm,cutoff=1).save('pm2.png')
