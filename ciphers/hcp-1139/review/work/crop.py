from PIL import Image
import glob,sys
im=Image.open(glob.glob('work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1024
def c(n,l,t,r,b,z=2):
    x=im.crop((int(l*S),int(t*S),int(r*S),int(b*S)))
    x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS).save(f'review/work/crops/{n}.png')
i=0
for y in range(5,640,75):
    c(f'b{i:02d}L',10,y,265,y+85); c(f'b{i:02d}R',255,y,515,y+85); i+=1
print(i)
