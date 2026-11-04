# Independent decode (reviewer). Words re-read from enlarged crops; sign names:
# T=cent-sign, D=pi, W=division, Y=-o-, J=y-dot, B=q-shaped 9, K9=round 9, U=( or C-shape
import collections
key={'T':'t','X':'a','K9':'k','8':'e','7':'m','B':'b','6':'c','5':'o','P':'i','a':'r','#':'?',
'/':'n','2':'g','3':'h','D':'d','d':'l','Y':'y','U':'u',')':'s','n':'p','o':'f','W':'w',':':'v','J':'j'}
words="""T X K9 8|7 8|B X 6 K9|B X 6 K9|B X 6 K9|T 5|B P a # P / 2 3 X 7|D 8 d P X|P )|T 3 8 T|T a P n|Y 5 U|P / T 8 / D|T X K9 P / 2|X|3 5 / 8 Y 7 5 5 /|P o|/ 5 T|n d 8 X ) 8|D 5 / T|2 5|) 5 5 /|T 3 X T|d 8 T T 8 a|W X )|X|2 5 D|) 8 / D|T 5|7 8|W P d d|Y 5 )|B 8|) 5|K9 P / D|X )|T 5|W a P T 8|X / 5 T 3 8 a|n d 8 X ) 8|Y 5 U a )|T a U d Y|W 8 ?
T 3 P )|P )|X|o P / 8|7 5 5 /|d P 2 3 T|/ P 2 3 T|X / D|P D|2 P : 8|T 3 8|W 5 a d D|J U ) T|T 5|B 8|W X d K9 P / 2|W P T 3|Y 5 U|W 8 ?"""
cnt=collections.Counter()
for side in words.split("\n"):
    out=[]
    for w in side.split("|"):
        s=w.split(); cnt.update(s)
        out.append("".join(key.get(c,'?') for c in s))
    print(" ".join(out))
print(len(cnt),"distinct signs;",sum(cnt.values()),"tokens")
