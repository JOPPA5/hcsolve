# Independent reviewer transcription of the main rows (own glyph names, own key, written from review crops).
# Glyphs: 2=two bars 3=three bars n=2 strokes m=3 strokes L=wave t=gamma T=inverted-T s=right bowl c=left bowl F=F-sign
# b=six x=diag cross(u) z=crossed-with-hook(z) +=upright cross(f) O=loop(no dot) I=dotted/crossed loop G=g-hook S=S-hook(k) K=section(k)
# Y=long tail(y) V=chevron R=right tick stroke(h/p) D=left tick stroke(d) W=loop with two dots(oe) -=struck
import collections,re,sys
key=dict(zip('23nmLtTscFbxz+OIGSKYVRDW',['a','e','n','m','l','t','j','s','c','r','b','u','z','f','o','i','g','k','k','y','v','h','d','ö']))
rows="""
s z 3 F 3 t 3 t 3 D 3 s T O L 2 n K 2 m S I
V 2 n O m R O G Y 2 L 3 G T O b b 3 G 3 s s 3 G
b 3 n t 2 L 2 L T 2 s O F 2 I m S 3 D V 3 s T O
- L 2 n S 2 m R O G Y m x L 2 t O t t 2
m x L 2 t s 2 G b 2 F 3 m 3 L 3 m T O L
b 2 F 3 n I s 3 L m 3 R 3 t 3 m V O L
n 2 I G 2 z 2 n s 2 T n 2 L O m R O G Y
n 3 m S 2 D t 2 m m 3 G 3 G Y n 2 R
R 2 L 3 L W b b m I n t I F t 2 m
I s L 3 t V O L n 2 2 n Y I s z 2 b 2 D
s 2 G O m R O G Y 3 L m 3 R 3 t 3 m
V O L n 2 R 3 3 z 3 n m 2 F
n 3 m L 3 R 3 t s 3 G I t 3 n I m 2 T D
m x L 2 t x n S R 2 + 3 L T W n
R 3 s t F 3 2 m I m 2 F c s 2 K
R O n 2 R L 2 s 2 n m 2 T D 3 L
m x L I S 2 z I s K 3 D V 3 s 3 m
I F T O n - R O G Y m x L 2 t O t
2 z t R I s z 3 m x t O L s O 2 F O S
s z 2 L 2 s O m x L 2 t s 2 G b 2
V O L t m O s t 3 n m O s t
m 2 s t I F O S m I V 3 L n 3 m
t x D O S m I t I F I F T O n
s O S 2 t R O G Y s O S 2 t
t x D 2 S V 2 L 3 s z O L n I
I s t 3 n V 3 L 3 D 3 s 3 m
""".strip().split('\n')
pl=[''.join(key[g] for g in r.split() if g!='-') for r in rows]
led=[]
for l in open('work/ledger.txt',encoding='utf-8'):
    if l[0] in '#\n':continue
    lab,*t=l.split()
    if lab.isdigit() and int(lab)<=26:
        s=''
        for x in t:
            x=x.lstrip('?')
            s+={'K2':'k','I0':'i','CS':'cs','O:':'ö','A:':'a','~x~':'','2½':''}.get(x,x.lower())
        led.append(s)
for i,(a,b) in enumerate(zip(pl,led),1):
    print(f'{i:02d}', 'OK ' if a==b else 'DIFF', a, '' if a==b else b)
t=''.join(led)
print(len(t), {w:t.count(w) for w in ['hogy','mulat','kedves','elmehetem','sokat']})
print(collections.Counter(pl and ''.join(pl)).most_common())
