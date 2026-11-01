from PIL import Image
im=Image.open('../../work/hires/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_adr.jpg').convert('RGB')
def prof(n,x0,x1,y0,y1):
    runs=[];on=None
    for y in range(y0,y1):
        c=sum(1 for x in range(x0,x1) if (lambda p:p[0]-p[1]>70)(im.getpixel((x,y))))
        if c>=5 and on is None:on=y
        if c<5 and on is not None:runs.append((on,y-1));on=None
    if on is not None: runs.append((on,y1-1))
    print(n,len(runs),runs)
prof('r13 after t (claimed e)',1018,1050,1605,1730)
prof('r07 te (control e)',175,215,895,1000)
prof('r15 ta (control a)',945,982,1825,1925)
