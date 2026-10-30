import sys,re
K={"1":"y","2":"u","3":"o","4":"i","5":"e","6":"a","7":"j","8":"l","b":"p","c":"s","d":"t","f":"v","g":"k","h":"r","m":"n","n":"m","p":"b","q":"z","r":"h","s":"c","t":"d","H":"ch"}
for line in open(sys.argv[1]):
    line=line.rstrip("\n")
    if not line: continue
    tag,rest=line.split(" ",1)
    out=re.sub(r"<UNK:\w+>",lambda m:m.group(0),rest)
    res=[];i=0
    while i<len(rest):
        m=re.match(r"<UNK:\w+>",rest[i:])
        if m: res.append(m.group(0)); i+=len(m.group(0)); continue
        ch=rest[i]; res.append(K.get(ch,ch)); i+=1
    print(tag,"".join(res))
