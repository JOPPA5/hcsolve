"""One-off: expands the row-by-row reading (one item = one sign) into ledger-opus.txt tokens."""
import re
R="""01 n e h a r a g u d j o n e r t e h o gy
02 i j s ü r ü n k ü l d ö m a l a p o
03 k a t d e e n n e m a gy g o n d o l
04 k o z o m m i n t ö n e n e k e m
05 j o l e s i k h a ö n n e l b e s z e l
06 h e t e k e d e s j o l a n k a m m e r t
07 e n m i k o r s o r a i m i r o m
08 ö #! n n? e k u gy e r z e m m a g a m m i n t
09 h a b e s z l g n e k e d e s j o l a n k a m
10 e l s e m t u d j a k e p z e l a i m i l y
11 h o s z u i d ö a z m e g m e g k a
12 p o m s o r i t u gy s z e r e t n e m
13 h a r e p ü l n e a l e v! e l e r e p ü l ö
14 g e p e t s z e r z e k b e h o gy gy
15 o r s a b a n j ö n n e b e cs e s l a p j a i
16 M^ i d e n g o n d o l a t n a l
17 a t e t t l e g t ö b b e t e r
18 i gy t e s! z k i cs ó k o t a d
19 s n e m p e d i g l e n k e r
E b . s o r a i t
B v a r v a m a r a m a r a d o k s z i v e n e k r a b s z o l g a j a f e r i
S1 i s t e n v e l e
S2 a t a v o l b .
S3 o l cs o k o
S4 l j a s z a m
S5 t a l a n s z o
S6 r"""
K={'r':'F','s':')','u':'X','b':'6','f':'+','ü':'X:d','ö':'O:d','ó':'O:a','gy':'GY','cs':'CS','.':'.','M':'M','n!':'N!','n?':'N?','v!':'V!','s!':')!'}
out=["# HCP1261 sign ledger, Claude Opus 5.5, 2026-11-01, read from enlarged crops of work/hires/*_adr.jpg (work/crops/).",
"# One token = one written sign. F=r )=s X=u 6=b +=f, H and P are one sign (long stroke + tick, h/p near-homograph), GY/CS digraphs,",
"# :d visible double dot, :a single mark. ! = blotted/overwritten sign read on word sense; N? = ambiguous two-stroke sign read n. Other acutes not transcribed.",
"# #! = heavy blot with no value of its own (see SOLUTION.md, uncertainty 2; added after review 1); M^ = plain Latin cursive capital M, not the cipher sign (added after review 1).",
"# Rows: 01-19 main; E left edge (runs down the edge into B); B bottom edge; S1-S6 stamp box in cipher. S6/S7 continue in PLAIN cursive: see decode_opus.py."]
for l in R.split('\n'):
    lab,*t=l.split()
    out.append(lab+' '+' '.join(K.get(x,x.upper()) for x in t))
open('ledger-opus.txt','w',encoding='utf-8').write('\n'.join(out)+'\n')
