"""Reviewer's independent decode of hcp-1073 from the reviewer's own sign reading (msg_rot.jpg crops).
Key derived independently: digits n -> letter at alphabet index with j omitted, c=1 (abcdefghiklm...).
Words separated by '/'; sign names: s=hook, S2=s-with-two-dots, r=triangle, a=inverted V, n=dash,
x=cross (ch), t=crossed-A, w=double loop, B=tall stroke, P=rho loop; o u ü literal."""
import collections
alpha = 'abcdefghiklmnopqrstuvwxyz'  # j omitted
digit = {str(i): alpha[i+1] for i in range(1,10)}  # 1->c ... 9->l
sym = {'s':'s','S2':'s','r':'r','a':'a','n':'n','x':'ch','t':'t','w':'w','B':'b','P':'st','o':'o','u':'u','ü':'ü'}
lines = [
 "1000 / 5 r ü s s 3 / u . / 8 ü s s 3",
 "s 3 n 2 3 t / 2 7 r",
 "2 3 7 n",
 "2 7 s s 3 9",
 "6 o 4 4 3 n t 9 7 x / 6 7 P / 2 u / 5 3 s u n 2",
 "w 3 n n / n 7 x t / 2 a n n / 9 a n 5 w 3 7 9 3 / 2 7 x",
 "B 7 t t 3 / n 7 x t / s o / u . / 2 3 n 8 / 3 7 n",
 "6 7 S2 x 3 n / a n / 2 3 7 n 3 / t r u 2 3",
]
cnt = collections.Counter(); out=[]
for L in lines:
    words=[]
    for w in L.split('/'):
        s=''
        for t in w.split():
            cnt[t]+=1
            s += t if t in ('1000','.') else digit.get(t) or sym[t]
        words.append(s)
    out.append(' '.join(words))
print('\n'.join(out)); print(sorted(cnt.items(), key=lambda x:-x[1]))
