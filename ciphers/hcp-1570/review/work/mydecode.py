import sys
K={'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','8':'l','q':'z','g':'k','f':'v','h':'r','t':'d','r':'h','c':'s','s':'c','n':'m','m':'n','p':'b','b':'p','d':'t','y':'j','H':'ch','G':'g'}
src=open(sys.argv[1]).read().replace('{U1}','G')
out=''.join(K.get(c,c) for c in src)
print(out)
n=sum(1 for c in src if c in K); print('units',n,'unmapped',sum(1 for c in src if c.isalnum() and c not in K))
