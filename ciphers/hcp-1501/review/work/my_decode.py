import sys,re
M={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
out=[];bad=0;n=0
for l in open(sys.argv[1]):
    if not l.startswith('L'):continue
    body=l.split(':',1)[1].strip()
    s=''
    for tok in body.split():
        if tok=='/': s+=' ';continue
        n+=1
        c=M.get(tok)
        if c is None: bad+=1; c='?'
        s+=c
    out.append(s)
print(f'groups={n} invalid={bad}')
print('|'.join(out))
