from PIL import Image, ImageOps
import numpy as np
A=Image.open('work/hires/pc_hcp_467_adr.JPG').convert('RGB')
s=1785/1024
# ink = dark and bluish-dark, ignore light-gray watermark: threshold on luminance
def prof(name,box,th=125):
    b=[int(x*s) for x in box]
    im=np.array(A.crop(b).convert('L'))
    ink=(im<th)
    cols=ink.sum(0)>0
    runs=[];st=None
    for i,v in enumerate(cols):
        if v and st is None: st=i
        if not v and st is not None: runs.append((st,i));st=None
    if st is not None: runs.append((st,len(cols)))
    gaps=[runs[i+1][0]-runs[i][1] for i in range(len(runs)-1)]
    print(name,'ink runs(hires px from x0=%d):'%b[0],runs);print(' gaps:',gaps)
prof('line2',(60,185,300,218))
prof('line6',(60,365,300,395))
prof('line6b',(280,365,500,395))
