# Independent reviewer decode of my own transcription (read from hi-res crops in review/work/)
import string
L=[l for l in string.ascii_uppercase if l!='J']
K={n:L[n-2] for n in range(2,27)}
mine = """12.10.6.3.6.18 7.18.10.20.26
10.4.9 11.15.13.13.6 9.6.21.20
23.10.6.5.6.18 6.10.14
3.10.19.4.9.6.14 26.26
5.10.18 23.6.14 6.19
18.6.4.9.20 10.19.20
9.6.18.26 12.10.6.14
8.18.21.19 21 11.21.19
5.6.10.14.6 13.10.14.14.2"""
nums=[]
for line in mine.splitlines():
    print(' '.join(''.join(K[int(x)] for x in w.split('.')) for w in line.split()))
    nums += [int(x) for w in line.split() for x in w.split('.')]
print(len(nums),'numbers; distinct',sorted(set(nums)))
