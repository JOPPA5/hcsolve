import sys
W,H=int(sys.argv[2]),int(sys.argv[3]); x0,x1=int(sys.argv[4]),int(sys.argv[5]); y0,y1=int(sys.argv[6]),int(sys.argv[7])
d=open(sys.argv[1],'rb').read()
for y in range(y0,y1):
    row=d[y*W+x0:y*W+x1]; n=sum(1 for v in row if v<90)
    print(y, '#'*(n//3))
