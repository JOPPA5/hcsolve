from PIL import Image, ImageOps, ImageEnhance
import sys
s=1785/1024
A=Image.open('work/hires/pc_hcp_467_adr.JPG').convert('RGB')
P=Image.open('work/hires/pc_hcp_467_pic.JPG').convert('RGB')
def c(im,box,z,name):
    b=[int(x*s) for x in box]
    r=im.crop(b); r=r.resize((r.width*z,r.height*z),Image.LANCZOS)
    r.save('review/work/'+name)
# each row, two halves
rows=[(140,185),(180,225),(222,268),(280,320),(318,355),(355,400),(405,445),(445,490),(490,535),(525,570)]
for i,(a,b) in enumerate(rows):
    c(A,(60,a,290,b),4,f'r{i}a.png'); c(A,(280,a,510,b),4,f'r{i}b.png')
c(A,(520,250,1000,600),2,'addr.png')
c(A,(690,40,960,300),3,'stamp.png')
c(P,(390,50,680,310),3,'pencil.png')
