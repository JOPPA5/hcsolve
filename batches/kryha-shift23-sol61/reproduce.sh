#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 scan.py
python3 control.py
python3 ransac.py
python3 make-crops.py
python3 diagnose.py
python3 collate.py
python3 - <<'PY'
from pathlib import Path
import json
b=Path('.')
for label in ('pixel-strong','pixel-strong-plus-moderate'):
 (b/f'{label}-pair.json').write_text(json.dumps([(b/f'{n}-{label}.txt').read_text().strip() for n in (350,351)])+'\n')
PY
python3 ransac.py pixel-strong-pair.json pixel-strong-ransac.json
python3 ransac.py pixel-strong-plus-moderate-pair.json pixel-strong-plus-moderate-ransac.json
python3 extent.py
python3 verify.py
