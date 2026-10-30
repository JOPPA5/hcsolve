import sys
# key typed independently from the SOLUTION.md table (cipher -> plain)
K=dict(zip("123456 8qgfhtrcsnmpbdy".replace(' ',''),"yuoiea lzkvrdhscmnbptj".replace(' ','')))
K['H']='ch'
for line in open(sys.argv[1]):
    tag,_,ct=line.rstrip('\n').partition(' ')
    out=''
    i=0
    while i<len(ct):
        if ct.startswith('[heart]',i): out+='♡'; i+=7; continue
        ch=ct[i]; out+=K.get(ch,ch) if ch not in ' ,.?:-' else ch
        if ch not in K and ch not in ' ,.?:-': out+='<?>'
        i+=1
    print(tag,out)
