from pathlib import Path
import random,json,subprocess,unicodedata
p=Path(__file__).parent;rng=random.Random(363)
text='Kontrolny text sluzi iba na overenie programu. Vyslanectvo oznamilo ministerstvu ze sprava bola prijata a vsetky dokumenty budu dorucene dalsim kurierom. Pracovnici porovnali povodny zapis s prijatym telegramom a zaznamenali rozdiely. Pri dalsom odoslani treba zachovat poradie pismen a presny pocet skupin. Tento priklad nema byt riesenim historickej sifry ani domnelym opisom skutocnych udalosti. Kontrolujeme len schopnost obnovit znamu transpoziciu.'
pt=''.join(c for c in unicodedata.normalize('NFD',(text+' Vysledok porovnavame s nezavisle ulozenym povodnym textom.').lower()) if 'a'<=c<='z')[:395]
assert len(pt)==395
cases={};controls={}
for w in [16,19,22]:
 key=list(range(w));rng.shuffle(key);s=''.join(pt[j::w] for j in key);name=f'control-{w}';cases[name]=s;controls[name]={'plaintext':pt,'keys':[key]}
s=pt;keys=[]
for w in [16,19,22]:
 key=list(range(w));rng.shuffle(key);keys.append(key);s=''.join(s[j::w] for j in key)
cases['control-triple']=s;controls['control-triple']={'plaintext':pt,'keys':keys}
p.joinpath('controls.json').write_text(json.dumps(controls,indent=2))
for name,s in cases.items():
 f=p/(name+'.txt');f.write_text(s);out=subprocess.check_output([str(p/'columnar'),str(p),str(f)],text=True);p.joinpath(name+'-results.txt').write_text(out);best=max(out.splitlines(),key=lambda l:float(l.split()[1]));print(name,'exact',any(l.split()[-1]==pt for l in out.splitlines()),best,flush=True)
