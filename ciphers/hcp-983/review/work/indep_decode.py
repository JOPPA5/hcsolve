# Independent reviewer decode of hcp-983 from my own reading of the hi-res scan.
# Tests A1Z26 (26 letters) and alphabets with I=J merged (24/25 letters).
import string
lines = [[[9,14,8],[8,5,17,2,18,19]], [[18,3,8,17,5,9,2,5],[2,1,11,4]]]
alph = {
 'A1Z26': string.ascii_uppercase,
 'IJ merged (25)': 'ABCDEFGHIKLMNOPQRSTUVWXYZ',
}
for name, a in alph.items():
    out = ' / '.join(' '.join(''.join(a[n-1] for n in w) for w in l) for l in lines)
    print(f'{name:16s} {out}')
nums = [n for l in lines for w in l for n in w]
print('numbers used:', sorted(set(nums)), 'count', len(nums))
