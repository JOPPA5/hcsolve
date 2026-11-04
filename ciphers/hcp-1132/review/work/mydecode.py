import sys,re
M={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','..-..':'É','.--.-':'Á','---.':'Ö','..--':'Ü'}
out=[]
for line in open(sys.argv[1],encoding='utf-8'):
    if line.startswith('#') or ':' not in line: continue
    lab,body=line.split(':',1)
    s=''
    for t in body.split():
        if t=='/': s+=' '
        elif t in(',','!','!!'): s+=t
        elif t=='[X]': s+='[X]'
        else: s+=M.get(t,'?'+t+'?')
    out.append((lab.split()[0],s)); print(lab.split()[0],s)
print(''.join(s for _,s in out))
