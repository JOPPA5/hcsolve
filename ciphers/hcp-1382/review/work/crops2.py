from PIL import Image
n=Image.open('work/crops/rot.png').convert('L') if 0 else None
r=Image.open('work/crops/rot.png'); print(r.size, r.mode)
m=Image.open('work/crops/norm.png'); print(m.size, m.mode)
