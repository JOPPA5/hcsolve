import sys, re
key={'s':'D','e':'E','a':'A','r':'R','l':'L','b':'B','t':'T','i':'I','i2':'I','m':'M','S':'S','o':'O','y':'Y','u':'U','g':'G','n':'N','h':'H','w':'W','d':'D'}
for line in open(sys.argv[1]):
    if not line.startswith('L'): continue
    lab,body=line.split(':',1)
    out=[]
    for tok in re.findall(r'\[[^\]]*\]|\S+',body):
        out.append(tok if tok.startswith('[') else key.get(tok,'<'+tok+'>'))
    print(lab, ''.join(o if len(o)==1 else ' '+o+' ' for o in out))
