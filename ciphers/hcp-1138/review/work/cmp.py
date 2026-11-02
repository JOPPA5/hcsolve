import re,difflib
src=open('own_decode.py',encoding='utf-8').read()
rows=re.search(r'ROWS="""(.*?)"""',src,re.S).group(1)
me=[t for t in rows.replace('/',' ').split()]
me=['9~' if t=='z' else t for t in me]
sol=[]
for l in open('../../work/transcription.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    sol+= [t for t in l.split('|')[0].split() if t!='#']
print(len(me),len(sol))
for op,a,b,c,d in difflib.SequenceMatcher(None,sol,me,autojunk=False).get_opcodes():
    if op!='equal': print(op,a,sol[max(a-2,0):a],sol[a:b],'->',me[c:d])
