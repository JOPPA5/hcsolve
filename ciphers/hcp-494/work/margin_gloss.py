"""Apply the contemporary margin gloss beside passage 1 (Claude contribution, 23 Oct 2026).

The glosser's margin beside passage 1 (source/full/0004.jpg, about x 110-640,
y 1950-2180) reads, in three lines: `disgustirt` / `undertanin` / `Holstein`.
The fifth letter of `erta?in` was previously left as r or z. It is read here as n:
- the glosser's r (disgustirt, ertanin) is a tall v-shape with a left hook; this letter is a low two-stroke form;
- a z would descend below the line, as the key's z does; nothing descends here;
- `undertanin` gives `Undertan in Holstein`, parallel to the clear `so wohl als in <601 Dennemarck>`.
The ciphertext glyph itself is still BB (= z in key 255; n would be PP). The gloss is
treated like the `Gott` gloss for 55: contemporary evidence for the intended letter,
not proof of the 1672 key cell. Crops: work/margin-gloss.jpg, work/margin-gloss-erta-n.jpg
(made with macOS `sips`; no Pillow needed).
"""
from pathlib import Path
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
baseline = json.loads(subprocess.check_output(
    [sys.executable, str(ROOT / 'work/audit.py')], text=True))
row = (ROOT / 'source/bourdeau/ct.txt').read_text().splitlines()
row = [x.split() for x in row if x.strip() and not x.startswith('#')][0]

literal = baseline['literal'][0]
assert literal.startswith('disgustirtundertazin'), literal
assert row[16] == 'BB', row
gloss_reading = literal.replace('undertazin', 'undertanin', 1)

CROPS = {  # name: (height, width, y, x) on source/full/0004.jpg, unretouched
    'margin-gloss.jpg': (500, 900, 1820, 0),
    'margin-gloss-erta-n.jpg': (110, 230, 2040, 300),
    'margin-cipher-bb.jpg': (220, 700, 2020, 1750),
}
if shutil.which('sips'):
    for name, (h, w, y, x) in CROPS.items():
        subprocess.run(['sips', '-c', str(h), str(w), '--cropOffset', str(y), str(x),
                        str(ROOT / 'source/full/0004.jpg'), '--out', str(ROOT / 'work' / name)],
                       check=True, capture_output=True)

result = {
    'status': 'PARTIAL — passage 1 gap read from contemporary margin gloss; ciphertext glyph unchanged',
    'token': {'index': 16, 'glyph': 'BB', 'key255_value': 'z', 'gloss_value': 'n', 'key255_n_sign': 'PP'},
    'margin_gloss': ['disgustirt', 'undertanin', 'Holstein'],
    'literal_passage1': literal,
    'passage1_with_gloss_correction': gloss_reading,
    'reading': 'Totaliter disgustirt [die] Undertan[en] in <634 Holstein>, nun so wohl als in <601 Dennemarck> Adell, Bürger und Bauren ... in plainten combiniret',
    'translation': 'The subjects in Holstein are totally disgruntled; now, as also in Denmark, nobility, burghers and peasants ... have combined in complaints.',
    'notes': [
        'Undertan is a shortened plural; the 1647-1669 DTA sample has unterthanen 26x, underthanen 5x, plural unterthan 0x.',
        'The verb (sind) is not in the cipher; clear words after 601 follow Bourdeau, not re-read here.',
        'Mechanism (encipherer slip BB for PP, or a different 1672 cell) is not determined.'],
    'crops': list(CROPS),
    'reviewed': False,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
