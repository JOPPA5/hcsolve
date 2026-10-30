from PIL import Image, ImageEnhance
import numpy as np
m=Image.open('review/work/norm.png'); r=Image.open('review/work/raw.png')
def c(src,name,box,s=6):
    x=src.crop(box); x.resize((x.width*s,x.height*s),Image.LANCZOS).save('review/work/'+name+'.png')
c(m,'z_N',(400,425,540,510));c(m,'z_ijti',(320,240,540,340),5);c(r,'z_dear_raw',(405,185,640,300),5)
c(m,'z_zpv',(520,250,720,350),5);c(m,'z_dots',(600,380,720,440),5);c(m,'z_ifsf',(420,310,600,460),5)
ad=Image.open('work/hires/pc_hcp_63_adr.JPG')
s=ad.width/1024
ad.crop((int(730*s),int(90*s),int(950*s),int(290*s))).resize((880,800)).save('review/work/z_pm.png')
ad.crop((int(470*s),int(280*s),int(960*s),int(570*s))).save('review/work/z_addr.png')
