"""Decode the source-bound manual reading; this script does not perform OCR."""
from pathlib import Path
import argparse,json,hashlib

BASE=Path(__file__).resolve().parents[1]
def load():
    key=json.loads((BASE/'work/key.json').read_text())
    source=BASE/key['source_image'];transcription=BASE/key['transcription']
    assert hashlib.sha256(source.read_bytes()).hexdigest()==key['source_sha256'], 'Source image changed'
    assert hashlib.sha256(transcription.read_bytes()).hexdigest()==key['transcription_sha256'], 'Manual reading changed'
    return key,transcription.read_text().strip()

def displacements(key,length):
    edges=key['adjacent_distances'];holes=key['holes_zero_based'];d=key['first_displacement']
    assert len(edges)==52 and sum(edges)==179 and len(set(holes))==key['period']==23
    out=[]
    for i in range(length):
        out.append(d%26);h=holes[i%23];nxt=holes[(i+1)%23];walk=0
        while h!=nxt:
            d+=edges[h];h=(h+1)%52;walk+=1;assert walk<=52
    return out

def decode(key,ciphertext):
    assert ciphertext[:5]==key['prefix_literal'] and len(ciphertext)==85
    P=key['input_positions'];O=key['output_positions'];assert sorted(P)==sorted(O)==list(range(26))
    inverse={slot:chr(97+i) for i,slot in enumerate(P)}
    return ''.join(inverse[(O[ord(c)-97]-d)%26] for c,d in zip(ciphertext[5:],displacements(key,80)))

def encode(key,plaintext):
    P=key['input_positions'];inverse={slot:chr(97+i) for i,slot in enumerate(key['output_positions'])}
    return key['prefix_literal']+''.join(inverse[(P[ord(c)-97]+d)%26] for c,d in zip(plaintext,displacements(key,len(plaintext))))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');group=ap.add_mutually_exclusive_group();group.add_argument('--alternate-35-n',action='store_true');group.add_argument('--alternate-35-m',action='store_true');args=ap.parse_args()
    key,c=load()
    if args.alternate_35_n:c=c[:34]+'n'+c[35:]
    if args.alternate_35_m:c=c[:34]+'m'+c[35:]
    p=decode(key,c);assert encode(key,p)==c
    result=dict(retained_prefix=c[:5],prefix_role='shared KIDAH indicator associated with the same initial state as373',indicator_encoding_deciphered=False,prefix_deciphered=False,body_plaintext_literal=p,body_letters=80,full85_source_reading_roundtrip_exact=True,padding_interpretation='last four coordinate19 values are X; supported by373sentence endings and terminalXX',canonical_unrecovered_labels=key['canonical_unrecovered_input_completion'],source_glyph35=c[34],source_glyph35_alternative=c[34]!='n')
    if args.json:print(json.dumps(result,indent=2))
    else:
        print('Shared starting-state indicator (encoding still open):',c[:5].upper())
        print('Literal decoded body:',p.upper())
        print('80/80 encrypted-body letters round trip exactly; XXXX agrees with the observed X preparation in373.')
