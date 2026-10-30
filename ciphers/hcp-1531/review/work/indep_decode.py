# Independent decoder: own key table (from hcp-1545 family key, typed here), reads transcription cipher strings only.
import json,sys
K={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','7':'J','8':'L','b':'P','c':'S','d':'T','f':'V','g':'K','h':'R','m':'N','n':'M','p':'B','q':'Z','r':'H','s':'C','t':'D','ř':'CH','□':'□'}
t=json.load(open(sys.argv[1]))
n=0;bad=[]
for r in t['rows']:
    out=''
    for ch in r['cipher']:
        if ch in K: out+=K[ch]; n+=1
        else: out+=ch
    print(r['id'],out, 'MATCH' if out==r['plaintext'] else 'DIFF')
print('units',n)
