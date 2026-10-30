from PIL import Image
im=Image.open('msg.png')
boxes={'a1':(340,195,700,300),'a2':(690,195,1070,325),'b1':(340,305,700,445),'b2':(720,325,1085,445),'c1':(340,430,700,585),'c2':(620,440,1085,610),'d1':(320,575,640,680),'d2':(620,600,1070,725),'e1':(330,685,700,790),'e2':(680,700,1060,835)}
for k,b in boxes.items():
    c=im.crop(b); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(k+'.png')
