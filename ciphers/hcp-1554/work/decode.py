#!/usr/bin/env python3
"""Read-only audit and known-key decoding of manually transcribed HCP1554.
No OCR, network, mutation, or glyph-recognition claim. Unknown spans stay opaque.
"""
from pathlib import Path
import hashlib,json,re
from PIL import Image,ImageDraw
W=Path(__file__).resolve().parent
C=W.parent
R=C.parents[1]
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def load(name):return json.loads((W/name).read_text())
def main():
    records=load('record-sha256.json')
    for name,expected in records.items():assert digest(W/name)==expected, f'record changed: {name}'
    source=load('source-sha256.json')
    assert set(source)=={'address.jpg','metadata.md','picture.jpg'}
    guard=json.loads((R/'batches/easy-2026-10-28/cz235-237-next-source-sha256.json').read_text())
    for name,expected in source.items():
        assert digest(C/'source'/name)==expected, f'original changed: {name}'
        assert guard[f'ciphers/hcp-1554/source/{name}']==expected
    refs=load('reference-sha256.json')
    for name,expected in refs.items():assert digest(R/name)==expected, f'reference changed: {name}'
    key=load('key.json')
    family=json.loads((R/'ciphers/hcp-1520/work/key.json').read_text())
    assert key==dict(family,v='f')
    assert len(key)==len(set(key.values()))==23
    inv={plain:cipher for cipher,plain in key.items()}
    raw=(W/'transcription.txt').read_text()
    inventory=load('inventory.json'); rows=inventory['rows']; unknowns=load('uncertainties.json')
    assert raw.splitlines()==[row['transcription'] for row in rows]
    pattern=r'⟦U\d+⟧|\[9:40\]|.'
    plainrows=[]; flattened=[]; seen_unknown=[]; unit_index=0
    im=Image.open(C/'source/picture.jpg')
    marg=im.crop((84,81,219,573)).rotate(270,expand=True)
    for row in rows:
        text=row['transcription']; tokens=list(re.finditer(pattern,text)); saved=row['tokens']
        assert len(tokens)==len(saved)
        output=[]
        for match,item in zip(tokens,saved):
            value=match.group()
            assert item['row']==row['id'] and item['column']==match.start()+1
            if value in key:
                unit_index+=1
                assert item['type']=='glyph' and item['cipher']==value and item['plain']==key[value]
                assert item['glyph_index']==unit_index
                flattened.append(item);output.append(key[value])
            elif value.startswith('⟦'):
                ident=value[1:-1];assert item['type']=='unknown' and item['id']==ident and ident in unknowns
                assert unknowns[ident]['row']==row['id']
                seen_unknown.append(ident);output.append(value)
            elif value=='[9:40]':
                assert item['type']=='ordinary' and item['text']=='9:40';output.append(value)
            else:
                assert value in ' .,!?-' and item['type']=='separator' and item['text']==value
                output.append(value)
        expected=(marg if row['id'].startswith('L') else im).crop(tuple(row['box']))
        if 'ownership_polygon' in row:
            context=expected.resize((expected.width*3,expected.height*3),Image.Resampling.NEAREST)
            saved_context=Image.open(W/row['context_crop'])
            assert context.size==saved_context.size and context.tobytes()==saved_context.tobytes()
            mask=Image.new('L',expected.size,0);x0,y0,_,_=row['box']
            ImageDraw.Draw(mask).polygon([(x-x0,y-y0) for x,y in row['ownership_polygon']],fill=255)
            expected=Image.composite(expected,Image.new('RGB',expected.size,'white'),mask)
        if row.get('resampling')=='nearest':
            expected=expected.resize((expected.width*3,expected.height*3),Image.Resampling.NEAREST)
        else:expected=expected.resize((expected.width*3,expected.height*3))
        actual=Image.open(W/row['crop'])
        assert expected.size==actual.size and expected.tobytes()==actual.tobytes(), f'crop mismatch {row["id"]}'
        plainrows.append(''.join(output))
    panels=load('control-panels.json')
    assert panels['resampling']=='nearest neighbor'
    for group,parts in panels['groups'].items():
        panel=Image.open(W/f'control-{group}-rawNN.png')
        for i,item in enumerate(parts):
            b=item['glyph_box']; tile=im.crop(b)
            tile=tile.resize((tile.width*5,tile.height*5),Image.Resampling.NEAREST)
            actual=panel.crop((10,i*210+28,10+tile.width,i*210+28+tile.height))
            assert tile.tobytes()==actual.tobytes(), f'raw-NN glyph panel mismatch {group}/{i}'
            b=item['row_box']; tile=im.crop(b)
            tile=tile.resize((tile.width*2,tile.height*2),Image.Resampling.NEAREST)
            actual=panel.crop((180,i*210+48,180+tile.width,i*210+48+tile.height))
            assert tile.tobytes()==actual.tobytes(), f'raw-NN row panel mismatch {group}/{i}'
    resolved=load('resolved-controls.json')
    assert {i:v['cipher'] for i,v in resolved.items()}=={'U1':'s','U2':'q','U3':'q','U5':'g'}
    assert flattened==inventory['glyphs']
    assert set(seen_unknown)==set(unknowns) and len(seen_unknown)==len(unknowns)==2
    literal='\n'.join(plainrows)+'\n'
    assert literal==(W/'literal.txt').read_text(), 'saved literal differs'
    # Whole plaintext inverse uses the COMPLETE fixed inverse, with greedy CH;
    # it does not invert each token by consulting its saved original cipher unit.
    back=[];pos=0
    while pos<len(literal):
        marker=re.match(r'⟦U\d+⟧|\[9:40\]',literal[pos:])
        if marker:
            back.append(marker.group());pos+=len(marker.group());continue
        if literal[pos:pos+2]=='ch':back.append(inv['ch']);pos+=2;continue
        char=literal[pos];back.append(inv.get(char,char));pos+=1
    assert ''.join(back)==raw, 'whole-key inverse mismatch'
    letters=sum(len(g['plain']) for g in flattened)
    print(f'Original hashes: {len(source)} OK; reference hashes: {len(refs)} OK; record hashes: {len(records)} OK')
    print('Manual rows: 16 main + 2 insertions + 3 rotated marginal = 21; image crops/marginal masks/raw contexts/row-token positions OK')
    print(f'Known glyph units: {unit_index}; known plaintext letters: {letters}; CH units: {sum(g["cipher"]=="H" for g in flattened)}; used key classes: {len(set(g["cipher"] for g in flattened))}/23')
    print('Resolved by same-card shape panels: U1=s/C, U2=q/Z, U3=q/Z, U5=g/K; raw-NN glyph/row pixels OK. Unknowns: 2 overink spans of unasserted length; total unit count unknown')
    print('Saved literal and actual whole-fixed-key inverse with greedy CH: OK')
    print('These checks audit records and mapping, not photographic glyph truth.\n')
    for row,plain in zip(rows,plainrows):print(f'{row["id"]}: {plain}')
    print('\nOrdinary writing: date 22/V.1903; address: Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.')
if __name__=='__main__':main()
