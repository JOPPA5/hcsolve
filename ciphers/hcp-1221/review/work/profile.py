from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1221/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-66_adr.jpg').convert('RGB')
def prof(name,x0,x1,y0,y1):
    out=[]
    for y in range(y0,y1,3):
        n=sum(1 for x in range(x0,x1) for r,g,b in [im.getpixel((x,y))] if r-g>70)
        out.append(n)
    print(name,x0,x1,y0,y1); print(' '.join(map(str,out)))
prof('row16 sign after rr',945,1025,1610,1700)
prof('row16 e of ter',395,470,1590,1690)
prof('row16 a of hat',1350,1420,1600,1660)
