from PIL import Image, ImageEnhance
import glob,sys,os
b=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
im=Image.open(glob.glob(b+'/work/hires/*_adr.jpg')[0]).convert('RGB')
pic=Image.open(glob.glob(b+'/work/hires/*_pic.jpg')[0]).convert('RGB')
pic.resize((1400,int(1400*pic.height/pic.width))).save(b+'/review/work/pic_full.png')
im.resize((1700,int(1700*im.height/im.width))).save(b+'/review/work/adr_full.png')
