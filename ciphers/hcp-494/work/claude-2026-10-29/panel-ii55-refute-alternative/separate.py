# Colour separation: brown (iron-gall) ink vs neutral black gloss. Output BMPs: brown-only and black-only; print column extents.
import sys, struct
import os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from components import read_bmp
def write_bmp(path,w,h,px):
    row=(w*3+3)//4*4; pad=b'\0'*(row-w*3)
    hdr=struct.pack('<2sIHHI',b'BM',54+row*h,0,0,54)+struct.pack('<IiiHHIIiiII',40,w,-h,1,24,0,row*h,2835,2835,0,0)
    out=bytearray(hdr)
    for y in range(h):
        for x in range(w):
            r,g,b=px[y][x]; out+=bytes((b,g,r))
        out+=pad
    open(path,'wb').write(out)
def classify(p):
    r,g,b=p; m=(r+g+b)/3
    if m>=150: return 'paper'
    # black gloss: dark and neutral (low red-blue excess); brown ink: red excess
    if (r-b)<=18 and m<110: return 'black'
    return 'brown'
def main(src,prefix,ranges):
    w,h,px=read_bmp(src)
    paper=(225,215,190)
    brown=[[px[y][x] if classify(px[y][x])!='black' else paper for x in range(w)] for y in range(h)]
    black=[[px[y][x] if classify(px[y][x])=='black' else paper for x in range(w)] for y in range(h)]
    write_bmp(prefix+'-brown.bmp',w,h,brown); write_bmp(prefix+'-black.bmp',w,h,black)
    for name,x0,x1 in ranges:
        ys=[y for y in range(h) for x in range(x0,x1+1) if classify(px[y][x])=='brown']
        print("%-12s x%4d-%4d brown-ink rows %3d-%3d height %3d"%(name,x0,x1,min(ys),max(ys),max(ys)-min(ys)+1) if ys else name+" none")
if __name__=='__main__':
    src=sys.argv[1]; prefix=sys.argv[2]
    ranges=[]
    for a in sys.argv[3:]:
        n,x0,x1=a.split(':'); ranges.append((n,int(x0),int(x1)))
    main(src,prefix,ranges)
