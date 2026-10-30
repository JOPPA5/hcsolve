# Reviewer's independent decoder (hcp-1478). Own transcription from 4-7x crops.
import string
A = string.ascii_lowercase
xor2 = {A[i]: (A[i ^ 2] if (i ^ 2) < 26 else A[i]) for i in range(26)}
# reviewer transcription (first glyph of line 1 = k-shaped capital, given as 'R?')
lines = ["Rm oy mup", "adrfkpe", "ukrf", "qkpbgtgqr", "jmxg htmo", "rymwt", "jmxkpe"]
sig = "Depgy"
def d(s, t):
    return "".join(t.get(c.lower(), c) if c.isalpha() else c for c in s)
print("pure XOR2 (involution incl. a<->c, b<->d):")
for l in lines + [sig]:
    print(f"  {l:12s} {d(l, xor2)}")
# solver abcd variant: cipher->plain a->b, b->c, c->d, d->a
var = dict(xor2); var.update({"a": "b", "b": "c", "c": "d", "d": "a"})
print("solver abcd rotation:")
for l in lines + [sig, "Pepgy"]:
    print(f"  {l:12s} {d(l, var)}")
# letters actually used in cipher
used = sorted(set("".join(lines).lower().replace(" ", "")))
print("cipher letters used:", "".join(used))
print("only-abcd-dependent glyphs:", [(l, c) for l in lines for c in l if c.lower() in "abcd"])
