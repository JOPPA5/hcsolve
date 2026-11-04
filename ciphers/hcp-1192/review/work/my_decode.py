# Independent reviewer decode: my own sign reading (writer's orientation) from review crops.
key = {'|':'a','-':'b','/':'d','‖':'e','\\\\':'g','//':'h','+':'i','*':'l','T':'m','I':'n',
       'Φ':'o','Rr':'r','Ss':'s','♀':'t','⊕':'u','⊗':'v','✲':'w','~':'y'}
lines = [
 "// ‖ * * Φ _ ✲ | Rr Rr ‖ I , _ // Φ ✲",
 "| Rr ‖ _ ~ Φ ⊕ ? _ \\\\ Φ + I \\\\ _ ♀ Φ",
 "⊗ Φ ♀ ‖ _ ♀ Φ / | ~ ?",
 "// Φ ✲ _ + Ss _ | I I | _ \\\\ ‖ Rr ♀ Rr ⊕ / ‖ ?",
 "\\\\ + ⊗ ‖ _ T ~ _ * Φ ⊗ ‖ _ ♀ Φ _ T | T T | .",
 "- ‖ _ | _ \\\\ Φ Φ / _ - Φ ~ .",
 "I Φ ⊗ _ 6 , ' 0 6 .",
 "Ss + Ss .",
]
from collections import Counter
cnt = Counter(); out=[]
for l in lines:
    s=''
    for t in l.split():
        if t=='_': s+=' '
        elif t in key: s+=key[t]; cnt[t]+=1
        else: s+=t
    out.append(s); print(s)
print('signs:', sum(cnt.values()), 'distinct:', len(cnt), 'unused:', set(key)-set(cnt))
