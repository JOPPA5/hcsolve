"""One-shot marker inventory; never starts a watcher or reviewer."""
from pathlib import Path
from datetime import datetime, timezone
import re, json

root = Path(__file__).resolve().parents[1]
rows = []
for folder in sorted((root / 'ciphers').iterdir()):
    if not folder.is_dir():
        continue
    names = {p.name for p in folder.iterdir() if p.is_file()}
    markers = sorted(n for n in names if re.fullmatch(r'(DONE|REVIEWED)\d+|FINAL', n))
    if not markers:
        continue
    rounds = [int(re.search(r'\d+$', n).group()) for n in markers if n != 'FINAL']
    latest = max(rounds, default=0)
    state = 'final' if 'FINAL' in names else 'awaiting_review' if f'REVIEWED{latest}' not in names else 'needs_solver_response'
    row = dict(cipher=folder.name, markers=markers, round=latest, state=state)
    if state == 'awaiting_review':
        raw = (folder / f'DONE{latest}').read_text().split()[0]
        then = datetime.fromisoformat(raw.replace('Z', '+00:00'))
        row['pending_minutes'] = round((datetime.now(timezone.utc)-then).total_seconds()/60, 1)
    if state == 'needs_solver_response':
        row['review'] = str(folder / 'review' / f'REVIEW{latest}.md')
    rows.append(row)
print(json.dumps(rows, indent=2))
