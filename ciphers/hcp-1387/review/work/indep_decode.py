import json,sys
rows=json.load(open(sys.argv[1]))["rows"]
n=0
for r in rows:
    out=''.join(chr((ord(c)-ord('A')-1)%26+ord('A')) if c.isupper() else chr((ord(c)-ord('a')-1)%26+ord('a')) if c.islower() else c for c in r)
    n+=sum(c.isalpha() for c in r); print(out)
print("letters",n)
