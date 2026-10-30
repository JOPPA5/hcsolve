import sys
codes = "A .- B -... C -.-. D -.. E . F ..-. G --. H .... I .. J .--- K -.- L .-.. M -- N -. O --- P .--. Q --.- R .-. S ... T - U ..- V ...- W .-- X -..- Y -.-- Z --.. , --..-- ? ..--..".split()
table = {codes[i+1]: codes[i] for i in range(0, len(codes), 2)}
for line in open(sys.argv[1]):
    line=line.strip()
    if not line or line[0]=="#": continue
    tag, body = line.split(":",1)
    out=[]
    for t in body.split():
        if t=="/": out.append(" "); continue
        m=t.replace("T","-").replace("s",".")
        out.append(table.get(m, "<%s>"%m))
    print(tag, "".join(out).strip())
