# Independent check (reviewer): numbers -> letters, A=1..Z=25 without J, and also A=1..26 for contrast
import sys
rows = [  # read by reviewer from review/work/seg0-2.png
 ["13.1.18.18.14.22"],
 ["8.5.17.25.11.9.3.8.5.13", "7.17.20.18.25"],
 ["18.5.13.4.5.19", "9.8.13.5.13"],
 ["6.17.9.4.1", "12.9.18.3.8.10.5"],
]
for name, alpha in (("25 no J", "ABCDEFGHIKLMNOPQRSTUVWXYZ"), ("26", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")):
    print("--", name)
    n = 0
    for r in rows:
        out = []
        for w in r:
            nums = [int(x) for x in w.split(".")]; n += len(nums)
            out.append("".join(alpha[k-1] for k in nums))
        print(" ".join(out))
    print("numbers:", n)
