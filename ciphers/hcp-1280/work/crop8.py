from PIL import Image, ImageFilter
import numpy as np
im=Image.open('work/hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')
def gb(c,s):
    l,h=float(c.min()),float(c.max())
    u=Image.fromarray(((c-l)/(h-l+1e-6)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(s))
    return np.asarray(u).astype('float32')/255*(h-l)+l
def norm(c,lo=1,hi=99):
    l,h=np.percentile(c,lo),np.percentile(c,hi); return (np.clip((c-l)/(h-l),0,1)*255).astype('uint8')
box=(2830,195,3250,450)
a=np.asarray(im.crop(box)).astype('float32'); r,g,b=a[...,0],a[...,1],a[...,2]
# teal print mask: red not exceeding green much
teal=(r-g)<8
tm=np.asarray(Image.fromarray((teal*255).astype('uint8')).filter(ImageFilter.MaxFilter(3)))>0
# replace teal by red-ink-preserving estimate: use weighted normalised blur
c=(g+b)/2
w=(~tm).astype('float32')
num=gb(c*w,1.6); den=gb(w,1.6)+1e-3
filled=np.where(tm,num/den,c)
Image.fromarray(norm(filled)).resize((filled.shape[1]*4,filled.shape[0]*4),Image.BICUBIC).save('work/crops2/nt.png')
# local contrast normalisation
hp=filled-gb(filled,7)
sd=np.sqrt(gb(hp*hp,12))+2
lcn=hp/sd
Image.fromarray(norm(lcn,2,98)).resize((filled.shape[1]*4,filled.shape[0]*4),Image.BICUBIC).save('work/crops2/nt_lcn.png')
sm=gb(lcn+5,0.8)
Image.fromarray(norm(sm,2,98)).resize((filled.shape[1]*4,filled.shape[0]*4),Image.BICUBIC).save('work/crops2/nt_lcn_s.png')
print(np.percentile(r-g,[1,5,50,95]))
H=filled.shape[1]*6
for nm,y0,y1 in (('L2',55,130),('L3',125,215)):
    for xn,x0,x1 in (('a',0,170),('b',130,300),('c',260,420)):
        s=filled[y0:y1,x0:x1]; t=lcn[y0:y1,x0:x1]
        A=Image.fromarray(norm(s)).resize((s.shape[1]*6,s.shape[0]*6),Image.BICUBIC)
        B=Image.fromarray(norm(gb(t+5,0.7),2,98)).resize((s.shape[1]*6,s.shape[0]*6),Image.BICUBIC)
        C=im.crop((box[0]+x0,box[1]+y0,box[0]+x1,box[1]+y1)).resize((s.shape[1]*6,s.shape[0]*6),Image.LANCZOS)
        M=Image.new('RGB',(A.width,A.height*3+8),'white'); M.paste(C,(0,0)); M.paste(A.convert('RGB'),(0,A.height+4)); M.paste(B.convert('RGB'),(0,A.height*2+8))
        M.save(f'work/crops2/{nm}{xn}.png')
