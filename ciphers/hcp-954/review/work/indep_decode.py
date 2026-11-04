# Independent check (reviewer): my own transcription of the 12 pencil lines, read from hi-res crops.
import sys
mine = """2 5 18 19 5 13 | 4 1 13 10 | 6 20 17 | 4 5
9 13 5 | 11 9 5 2 5 13 | 10 1 17 19 5 13
22 9 5 | 18 5 8 13 5 | 9 3 8 | 12 9 3 8
25 20 | 4 9 17 | 12 5 9 13 5 | 7 20 19 5 | 12
9 3 8 | 11 9 5 2 5 | 4 9 3 8 | 4 14 3 8
18 14 | 18 5 8 17 12 5 9 13 5 13
2 17 9 5 6 | 8 1 18 19 | 4 20
4 14 3 8 | 5 17 8 1 11 19 5 13
6 17 5 20 13 4 11 9 3 8 5
7 17 20 18 25 5
5 22 9 7
4 5 9 13 3 1 17 11"""
A = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
nums = [int(t) for t in mine.split() if t != "|"]
out = "".join(A[n-1] for n in nums)
print(len(nums), out)
from collections import Counter
print(sorted(Counter(nums).items()))
# compare with solver transcription
sol = [t.rstrip("u") for l in open("work/transcription.txt") if not l.startswith("#") for t in l.split() if t not in "/.?"]
print("solver numbers:", len(sol), "identical:", [int(x) for x in sol] == nums)
