# Independent reviewer decode of hcp-974 from my own reading of review/work/msg_full.png
# Ciphertext words (digits = cipher; capitals = plain Latin letters), my own transcription.
CT = """7238 Z50T18D 30T
B2D25T28D G2
B2029T. 23W230
30T F10T G18Z
W2G. 23T29 F38-
D2T D29 19ZT
K23828 72H9.
W1029 30T G18Z
H26! 749G28- 0170-
T1G 81CH73T1G-"""
# key derived independently from cribs: keinen(K23828) -> 2=e,3=i,8=n; ist(30T) -> 0=s;
# zustand -> 5=u,1=a; der(D29) -> 9=r; hel(H26) -> 6=l; mehr(72H9) -> 7=m; morgen -> 4=o
KEY = {'2':'e','3':'i','8':'n','0':'s','5':'u','1':'a','9':'r','6':'l','7':'m','4':'o'}
n_cipher = n_plain = 0
for line in CT.splitlines():
    out=''
    for ch in line:
        if ch in KEY: out+=KEY[ch]; n_cipher+=1
        elif ch.isalpha(): out+=ch.lower(); n_plain+=1
        else: out+=ch
    print(out)
print('cipher signs', n_cipher, 'plain letters', n_plain, 'total', n_cipher+n_plain)
