"""Crops and provenance for original-brown page4 diplomatic inspection.

Never masks, reconstructs, enhances or fills annotated strokes.
"""
from pathlib import Path
import hashlib
import json
from PIL import Image

WORK = Path(__file__).resolve().parent
SOURCE = WORK.parent / 'source/full/0004.jpg'
OUT = WORK / 'page4-diplomatic-2026-10-29'
BOXES = {
    'band1': (510, 585, 2430, 1335),
    'band2': (510, 1295, 2430, 2035),
    'band3': (510, 1990, 2430, 2685),
    'band4': (510, 2640, 2430, 3340),
    'signature': (1290, 3520, 2310, 3790),
    'dateline': (55, 3480, 610, 3800),
    'top-start': (510, 590, 1300, 815),
    'top-576-clause': (1300, 690, 2420, 890),
    '625-word': (1330, 885, 2420, 1070),
    'etlicher-word': (760, 1000, 2420, 1180),
    'schilling-line': (510, 1500, 2420, 1720),
    'execution-line': (510, 1780, 2420, 1995),
    'latin': (500, 2260, 2410, 2430),
    'litb-clause': (510, 2630, 2410, 2805),
    'desiderio-line': (510, 2740, 2410, 2915),
    'einge-word': (510, 1260, 1250, 1435),
    'adell-word': (1730, 2130, 2410, 2260),
}

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    im = Image.open(SOURCE)
    records=[]
    for name, box in BOXES.items():
        path = OUT / f'{name}.png'
        im.crop(box).save(path)
        records.append({'id': name, 'box': box, 'path': str(path.relative_to(WORK)),
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    result = {'source': 'source/full/0004.jpg',
              'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'source_dimensions': im.size, 'method': 'direct original-pixel crops, no rescaling or enhancement',
              'crops': records}
    (OUT / 'crop-manifest.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'crops': len(records), 'source_sha256': result['source_sha256']}))
