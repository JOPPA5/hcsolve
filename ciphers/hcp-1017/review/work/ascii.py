import sys,subprocess
img,x,y,w,h=sys.argv[1],*map(int,sys.argv[2:6])
d=subprocess.run(['ffmpeg','-loglevel','error','-i',img,'-vf',f'crop={w}:{h}:{x}:{y},format=gray','-f','rawvideo','-'],capture_output=True).stdout
for r in range(h): print(''.join(' .:-=+*#%@'[min(9,max(0,(235-d[r*w+c])//20))] for c in range(w)))
