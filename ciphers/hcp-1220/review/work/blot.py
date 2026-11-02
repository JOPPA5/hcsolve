from PIL import Image
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
c=im.crop((690,770,1010,930)); c.resize((c.width*4,c.height*4),Image.LANCZOS).save('blot7.png')
