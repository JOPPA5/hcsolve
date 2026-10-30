import sys,string
t=open(sys.argv[1]).read()
up=string.ascii_uppercase; lo=string.ascii_lowercase
tab=str.maketrans(up[1:]+up[:1]+lo[1:]+lo[:1], up+lo)
print(t.translate(tab),end="")
