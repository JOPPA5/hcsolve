from PIL import Image
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1256/review/work/'
a=[Image.open(out+n+'.png') for n in ('z24a','z24b')]
c=Image.new('RGB',(max(i.width for i in a),sum(i.height for i in a)+10),'white')
y=0
for i in a: c.paste(i,(0,y)); y+=i.height+10
c.save(out+'z24.png')
