#!/usr/bin/env python3
"""Source-preserving crops and recorded manual diplomatic reading; not OCR."""
import hashlib
import json
from pathlib import Path
from PIL import Image

BASE=Path(__file__).resolve().parent
CIPHER=BASE.parents[2]
SOURCE=CIPHER/'source'/'full'/'0004.jpg'
REGIONS={
    'context':([440,2550,2400,3410],1),
    'prose1':([500,2790,2380,3010],1),
    'prose2':([470,2960,2380,3195],1),
    'prose3':([440,3120,2350,3380],1),
    'date':([60,3440,700,3800],1),
    'subscription':([1200,3440,2320,3800],1),
    'formula-detail':([1360,3050,2360,3190],2),
    'subscription-detail':([1250,3530,2200,3780],2),
    'date-detail':([80,3500,650,3790],2),
    'lastline-detail':([520,3210,2310,3340],2),
    'lit-b-clause':([510,2630,2370,2785],1),
    'desiderio-clause':([525,2740,2370,2885],1),
    'secretarius-clause':([520,2535,2370,2690],1),
}
READING={
    'brown_context_lines':[
        'Secretarius Raumer an mich begehrt[?] gibt die beylage',
        'Lit. B. und wird [Anredeabkürzung unaufgelöst] Cantzlar schon wißen wie weit Ihme',
        'hierinnen in seinem desiderio zu fügen. Der [selbige?]',
        '427. 641. war auch zu Hamburg, und hat selbiger',
        'einer estroite[?] 303. zwischen 447. 602. und 834;',
        'unter handlung, und wird selbige ehistes tages zum',
        'stande kommen. Hiermit[?] [Anredeabkürzung unaufgelöst] Cantzlar Göttl:',
        'Obhuth; mich aber dero beharrl: affection empfehle',
        'Meines insonders hochgeehrten Herrn Cantzlar[s?]',
    ],
    'dateline_lines':['Hamburg','den 4.[kleines Zeichen unaufgelöst] May','a° 1672'],
    'subscription_lines':['[schuldigster?] [gehorsamster?]','[trewster?] diener','[kurzes Monogramm, nicht zu einem Namen aufgelöst]'],
    'uncertainties':[
        'The adjective after Der before codes 427/641 is unresolved. selbige is a visual candidate, not an adopted reading.',
        'The address abbreviation before Cantzlar is left unexpanded in both occurrences.',
        'Spacing, punctuation and capitalization are tentative diplomatic conventions, not a facsimile transcription.',
        'The small mark after day 4 could include an ordinal/scribal abbreviation; this crop does not securely establish a separate day 14.',
        'The subscription first two adjectives and trewster are tentative; only diener and the presence of a short monogram are firm.',
        'The words under discussion are brown-ink readings. Black interlinear glosses have not been used to supply missing words or identify codes.',
        'Historical sender/date context was already known; this is an independent fresh reading, not a blinded experiment.',
    ],
}

def main():
    manifest=json.loads((CIPHER/'work'/'source-sha256-2026-10-23-key1236.json').read_text())
    checked=0
    for rel,expected in manifest.items():
        assert hashlib.sha256((CIPHER/'source'/rel).read_bytes()).hexdigest()==expected,rel
        checked+=1
    im=Image.open(SOURCE)
    crops=[]
    for name,(box,scale) in REGIONS.items():
        crop=im.crop(box)
        if scale!=1:
            crop=crop.resize((crop.width*scale,crop.height*scale),Image.Resampling.NEAREST)
        dst=BASE/f'{name}.png';crop.save(dst)
        crops.append({'name':name,'box_xyxy':box,'integer_nearest_neighbor_scale':scale,'file':dst.name,'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
    record={'source':'source/full/0004.jpg','source_dimensions':list(im.size),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'source_hashes_verified':checked,'method':'Manual reading from original-color image with native-pixel crops and integer nearest-neighbor duplicates only. No erasing, enhancement or generated pixels. Script verifies preservation/crop geometry, not paleographic truth.','reading':READING,'crops':crops}
    (BASE/'helper-ending.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'source_hashes_verified':checked,'crops':len(crops),'output':'helper-ending.json'}))

if __name__=='__main__':main()
