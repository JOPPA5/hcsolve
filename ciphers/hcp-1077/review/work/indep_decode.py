# Independent reviewer decode of hcp-1077 from my own reading of the pixels.
groups = [[11,20,4,22,9,7],[10,1,11,2,8,5,13,13]]
import string
alphas = {
 'A=1..Z=26 with J': string.ascii_uppercase,
 'no J (I=J)': 'ABCDEFGHIKLMNOPQRSTUVWXYZ',
 'no J, no V (U=V)': 'ABCDEFGHIKLMNOPQRSTUWXYZ',
}
for n,a in alphas.items():
    print(n.ljust(20), ' '.join(''.join(a[x-1] for x in g) for g in groups))
# alternatives for the weak 5 in line 2
a='ABCDEFGHIKLMNOPQRSTUVWXYZ'
for alt in (1,3,5,6,8):
    g=groups[1][:]; g[5]=alt; print('pos6=',alt, ''.join(a[x-1] for x in g))
