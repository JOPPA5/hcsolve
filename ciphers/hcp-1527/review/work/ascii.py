import sys
W,H=int(sys.argv[2]),int(sys.argv[3]); x0,y0,w,h=map(int,sys.argv[4:8]); thr=int(sys.argv[8]) if len(sys.argv)>8 else 110
d=open(sys.argv[1],'rb').read()
print('    '+''.join(str((x0+i)//10%10) if (x0+i)%10==0 else ' ' for i in range(w)))
for y in range(y0,y0+h):
    print(f'{y:4d}'+''.join('#' if d[y*W+x]<thr else ('+' if d[y*W+x]<thr+30 else '.') for x in range(x0,x0+w)))
