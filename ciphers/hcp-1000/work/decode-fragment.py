"""Known public key; an opening fragment only, never a complete edition."""
from pathlib import Path
import json
p=Path(__file__).resolve().parent
key=json.loads((p/'public-key.json').read_text())
groups=(p/'opening-fragment.txt').read_text().split()
print(' '.join(''.join(key.get(n,'?') for n in group.split('/')) for group in groups))
