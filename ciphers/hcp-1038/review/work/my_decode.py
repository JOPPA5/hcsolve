# Independent reviewer decoder for hcp-1038 (Claude Opus 5.5, review round 1).
# Transcription read by the reviewer from review/work/all.png, bottom.png, plain.png (rotated hi-res crops).
# Signs separated by spaces, no word breaks (as on the card).
K = {'0':'o','1..':'i','1.':'a','1*':'a',"1'":'á','1:':'e','^1':'ü','1,':'b','2':'l','2.':'é','2,':'cs',
     '3':'d','3,':'r','3.':'v','4,':'g','4.':'gy','5':'h','5,':'l','6':'j','6,':'n','6.':'ny','7':'k',
     '7,':'s','7.':'sz','8':'m','8,':'t','9':'p','9,':'z'}
T = """2. 3 1: 7, 6 0 2 1.. 7 1* 8
5 1. 5, 5, 0 8, 8, 1. 8 6, 1. 4. 0 6, 7 1.. 7 1. 9 0 8, 8, 8 1.. 1. 8, 8,
1* 8 1.. 4, 1* 9, 1' 6, 6, 1. 4. 0 6, 7, 1. 6 6, 1* 5, 0 8 3 1: 2. 6, 1: 8
1.. 7, 4, 0 6, 3 0 5, 8, 1. 8 5 0 4. 2. 3 1: 7, 1. 9 6 1. 7 1: 9,
2. 1, 1: 7 1: 3, ^1 5, 6, 1: 7 1. 5, 1. 9 0 7
7, 0 7 7. 0 3, 2, 0 7 0 5, 0 8
7, 1. 6. 1..
3. 1* 3, 0 7 3. 1* 5 1* 7. 8,"""
n=0; s=set()
for line in T.splitlines():
    t=line.split(); n+=len(t); s|=set(t)
    print(''.join(K[x] for x in t))
print(n,'signs',len(s),'distinct; unmapped:',[x for x in s if x not in K])
