# Independent reviewer decode: my own sign-by-sign reading of the hi-res address scan,
# decoded with the American (landline) Morse alphabet. '_' = long dash (L).
AM={'.-':'A','-...':'B','.. .':'C','-..':'D','.':'E','.-.':'F','--.':'G','....':'H','..':'I',
 '-.-.':'J','-.-':'K','_':'L','--':'M','-.':'N','. .':'O','.....':'P','..-.':'Q','. ..':'R',
 '...':'S','-':'T','..-':'U','...-':'V','.--':'W','.-..':'X','.. ..':'Y','... .':'Z',
 '.--.':'1','..-..':'2','...-.':'3','....-':'4','---':'5','......':'6','--..':'7','-....':'8','-..-':'9'}
rows=[ # letters separated by '|', words by ','
 ". ..|.|.. .|-.. , .. ..|. .",
 "..-|. .. , .. .|.-|. ..|-.. ,",
 "-|....|..|... , .-|-- ,",
 ". .|.--|..|_|_ , .--|. ..",   # I(wide gap) W I L L(medium dashes, read L by sense) / W R
 "..|-|. , ...|. .|. .|-. , --", # SOON: 2nd O drawn tight (literally I)
 ".. ..|, .-|-..|-..|. ..|.|...|... , ..|... ,",
 "....-|---|--.. , .. .|.-|. ..|. ..|. .|_|_ ,",
 "...|- , .-|-.-|. ..|. .|-.|. .|....|..|. .",
]
words=[]
cur=''
for tok in '|'.join(rows).replace(',','|,|').split('|'):
    t=tok.strip()
    if t==',': words.append(cur); cur=''; continue
    if t: cur+=AM[t]
words.append(cur)
print(' '.join(w for w in words if w))
