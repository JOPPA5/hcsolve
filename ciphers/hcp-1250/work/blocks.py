import subprocess,sys
a=[]
for b,y in enumerate([40,370,700,1030,1360,1690]):
    for c,x in enumerate([60,640,1220]):
        a+=[f'b{b}c{c}',x,y,x+660,y+370,1.5]
subprocess.run([sys.executable,'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1250/work/crop.py']+list(map(str,a)))
