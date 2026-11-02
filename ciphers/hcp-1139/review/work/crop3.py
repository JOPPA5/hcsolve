from PIL import Image
import glob
im=Image.open(glob.glob('work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1024
x=im.crop((int(520*S),int(10*S),int(975*S),int(260*S)));x.resize((x.width//2*1,x.height//2)).save('review/work/crops/pm.png')
