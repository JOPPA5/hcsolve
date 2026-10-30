# One comparison try: pencil lower-right block on 1786 versus the hcp-1787 picture side (read-only).
from PIL import Image
P=Image.open('work/hires/pc_hcp_467_pic.JPG').convert('RGB')
P.crop((960,440,1100,540)).resize((840,600),Image.LANCZOS).save('work/crops2/pencil_sig.png')
P.crop((700,90,1160,460)).resize((1380,1110),Image.LANCZOS).save('work/crops2/pencil_plain3x.png')
Q=Image.open('../hcp-1787/work/hires/pc_hcp_468_pic.JPG').convert('RGB')
Q.save('work/crops2/sister_1787_pic.png'); print(Q.size)
