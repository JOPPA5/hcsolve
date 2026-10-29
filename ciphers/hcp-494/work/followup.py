"""Reproduce the revised partial claim, keeping prior text and assumptions separate.

This is not an OCR or an automatic solution. Visual corrections are encoded
explicitly below and linked to saved crops of the immutable manuscript.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
baseline = json.loads(subprocess.check_output(
    [sys.executable, str(ROOT / 'work/audit.py')], text=True))
rows = []
for line in (ROOT / 'source/bourdeau/codes.txt').read_text().splitlines():
    if line.startswith(('f2r', 'f3r', 'f4r')):
        page, code, rest = line.split(maxsplit=2)
        rows.append({'page': page, 'borrowed_code': code,
                     'preferred_code': code, 'borrowed_annotation': rest})

# Occurrences are 1-based within Bourdeau's 26-code list.
revisions = {
    21: {'preferred_code': '427', 'preferred_gloss': 'Herzog',
         'basis': 'Middle digit has the curved 2 form, unlike both angular 4s in occurrence 24.',
         'confidence': 'preferred visual transcription; not independently reviewed'},
    24: {'preferred_gloss': None,
         'basis': '447 is not the preceding Herzog code (preferred 427); crossed Haus Braunschweig annotation is not a secure value.',
         'confidence': 'unresolved'},
    25: {'preferred_gloss': 'Kayser',
         'basis': 'Uncancelled manuscript gloss above 602; withdraw prior inferred Braunschweig.',
         'confidence': 'gloss reading, not independently recovered codebook value'},
}
for i, row in enumerate(rows, 1):
    row['occurrence'] = i
    if i in revisions:
        row['revision'] = revisions[i]
        row['preferred_code'] = revisions[i].get('preferred_code', row['preferred_code'])

old_hashes = json.loads((ROOT / 'work/source-sha256.json').read_text())
preserved = all(hashlib.sha256((ROOT / 'source' / p).read_bytes()).hexdigest() == h
                for p, h in old_hashes.items())
result = {
    'status': 'PARTIAL — new archival evidence and transcription corrections, no solved gap',
    'baseline_sources_preserved': preserved,
    'literal_letter_passages': baseline['literal'],
    'interpreted_letter_passages_with_disclosed_assumptions': baseline['borrowed_reading_with_disclosed_assumptions'],
    'gap': {'tokens': baseline['gap_tokens'], 'literal': 'ertaz', 'accepted_reconstruction': None},
    'correspondents': {
        'sender': 'Secretary Linker/Lincker (given name not established)',
        'recipient': 'Chancellor Vultejus (Vulteium on docket; given name not established)',
        'evidence': ['source/arcinsys/metadata.md', 'source/arcinsys/0001.jpg', 'source/arcinsys/0005.jpg'],
        'qualification': 'Catalogue attribution plus direct dorsal docket; not cipher-derived.'},
    'nomenclator_occurrences': rows,
    'revised_alliance_fragment': 'Der selbige <427 Herzog> <641 Plön> war auch zu Hamburg ... eine estroite <303 alliance> zwischen <447 unresolved> <602 Kayser: gloss> und <834 Rex Daniae: gloss> unter Handen ...',
    'revised_alliance_translation': 'The same Duke of Plön was also in Hamburg ... has a close alliance under negotiation between [447 unresolved], [602 Emperor, per gloss] and the King of Denmark ...',
    'alliance_crops': ['work/alliance-codes.png', 'work/427-vs-447.png'],
    'reviewed': False,
}
if not preserved:
    raise SystemExit('An original source hash changed; investigate before proceeding.')
if len(rows) != 26:
    raise SystemExit('Unexpected source-code list length; inspect the source.')
print(json.dumps(result, ensure_ascii=False, indent=2))
