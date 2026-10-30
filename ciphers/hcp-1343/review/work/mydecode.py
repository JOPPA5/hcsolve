# Independent decoder: own key table written from the SOLUTION key table prose, own tokenizer.
import re,collections,sys
key=dict(zip("O 3 C ) . F G H : J K L M V Q P X 7 2 T U > Y".split(),"abcdefghijklmnopqrstuvy".replace('v','n',0)))
key={'O':'a','3':'b','C':'c',')':'d','.':'e','F':'f','G':'g','H':'h',':':'i','J':'j','K':'k','L':'l','M':'m','V':'n','Q':'o','P':'p','X':'q','7':'r','2':'s','T':'t','U':'u','>':'v','Y':'y',"'":"'"}
freq=collections.Counter();words=[]
for l in open('work/transcription.txt'):
    if l.startswith('#') or not l.strip(): continue
    lab,b=l.split(None,1); out=[]
    for w in b.split(' / '):
        s=''
        for t in w.split():
            if t in('PO','PC'): s+='|';continue
            if '=' in t: 
                a,c=t.split('='); s+=c.rstrip('?').upper()
            else: s+=key[t]
            freq[t.split('=')[0]]+=1
        out.append(s)
    print(lab,' '.join(out)); words+=out
print(len(words),sum(freq.values()),freq.most_common())
