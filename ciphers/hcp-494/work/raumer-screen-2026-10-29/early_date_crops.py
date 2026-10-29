"""Unmodified-pixel crops for bounded Raumer file date/signature triage.

This is an inspection aid, not OCR or an automatic dating method.
"""
from pathlib import Path
import hashlib
import json
from PIL import Image

ROOT = Path(__file__).resolve().parent
# Coordinates are in the downloaded DEFAULT images.
CROPS = {
    2: (270, 150, 1330, 820),
    12: (245, 640, 750, 895),
    13: (350, 525, 750, 890),
    15: (970, 90, 1280, 200),
    17: (765, 100, 1265, 240),
    18: (255, 230, 740, 395),
    19: (750, 730, 1260, 890),
    22: (750, 700, 1260, 890),
    28: (250, 640, 750, 900),
    32: (350, 630, 760, 720),
    36: (250, 700, 750, 900),
    41: (740, 740, 1260, 895),
    51: (765, 640, 1170, 725),
}

if __name__ == '__main__':
    out = ROOT / 'early-date-crops'
    out.mkdir(exist_ok=True)
    records = []
    for page, box in CROPS.items():
        path = ROOT / 'default' / f'{page:03d}.jpg'
        data = path.read_bytes()
        im = Image.open(path).crop(box)
        im.resize((im.width * 2, im.height * 2), Image.Resampling.NEAREST).save(out / f'{page:03d}.png')
        records.append({'page': page, 'source': str(path.relative_to(ROOT)),
                        'source_sha256': hashlib.sha256(data).hexdigest(),
                        'crop': box, 'scale': 2,
                        'method': 'crop, nearest-neighbor integer scale; no enhancement'})
    for page, box in {2: (1450, 680, 2150, 990), 18: (445, 385, 1225, 640)}.items():
        path = ROOT / 'max' / f'{page:03d}.jpg'
        im = Image.open(path).crop(box)
        im.resize((im.width * 2, im.height * 2), Image.Resampling.NEAREST).save(out / f'{page:03d}-max.png')
        records.append({'page': page, 'source': str(path.relative_to(ROOT)),
                        'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'crop': box, 'scale': 2,
                        'method': 'crop, nearest-neighbor integer scale; no enhancement'})
    (out / 'crop-manifest.json').write_text(json.dumps(records, indent=2) + '\n')
    print(json.dumps({'crops': len(records)}))
