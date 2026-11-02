import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
for j,(a,b) in enumerate([(150,1250),(1150,2250),(2250,3400)]):
    crop(f'c{j}',(a,1700,b,2180),1.35)
