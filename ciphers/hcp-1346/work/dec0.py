import re
K={"0":"0","0'":"a","1":"e","1'":"b","2'":"c","2":"C","3'":"g","3":"3","4":"h","5":"i","5'":"I","6":"6","6'":"r","7":"l","7'":"s","8":"n","8'":"t","9":"o","9'":"9'","4'":"4'"}
for l in open('transcription.txt'):
    if l.startswith('#'): print(l.strip()); continue
    o=[]
    for w in l.split():
        toks=re.findall(r"\d\.?",w)
        o.append(''.join(K.get(t.replace('.',"'"),'['+t+']') for t in toks))
    print(l.strip(),' => ',' '.join(o))
