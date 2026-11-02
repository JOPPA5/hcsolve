"""Reviewer's independent decode of HCP1239. Sign names below were keyed by the reviewer from
review/work/crops2/* WITHOUT using work/ledger.txt tokens; sign table from ciphers/hcp-1216/SOLUTION.md.
Sign names: bars2 bars3 six cL(left bowl) sR(right bowl) stRL(d: short-left+long-right) stLR(h/p: long-left+short-right)
gam(t) sec(k) oct(closed 8=k) wav(l) m3 n2 loop(o) loopd(ö) dot(i) ing(j) Fr(r) x(u) xd(ü) xt(z) chev(v) g gyy pl(f)"""
import re,subprocess,sys,difflib
K=dict(bars2='a',bars3='e',six='b',cL='c',sR='s',stRL='d',stLR='h',gam='t',sec='k',oct='k',wav='l',m3='m',n2='n',loop='o',loopd='ö',
 dot='i',ing='j',Fr='r',x='u',xd='ü',xt='z',chev='v',g='g',y='y',pl='f',P='?')
T={ # row: signs
1:"sec bars3 stRL chev bars3 sR ing loop wav bars2 n2 sec bars2 m3 six bars3 cL sR bars3 sR",
2:"sR loop Fr bars2 dot gam sec loop sR xt loop n2 bars3 gam bars3 wav",
3:"m3 bars3 g sec bars2 stRL gam bars2 m3 dot g bars2 xt bars2 n2 sR bars2 ing n2 bars2",
4:"wav loop m3 stLR loop g y bars3 n2 m3 dot bars2 gam gam bars2 m3",
5:"bars2 n2 y dot gam sR xt bars3 n2 chev bars3 stRL stRL bars3 n2 bars3 m3 gam bars3",
6:"stRL bars3 gam bars3 oct Fr loop wav bars2 sec bars3 stRL chev bars3 sR ing loop",
7:"wav bars2 n2 sec bars2 m3 ing loop ing ing loopd n2 bars3 wav bars2",
8:"stRL bars2 wav bars3 sR gam bars3 ing Fr bars3 cL sR xd gam loopd Fr",
9:"gam loopd Fr gam loop sec loopd n2 dot stRL bars3 pl bars3 sec bars3",
10:"gam bars3 Fr x stLR bars2 six bars2 n2 dot sR bars3 wav ing loopd stLR bars3 gam",
11:"m3 loop cL xt bars2 Fr x Fr bars3 oct bars2 gam dot sR m3 bars3 g",
12:"stLR dot chev gam bars2 m3 bars2 sR xt loop n2 y sR bars2 g bars2 wav",
13:"dot sR bars3 wav ing loopd n2 bars3 gam stLR bars2 cL sR gam bars3 stLR gam dot",
14:"ing loopd ing loopd n2 bars3 wav bars3 stRL bars3 P bars3 m3 six dot sR xt gam bars2",
15:"gam loop chev bars2 wav bars2 sR xt bars2 gam chev bars2 Fr chev bars2",
16:"m3 bars2 Fr bars2 stRL loop oct loopd sR xt dot n2 gam bars3 gam dot sR xt",
17:"gam bars3 wav loopd ing bars3 dot sR gam bars3 n2 chev bars3 wav bars3",
18:"bars2 chev dot sR xt loop n2 gam wav bars2 gam bars2 sR Fr bars2",
19:"bars3 n2 P bars3 sR xt gam bars3 wav ing P wav ing bars3 oct dot oct bars3 stRL chev bars3 sR m3 bars2 m3 bars2 ing bars2 bars3 P bars2 stLR ing bars2 gam gam dot sR xt",
20:"gam bars3 wav bars3 gam bars3 m3 bars3 gam",
}
out=subprocess.run([sys.executable,'-I','work/decode.py'],capture_output=True,text=True).stdout
sol={int(m[1]):m[2] for m in re.finditer(r'^ (\d\d) (\S+)$',out,re.M)}
for r,s in T.items():
    mine=''.join(K[t] for t in s.split()); so=sol[r].replace('-','').replace(':','').replace('[+]','?').replace('[#]','?') 
    so=__import__('unicodedata').normalize('NFC',so)
    d=[(a,b) for a,b in zip(mine,so) if a!=b and a!='?']
    print(r,mine,'SAME' if mine==so else ('LEN' if len(mine)!=len(so) else f'DIFF {d}'), '' if mine==so else so)
