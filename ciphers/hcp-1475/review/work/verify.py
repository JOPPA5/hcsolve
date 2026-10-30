"""Reviewer check for hcp-1475: own transcription, shift/atbash test, initialism pattern."""
import string
ct = "ILMWAMWLM"   # reviewer's own reading from review/work/mid_x7.png, end_x8.png
A = string.ascii_uppercase
for k in range(26):
    print(k, "".join(A[(A.index(c)+k) % 26] for c in ct))
print("atbash", "".join(A[25-A.index(c)] for c in ct))
# initialism: independent dictionary of words, one word per letter, same word-stem for repeats
words = {"I": "I", "L": "love", "M": "my", "W": "wife", "A": "and"}
pt = [words[c] for c in ct]
pt[7] = "loves"; pt[8] = "me"          # inflection only, stems unchanged
print(" ".join(pt) + ".")
