exec(open('crop.py').read().split('bands=')[0])
for k in range(6):
    x=40+k*310
    c(f'S{k}',x,1050,x+340,1195,3)
