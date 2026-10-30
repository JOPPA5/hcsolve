# Reviewer's independent reading (from rotated crops full.png/l12/l34/tog/l78/last), glyph names my own.
rows = """two eps one T two
seven pct seven hash one five zero six plus pct seven nine EIGHT one plus zero
seven eight eps one T two eq T zero nine
dash zero u eight one V eps dash zero u eq zero T plus plus zero pct pct
eps six nine eps one five five pct zero plus DARK plus pct eight eps T
Dcur zero T four seven six plus eps V eps T dash two one dash
five eps pct nine eps eight eps one T eq T zero nine dash zero u
seven eq dash zero u Dcur one six pct pct zero
C five one T eps six C eps"""
# key derived only from the cipher words that are certain from the plain-hand context
key = dict(two='D',eps='E',one='A',T='R',seven='I',pct='T',hash='S',five='L',zero='O',six='N',
           plus='G',nine='M',eight='H',eq='F',dash='Y',u='U',V='V',four='K',Dcur='W',C='C')
n=0; out=[]
for r in rows.splitlines():
    s=''
    for t in r.split():
        n+=1; s+=key.get(t,'['+t+']')
    out.append(s)
print("\n".join(out)); print("signs:",n,"distinct:",len(set(" ".join(rows.split()).split())))
