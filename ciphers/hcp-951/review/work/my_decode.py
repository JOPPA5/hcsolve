# Reviewer's independent decode of hcp-951 from my own reading of the hires scan.
rows = [
 [[9,12,19,5],[19,3,8,23,1,18,26,5]],
 [[4,15,2,5,12,14]],
 [[2,18,5,9,20,5]],
 [[19,20,18,1,19,5],[14,18],[19]],
]
for r in rows:
    print(" ".join("".join(chr(64+n) for n in w) for w in r))
alt = [9,18,5,9,20,5]
print("alt row3 with 9:", "".join(chr(64+n) for n in alt))
print("alt split 18,2,6,5:", "".join(chr(64+n) for n in [1,18,2,6,5]))
