# One-off helper: turns the hand-read rows (letter values, read from enlarged crops) into sign tokens for ledger.txt.
R="""01 szeretetedesjolankamedesegyet
02 lenremenyemkivanomhogy
03 alegjobbegessegbentalaljaso
04 raimsajnalattalveszem[t][u][d]o
05 masulhogyutobbisoraojke
06 sOnvalaszoltamvolna
07 barenmikormegkaPtamrOg
08 tOnvalaszoltammert
09 azthiszemedesemhogyma
10 gaisojotnehezenvarja
11 soraimintamijennehe
12 zenvaromamagabecsesso
13 rai[t]higyjeeledesemszo
14 valkisemlehetfejezniazt
15 azerzesemielfogtaszi
16 vemmikorbecsessoraitel
17 olvastamcsakeztsajnaltam
18 hogymiert[n]incsitazezen
19 gyalkaamelikesoroket
20 irjahogyszivemhezOlel
21 hetnemhogyhaderazhetne
22 teljesenboldognakma
23 gathigyjeeledesemugyfaj
24 aszIvemhogynemletha
25 tomcsakaztszeretnemtud
26 nimedigkelmegazegyUtle
27 tUnkigazenarvaszivemnekcsinalomedesemhogyojha
28 marbelenyugszikhogyhaegyicsitesetlegkesikalaPom
29 abolkelazt[f]etetelezni hogykOnyenefelejteneha asor
E1 sszetvalasztanabenUnket
S1 istenvele
S2 edesem
S3 csokolja
S4 szamta
S5 lanszor
S6 sirig
S7 hukedves
S8 seferi"""
M=dict(a='=',b='6',c='(',d='4',e='#',f='+',g='G',h='H',P='P',i='i',j='T',k='S',l='~',m='3',n='2',o='Q',r='F',s=')',t='L',u='X',v='^',y='Y',z='Z',O='Q:',U='X:',I='i:')
out=[]
for line in R.splitlines():
    lab,*w=line.split(); s=''.join(w); t=[]; i=0
    while i<len(s):
        if s.startswith('cs',i): t.append('CS'); i+=2
        elif s[i]=='[': t.append('['+M[s[i+1]]+']'); i+=3
        else: t.append(M[s[i]]); i+=1
    out.append(lab+' '+' '.join(t))
hdr="""# HCP1299 sign ledger, Claude Opus 5.5, 2026-10-30. One token = one written sign, read by eye from enlarged crops of the
# un-converted address scan (work/hires/..._adr.jpg). Not OCR. Rows 01-29 main text (28-29 run on under the address to the
# right corner), E1 up the right edge from the bottom corner, S1-S8 under the stamp.
# Tokens: = a (two bars)  # e (three bars)  6 b  ( c  CS opposed bowls  4 d (long+short joined)  + f (upright cross)
# G g  H h (tall + short)  P same class as H, value p chosen from word sense  i i (crossed curve)  T j (inverted T)
# S k (section mark)  ~ l  3 m (three short strokes)  2 n (two short strokes)  Q o  F r  ) s  L t (gamma)
# X u  ^ v  Y y  Z z (crossed diagonal with tail).  Suffix : = dots seen over the sign.  [x] = sign physically hidden by a blot.
"""
open('ledger.txt','w',encoding='utf-8').write(hdr+'\n'.join(out)+'\n')
