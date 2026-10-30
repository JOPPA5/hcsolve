# independent re-reading by the reviewer: glyph classes only, typed from review crops, no letters
# classes: u(U incl. heavy) o x r(R) 9(Q) l(L) P N T n(theta) f(rho) t(I) V w(W) E S z(s) y(Y) j(Z)
import itertools,re,collections
mine="""u o 9 n 9 t x | l x | P r o | T x l u T u x
n u x | u r n E u f | V x w x
u f | T 9 n T x | E x l u f | 9 x l
u o r | t r n E x | l r | 9 l | 9 u f
f r 9 u l | T x P | u | N u P u
9 l x u u u r V N r n t r | 9 u
l u | x | V u w u l | n x u x
u x | f x V | 9 x f t x | y u | l r u r
P x f | T u | r f t u l | o P
S r 9 j x | u x | V o 9 z 9 t x
f u o l u l r f | u | V u o l u
r | 9 u o V x | r | o P | u S l u
T x | l u | t o u | t l 9 z | u t r
V x w x | u P x l f 9 t x""".split('\n')
M={'u':'aqv','o':'u','x':'o','r':'e','9':'ip','l':'dr','P':'m','N':'m','T':'c','n':'n','f':'s','t':'t','V':'l','w':'g','E':'h','S':'b','z':'z','y':'j','j':'j'}
sol=[]
for l in open('ciphers/hcp-1333/work/transcription.txt',encoding='utf8'):
    if l[0]=='#' or not l.strip(): continue
    sol.append([t.rstrip('!').split('.') for t in l.split() if t not in '/-'])
name={'U':'u','O':'o','X':'x','R':'r','Q':'9','L':'l','P':'P','N':'N','T':'T','H':'n','F':'f','I':'t','V':'V','W':'w','E':'E','S':'S','s':'z','Y':'y','Z':'j'}
tot=0;bad=0;words=[]
for i,(m,s) in enumerate(zip(mine,sol),1):
    a=[c for c in m.split() if c!='|']; b=[name[c[0]] for c in s]
    tot+=len(a)
    if a!=b: bad+=1; print('line',i,'DIFF',a,b)
    words+= [w.split() for w in m.split('|')]
print('lines',len(mine),'signs',tot,'differing lines',bad)
print('class freq',collections.Counter(c for w in words for c in w).most_common())
print('per-word candidate counts:')
for w in words:
    c=[''.join(p) for p in itertools.product(*[M[x] for x in w])]
    print(''.join(w),len(c),c[:12])
