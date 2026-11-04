# zoom.py NAME y0 y1 x_at_y0 x_at_y1 [scale] -> rotated strip crop of one column segment
import sys
from PIL import Image
HI='ciphers/hcp-927/work/hires/cpc_1910-06-19_DE_Graudenz-(Grudziadz)_DE_Rendsburg__adr.jpg'
im=Image.open(HI).convert('RGB')
n,y0,y1,xa,xb=sys.argv[1],*map(int,sys.argv[2:6]); S=int(sys.argv[6]) if len(sys.argv)>6 else 4
HW=40
st=Image.new('RGB',(y1-y0,2*HW),'white')
for y in range(y0,y1):
    xc=int(round(xa+(xb-xa)*(y-y0)/(y1-y0)))
    st.paste(im.crop((xc-HW,y,xc+HW,y+1)).transpose(Image.ROTATE_90),(y-y0,0))
st.resize(((y1-y0)*S,2*HW*S)).save('ciphers/hcp-927/work/crops/z_%s.png'%n)
