exec(open('crop.py').read().split('bands=')[0])
for i,y in enumerate((755,800,845,885,925,972,1015),14):
    for j,x in enumerate((30,320,610)):
        c(f'z{i}{"abc"[j]}',x,y-34,x+300,y+40,3)
