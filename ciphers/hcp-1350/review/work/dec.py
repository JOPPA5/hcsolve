import sys,re
t=open(sys.argv[1]).read()
o=''.join(chr((ord(c.upper())-65-1)%26+65) if c.isalpha() else c for c in t)
print(o); print(sum(c.isalpha() for c in t))
