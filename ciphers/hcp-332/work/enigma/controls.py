from pathlib import Path
import sys,subprocess,json,random,hashlib
p=Path(__file__).resolve().parent
sys.path.insert(0,str(p/'vendor/enigma-master'))
from enigma.machine import EnigmaMachine
from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.rotors.data import ROTORS
exe=p/'search'
def ours(order,rings,win,ref,text,plugs=''):
 return subprocess.check_output([str(exe),'crypt',order,rings,win,ref,text,plugs],text=True).strip()
def other(order,rings,win,ref,text,plugs=''):
 names=['I','II','III','IV','V']
 rotors=[Rotor(names[int(x)-1],ROTORS[names[int(x)-1]]['wiring'],ord(r)-65,ROTORS[names[int(x)-1]]['stepping']) for x,r in zip(order,rings)]
 wire={'A':'EJMZALYXVBWFCRQUONTSPIKHGD','B':'YRUHQSLDPXNGOKMIEBFZCWVJAT','C':'FVPJIAOYEDRZXWGCTKUQSBNMHL'}[ref]
 pb=Plugboard.from_key_sheet(' '.join(plugs[i:i+2] for i in range(0,len(plugs),2)))
 machine=EnigmaMachine(rotors,Rotor(ref,wire),pb);machine.set_display(win)
 return machine.process_text(text).lower()
assert ours('245','BUL','WXC','B','BLA','AVBSCGDLFUHZINKMOWRX')=='kch'
assert ours('245','BUL','BLA','B','THEXRUSSIANSXAREXCOMINGX','AVBSCGDLFUHZINKMOWRX')=='niblfmymllufwcascssnvhaz'
rng=random.Random(332610)
checks=[]
for i in range(100):
 order=''.join(rng.sample('12345',3));rings=''.join(rng.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ',k=3));win=''.join(rng.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ',k=3));ref=rng.choice('ABC');text=''.join(rng.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ',k=100))
 a=ours(order,rings,win,ref,text);b=other(order,rings,win,ref,text)
 assert a==b,(i,order,rings,win,ref)
 assert ours(order,rings,win,ref,a)==text.lower()
 assert all(x.lower()!=y for x,y in zip(text,a))
 checks.append({'order':order,'rings':rings,'window':win,'reflector':ref,'exact':True})
# Verify the documented double-step progression independently through official library.
m=EnigmaMachine.from_key_sheet(rotors='III II I',ring_settings='A A A',reflector='B');m.set_display('KDO');seq=['KDO']
for _ in range(6):m.key_press('A');seq.append(m.get_display())
assert seq==['KDO','KDP','KDQ','KER','LFS','LFT','LFU']
controls=[('sk40','vyslanectvoziadaodoslatnovuspravubezodkladu'[:40],'435','RGF','C'),('de40',(p.parents[3]/'batches/scoring-sol61/german/flat40-plain.txt').read_text().strip(),'251','KPX','B')]
saved=[]
for name,text,order,rings,ref in controls:
 assert len(text)==40
 ct=other(order,rings,'TRC',ref,text)
 assert ours(order,rings,'TRC',ref,ct)==text
 (p/(name+'-plain.txt')).write_text(text+'\n');(p/(name+'-cipher.txt')).write_text(ct+'\n')
 saved.append({'name':name,'plain':text,'cipher':ct,'order':order,'rings':rings,'window':'TRC','reflector':ref,'source':'first40 letters of earlier separately planted Slovak holdout; text previously exposed during scoring development, not model training' if name=='sk40' else 'German UD test-only entropy-matched holdout','generator':'unaltered primary Py-Enigma, independently checked by C++','reencryption_exact':True})
(p/'controls.json').write_text(json.dumps({'published_doc_vectors_exact':True,'random_cross_implementation_checks':checks,'double_step_sequence':seq,'heldout_controls':saved,'vendor_sha256':{str(x.relative_to(p)):hashlib.sha256(x.read_bytes()).hexdigest() for x in (p/'vendor').glob('*.py')}},indent=2)+'\n')
print(json.dumps(saved,indent=2))
