# Independent reviewer decode of hcp-1432 from the reviewer's own pixel transcript
# (component measurements in comps.py output; see REVIEW1.md).
M={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I',
'.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
'...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
rows=[
 ('thanks-1','-.- .. -.'),
 ('thanks-2','-.. -. . ... ... --- -. ...'),
 ('thanks-3','.- - ..- .-. -.. .- -.--'),
 ('tired-1','...- .[-x] .-. -.-- - ..'),  # [-x] = dash crossed by the separator slash
 ('tired-2','.-. . -..'),
 ('home-1','.-. . .- .-.- .... . -.. ....'),
 ('home-2','--- -- .'),
 ('closing','- -. ..- .'),
]
n=0;bad=0;out=[]
for rid,s in rows:
  w=''
  for g in s.split():
    n+=1
    core=g.replace('[-x]','')
    if core in M: w+=M[core]
    else: w+='{'+core+'}';bad+=1
  out.append(w);print(f'{rid:9s} {s:40s} {w}')
print(n,'groups,',bad,'non-alphabet')
print(' | '.join(out))
