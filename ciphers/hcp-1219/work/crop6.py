exec(open('crop.py').read().split('bands=')[0])
# overlapping full-row strips, left/mid/right
ys=[85,130,190,240,283,325,382,428,490,540,593,650,700,750]
for i,y in enumerate(ys,1):
    if i in(2,3,4,5,6,7,8): 
        c(f'x{i:02d}a',30,y-34,330,y+34,3); c(f'x{i:02d}b',320,y-34,620,y+34,3); c(f'x{i:02d}c',610,y-34,910,y+34,3)
