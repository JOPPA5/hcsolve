import json,sys
M={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','.-.-':'Ä','---.':'Ö','..--':'Ü','----':'CH','.--.-':'Á','..-..':'É','.-.-.-':'.','--..--':','}
T=int(sys.argv[1])
cols=json.load(open('work/columns.json'))
for i in range(len(cols)-1,-1,-1):
    groups=[];cur=''
    for m in cols[i]:
        if m['gap'] is not None and m['gap']>T and cur: groups.append(cur);cur=''
        cur+=m['sym']
    groups.append(cur)
    print(i,' '.join(groups),'  ',''.join(M.get(g,'['+g+']') for g in groups))
