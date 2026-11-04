"""Reviewer's independent decode of hcp-1201 from my own reading of the hires scan."""
import string
# my own sign-by-sign reading (review/work/l1_*.jpg, l2_*.jpg)
L1 = [19,15,21,22,3,14,9,18]
L2 = [1,6,6,5,3,20,21,5,21,23]
std = {i+1:c for i,c in enumerate(string.ascii_uppercase)}
now = {i+1:c for i,c in enumerate('ABCDEFGHIJKLMNOPQRSTUVXYZ')}
for name,k in (('A=1 26 letters',std),('A=1 no W',now)):
    print(name, ''.join(k[n] for n in L1), ''.join(k[n] for n in L2))
print('distinct numbers', sorted(set(L1+L2)), 'count', len(L1+L2))
