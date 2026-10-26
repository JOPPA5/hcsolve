# Independent reviewer decoder for HCP 1514: numeric lines A1Z26; letter words rotated right by one.
import sys, re
lines = open(sys.argv[1]).read().strip().split("\n")
nnum = nlet = 0
for line in lines:
    if re.fullmatch(r"[\d. ]+", line):
        nums = [int(x) for x in re.findall(r"\d+", line)]
        nnum += len(nums)
        assert all(1 <= x <= 26 for x in nums)
        print("".join(chr(64 + x) for x in nums))
    else:
        out = []
        for tok in line.split():
            w = re.match(r"[A-Za-z]+", tok).group(0); rest = tok[len(w):]
            nlet += len(w)
            out.append(w[-1] + w[:-1] + rest)
        print(" ".join(out))
print(f"# numeric positions={nnum} letters={nlet}")
