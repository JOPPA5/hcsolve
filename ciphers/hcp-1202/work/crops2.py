import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
# 3 columns of tiles
y=130;i=0
while y<2200:
    for j,x0 in enumerate([150,800,1450]):
        crop(f't{i:02d}_{j}',(x0,y,x0+760,y+215),2.0)
    y+=185;i+=1
for i,y in enumerate([1650,1835,2020]):
    for j,x0 in enumerate([2150,2800]):
        crop(f'tr{i}_{j}',(x0,y,x0+760,y+215),2.0)
