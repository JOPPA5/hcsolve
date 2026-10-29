import sys, struct
def read_bmp(path):
    d=open(path,'rb').read()
    off=struct.unpack_from('<I',d,10)[0]; w,h=struct.unpack_from('<ii',d,18); bpp=struct.unpack_from('<H',d,28)[0]
    assert bpp in (24,32), bpp
    bpx=bpp//8; row=(w*bpx+3)//4*4; top=h<0; h=abs(h)
    px=[]
    for y in range(h):
        yy=y if top else h-1-y
        base=off+yy*row
        px.append([(d[base+x*bpx+2],d[base+x*bpx+1],d[base+x*bpx]) for x in range(w)])
    return w,h,px
def main(path,thr=140,minpix=25):
    w,h,px=read_bmp(path)
    ink=[[ (sum(px[y][x])/3)<thr for x in range(w)] for y in range(h)]
    seen=[[False]*w for _ in range(h)]
    comps=[]
    for y in range(h):
        for x in range(w):
            if ink[y][x] and not seen[y][x]:
                st=[(y,x)]; seen[y][x]=True; pts=[]
                while st:
                    cy,cx=st.pop(); pts.append((cy,cx))
                    for dy in(-1,0,1):
                        for dx in(-1,0,1):
                            ny,nx=cy+dy,cx+dx
                            if 0<=ny<h and 0<=nx<w and ink[ny][nx] and not seen[ny][nx]:
                                seen[ny][nx]=True; st.append((ny,nx))
                if len(pts)>=minpix:
                    ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
                    cols=[px[p[0]][p[1]] for p in pts]
                    mr=sum(c[0] for c in cols)/len(cols); mb=sum(c[2] for c in cols)/len(cols); mg=sum(c[1] for c in cols)/len(cols)
                    comps.append((min(xs),min(ys),max(xs),max(ys),len(pts),mr,mg,mb))
    comps.sort()
    print("x0 y0 x1 y1  w  h  n  meanRGB  (R-B: brown ink is high, black gloss low)")
    for c in comps:
        print("%4d %3d %4d %3d  %3d %3d %5d  %3.0f %3.0f %3.0f  R-B=%+3.0f"%(c[0],c[1],c[2],c[3],c[2]-c[0]+1,c[3]-c[1]+1,c[4],c[5],c[6],c[7],c[5]-c[7]))
if __name__=='__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv)>2 else 140)
