import glob
from PIL import Image, ImageOps
im=Image.open(glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1214/work/hires/*adr.jpg')[0]).convert('L')
s=3445/1400
# boxes in full.png coords
B={'a_r1end':(440,45,570,110),'b_r2':(240,80,600,130),'c_r6':(380,270,540,330),'d_r7':(280,320,590,380),
'e_r8':(40,380,300,435),'f_r9end':(300,395,650,440),'g_r10end':(330,430,620,480),'h_r11':(40,510,330,560),'i_r11b':(230,490,590,535),
'j_r12':(260,520,560,565),'k_r13':(40,590,350,650),'l_r13b':(330,560,650,620),'m_r14':(40,640,300,700),'n_r14b':(290,600,620,670),
'o_r15':(40,680,330,730),'p_r15b':(290,640,660,700),'q_r16':(40,710,340,760),'r_r17':(40,740,350,790),'s_r17b':(320,720,680,770),'t_r3':(30,130,600,180),'u_r6s':(30,285,330,335),'v_r4':(30,175,320,225)}
for k,b in B.items():
    c=im.crop(tuple(int(v*s) for v in b)); c=ImageOps.autocontrast(c,cutoff=1)
    f=2; c=c.resize((c.width*f,c.height*f),Image.LANCZOS); c.save(k+'.png')
