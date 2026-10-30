# Independent reviewer decoder for hcp-1449. Glyph labels are my own (Greek letter names),
# transcribed by the reviewer from review/work/*.png crops of source/address.jpg.
T = [
 "Eta alpha upsilon eta-bar | lat_j omicron sigma tau | sigma eta-bar eta-bar nu | mu gamma | omega phi phi",
 "lambda omega omega kappa | omega [blot:omicron?] tau | phi_loop omega rho | Eta iota mu",
 "tau omega mu omega rho rho omega lat_w | kappa iota nu delta | rho eta gamma alpha rho delta sigma",
]
K = {'Eta':'h','alpha':'a','upsilon':'v','eta-bar':'e','eta':'e','lat_j':'j','omicron':'u','sigma':'s',
     'tau':'t','nu':'n','mu':'m','gamma':'g','omega':'o','phi':'f','phi_loop':'f','lambda':'l','kappa':'k',
     'rho':'r','iota':'i','delta':'d','lat_w':'w','[blot:omicron?]':'u'}
from collections import Counter
c=Counter()
for line in T:
    words=[]
    for w in line.split('|'):
        gl=w.split(); c.update(gl); words.append(''.join(K[g] for g in gl))
    print(' '.join(words))
print(len(c),'distinct glyph labels;', sum(c.values()),'glyphs; all mapped:', all(g in K for g in c))
