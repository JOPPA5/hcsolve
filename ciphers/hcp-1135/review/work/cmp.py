import re
sol=[l.rstrip('\n') for l in open('../../work/transcription.txt',encoding='utf-8') if l[0]!='#']
rev=re.search(r'T="""(.*?)"""',open('decode_review.py',encoding='utf-8').read(),re.S).group(1).split('\n')
def norm(s):
    o=[]
    for t in s.replace('|',' ').split():
        if t=='-' or t[0]=='=': continue
        o.append(t.split('~')[0].replace('?',''))
    return o
a=[t for l in sol for t in norm(l)]; b=[t for l in rev for t in norm(l)]
print(len(a),len(b))
import difflib
for op in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
    if op[0]!='equal': print(op,a[op[1]:op[2]],b[op[3]:op[4]])
