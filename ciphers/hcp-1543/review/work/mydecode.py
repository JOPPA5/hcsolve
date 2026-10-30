import json,sys
d=json.load(open(sys.argv[1]))
K={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','8':'L','b':'P','c':'S','d':'T','f':'V','g':'K','h':'R','m':'N','n':'M','p':'B','q':'Z','r':'H','s':'C','t':'D','y':'J','H':'CH','7':'J','ř':'CH'}
bad=0;n=0;cnt={}
for r in d['rows']:
    c=r['cipher'].replace('{U1}','#').replace('{U2}','@');o=''
    for ch in c:
        if ch in K:o+=K[ch];n+=1;cnt[ch]=cnt.get(ch,0)+1
        elif ch in ' ,.-':o+=ch
        elif ch=='#':o+='[UNK1]'
        elif ch=='@':o+='[UNK2]'
        else:o+='?';bad+=1
    ok=o==r['plaintext']
    print(r['id'],'OK' if ok else 'DIFF',o)
print('units',n,'unmapped',bad);print(sorted(cnt.items(),key=lambda x:-x[1]))
