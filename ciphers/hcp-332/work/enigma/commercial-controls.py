from pathlib import Path
import sys,subprocess,json,random
p=Path(__file__).resolve().parent
sys.path.insert(0,str(p/'vendor/enigma-cipher-machine-main'))
from enigma.machine import Machine
from enigma.rotor import Rotor
from enigma.plugboard import Plugboard
wires=['LPGSZMHAEOQKVXRFYBUTNICJDW','SLVGBTFXJQOHEWIRZYAMKPCNDU','CJGDPSHKTURAWZXFMYNQOBVLIE'];notches='YEN'
def other(order,rings,win,ref,text,direction=0):
 etw='QWERTZUIOASDFGHJKPYXCVBNML'
 if direction:etw=''.join(chr(65+etw.index(chr(65+i))) for i in range(26))
 rotors=[Rotor('ETW',etw,'',rotate=False)]
 for i in [2,1,0]:
  r=int(order[i])-1;rotors.append(Rotor('wheel'+str(i),wires[r],notches[r],position=win[i],ringstellung=rings[i]))
 rotors.append(Rotor('UKW','IMETCGFRAYSQBZXWLHKDVUPOJN','',reflector=True,position=ref))
 return Machine('commercialK',rotors,Plugboard('')).encode(text,split=0)
def ours(order,rings,win,ref,text,direction=0):return subprocess.check_output([str(p/'commercial'),'crypt',order,rings,win,ref,text,str(direction)],text=True).strip()
rng=random.Random(61033217);checks=[]
for i in range(100):
 order=''.join(rng.sample('123',3));rings=''.join(rng.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ',k=3));win=''.join(rng.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ',k=3));ref=rng.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ');direction=i%2;text=''.join(rng.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ',k=100))
 a=ours(order,rings,win,ref,text,direction);b=other(order,rings,win,ref,text,direction)
 assert a==b,(i,order,rings,win,ref,direction,a,b)
 assert ours(order,rings,win,ref,a,direction)==text.lower()
 assert all(x.lower()!=y for x,y in zip(text,a))
 checks.append({'order':order,'rings':rings,'window':win,'reflector_position':ref,'entry_direction':direction,'exact':True})
base=json.loads((p/'controls.json').read_text())['heldout_controls'];controls=[]
for i,c in enumerate(base):
 order=['312','231'][i];rings=['FPO','CKV'][i];ref=['M','X'][i];text=c['plain'];direction=0
 ct=other(order,rings,'TRC',ref,text,direction);assert ours(order,rings,'TRC',ref,ct,direction)==text
 name='commercial-'+c['name'];(p/(name+'-cipher.txt')).write_text(ct+'\n')
 controls.append({'name':name,'plain':text,'cipher':ct,'order':order,'rings':rings,'reflector_position':ref,'entry_direction':direction,'generator':'untouched raymas implementation with uniquely named correctly specified rotors; not its incomplete commercial test','reencryption_exact':True})
(p/'commercial-controls.json').write_text(json.dumps({'random_cross_implementation_checks':checks,'heldout_controls':controls,'permutations_and_reflector_involution_asserted_in_cpp':True},indent=2)+'\n')
print(json.dumps(controls,indent=2))
