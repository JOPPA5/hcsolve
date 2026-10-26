# Independent reviewer decoder for HCP 56: Caesar shift 13 on letters only.
import sys
def rot(s, k=13):
    return "".join(chr((ord(c) - b + k) % 26 + b) if c.isalpha() else c
                   for c in s for b in [65 if c.isupper() else 97])
t = open(sys.argv[1]).read().rstrip("\n")
print(rot(t)); print("# letters:", sum(c.isalpha() for c in t))
