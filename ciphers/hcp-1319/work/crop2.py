from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-107_adr.jpg').convert('RGB')
s=1.72
B={'a_r3end':(590,190,910,270),'b_r3l':(60,205,420,275),'c_r4':(60,265,460,340),'d_r5mid':(200,340,520,430),'e_r6end':(640,430,890,510),
'f_r7a':(60,490,300,560),'g_r7b':(370,495,640,570),'h_r9a':(50,625,330,700),'i_r9b':(340,630,620,710),'j_r9c':(640,630,880,720),'k_r10a':(60,680,420,770),'l_r10b':(380,700,840,790),'m_r11':(70,765,460,840),'n_r11b':(380,820,750,885),'o_r1314':(70,870,830,1020)}
for k,b in B.items():
    c=im.crop(tuple(int(x*s) for x in b)); f=3
    if c.width*f>1600: f=1600/c.width
    c=c.resize((int(c.width*f),int(c.height*f)),Image.LANCZOS); ImageEnhance.Contrast(c).enhance(1.4).save(f'crops/{k}.png')
