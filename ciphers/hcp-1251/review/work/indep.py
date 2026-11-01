"""Reviewer's independent decode. Own sign-class transcription of sample rows made from enlarged crops,
decoded with the family key of ciphers/hcp-1216/work/graphic-key.json (not this card's key.json),
then diffed against the solver's ledger. Run: python3 -I ciphers/hcp-1251/review/work/indep.py"""
import json, os, re, difflib
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
K=json.load(open(os.path.join(R,'..','hcp-1216','work','graphic-key.json'),encoding='utf-8'))
A={'2':'two-bars','3':'three-bars','6':'six','B':'left-bowl','S':'right-bowl','d':'joined-two-strokes','+':'cross',
'g':'open-loop-descender','h':'tall-short-stroke','i':'dotted-crossed-curve','T':'inverted-T','k':'section-mark','~':'wave',
'm':'three-short-strokes','n':'two-short-strokes','o':'cursive-loop','F':'F','L':'gamma','x':'x','v':'chevron','y':'low-descender','z':'crossed-diagonal'}
rows={
'01':'S z 3 F 3 L 3 L 3 d 3 S T o ~ 2 n k 2 m 6 3',
'04':'3 n k x ~ d L 3 m m 2 g 2 n 2 k 3 g y ~ 2 h o L',   # reviewer: ends p-o-t; no b, e
'05':'m x ~ L ~ 3 v 3 ~ 3 F 3 T 2 S z 6 3 F 3 n y 6 3',
'12':'2 m o S L 2 n i i g 2 z 2 v 2 n 3 d 3 S 3 m h o g y',
'15':'2 L 3 F v 3 h o g y S z 3 L v 2 ~ 2 S S z o n 6 3 n',   # reviewer: two bars in -val-
'18':'h 2 L 2 ~ o m 2 m i 3 ~ v 2 S z o n 3 g y m 2 S',
'20':'x L o ~ T 2 F 2 3 d 3 S 3 m 6 2 F m i T 3 n',          # reviewer: 6 + two bars + dot, see REVIEW1
'26a':'k o S z n o m m 2 g 2 n 2 k 3 d 3 S 3 m h o g y',      # single section mark
'28':'k 3 F 3 S n i h o g y S z 3 n y 3 n 3 g y B S 2 ~ 2 d o L 3 ~ L 2 F L S 2 k B S 2 k 3 z',
}
L={}
for l in open(os.path.join(R,'work','ledger.txt'),encoding='utf-8'):
    if l.strip() and not l.startswith('#'):
        a,b=l.split(); L[a]=re.sub(r'[\[\]{}]','',b)
deacc=str.maketrans('öüőóéá','ouooea')
for r,t in rows.items():
    s=''.join({'left-bowl':'c'}.get(A[c],'') or K[A[c]] for c in t.split())
    s=s.replace('cS','c')
    s=s.replace('cs','c')
    # the bowl pair () is one sign c = cs in the ledger
    s=s.replace('p','h')
    led=L[r[:2]].translate(deacc)
    if r=='26a': led=led[:len(s)+1]
    print(r,'mine  ',s); print('  ','ledger',led)
    d=[o for o in difflib.SequenceMatcher(None,s,led,autojunk=False).get_opcodes() if o[0]!='equal']
    print('   diff',[(o[0],s[o[1]:o[2]],led[o[3]:o[4]]) for o in d])
