"""Reproduce inventory/hash checks; visual readings are explicit manual observations."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
WORK = HERE.parent
CIPHER = WORK.parent
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()

# No OCR or automatic plaintext inference. These readings are deliberately bounded.
EARLY = [
    {'page': 2, 'kind': 'archival cover', 'reading': 'Georg Raumer 1665/75; Friedrich Gottfried v. Raumer 1673/86; Johann Georg v. Raumer 1690/3; Ephraim Jonathan Raumer 1667; overall 1665/92', 'confidence': 'The two catalogue discrepancies 1673/86 and 1667 are clear in MAX. Cover is a later archival description, not a contemporary letter.'},
    {'page': 9, 'kind': 'German letter body', 'reading': None, 'confidence': 'No date or signature established on selected spread.'},
    {'page': 12, 'kind': 'closing on left/new letter on right', 'reading': 'Dessau [day/month unresolved] 1665; Georg Raumer', 'year': 1665, 'confidence': 'Year and signature read from original closing; day/month not stabilized.'},
    {'page': 13, 'kind': 'closing', 'reading': 'Dessau am 21. Apr. 1675; Georg Raumer', 'year': 1675, 'confidence': 'Date and surname reasonably legible; no full body transcription.'},
    {'page': 15, 'kind': 'French opening, continues through 17 left', 'reading': 'Berlin le [19?] Juin 1673', 'year': 1673, 'target_window_positive': True, 'confidence': 'Place/year clear enough for screening; day uncertain. No enclosure B label identified.'},
    {'page': 16, 'kind': 'French continuation', 'reading': None, 'confidence': 'Continuous body, no independent date established.'},
    {'page': 17, 'kind': 'French closing left; revised German draft begins right', 'reading': 'French subscription probable Raumer; German salutation to a Freiherr / Herr Baron', 'confidence': 'Do not identify the German addressee or writer. Many explicit revisions; separate texts on the spread.'},
    {'page': 18, 'kind': 'German draft closing left; next letter opening right', 'reading': '[place unresolved, possibly Regenspurg] den [stacked day pair unresolved] Januarij(?) 1673', 'year': 1673, 'target_window_positive': True, 'confidence': 'MAX establishes 1673; month tentative. Earlier Nov interpretation withdrawn. A formula/abbreviated subscription is not a secure Raumer signature. Date applies to left text only.'},
    {'page': 19, 'kind': 'German closing', 'reading': 'Dessau am [19/29?] Martij 1685; Friedrich [given name unresolved] Raumer', 'year': 1685, 'confidence': 'Year clear; day pair and full given name not asserted.'},
    {'page': 20, 'kind': 'German opening', 'reading': None, 'confidence': 'No date/signature established on selected spread.'},
    {'page': 22, 'kind': 'German closing', 'reading': 'Dessau am 29. Julij 1686; Raumer', 'year': 1686, 'confidence': 'Year/place reasonably legible; initials not expanded.'},
    {'page': 24, 'kind': 'French opening', 'reading': None, 'confidence': 'No date/signature established on selected spread.'},
    {'page': 28, 'kind': 'French closing left/new opening right', 'reading': 'Raumer subscription on left', 'confidence': 'No date established; initials not expanded.'},
    {'page': 32, 'kind': 'French closing left/new opening right', 'reading': 'Viene le 24 Juillet 1690; Raumer', 'year': 1690, 'confidence': 'Date taken from original ink at left, not the pencilled 10.90 on right.'},
    {'page': 36, 'kind': 'French closing left/new German opening right', 'reading': 'Buda le [18/28?] Octobr. 1690; Raumer', 'year': 1690, 'confidence': 'Earlier 15/25 day reading withdrawn on crop review; day pair remains tentative. Year legible.'},
    {'page': 41, 'kind': 'German closing right', 'reading': 'Wien [day unresolved] Januarii 1691; Raumer', 'year': 1691, 'confidence': 'Year reasonably legible; day not stabilized.'},
    {'page': 51, 'kind': 'French closing right', 'reading': 'Viene le [13/23?] Avril 169[1?]; Raumer', 'year': None, 'confidence': 'Faint date: last year digit not secure; not used as positive target-window match.'},
]

def main():
    groups = {}
    for name in ['thumbs', 'default', 'max']:
        rows = json.loads((HERE / f'{name}-manifest.json').read_text())
        good = [r for r in rows if 'error' not in r]
        for r in good:
            assert sha(WORK / r['path']) == r['sha256'], (name, r['page'])
        groups[name] = {'verified_files': len(good), 'pages': [r['page'] for r in good],
                        'errors': [r for r in rows if 'error' in r]}
    source_manifest = json.loads((WORK / 'source-sha256-2026-10-23-key1236.json').read_text())
    for name, digest in source_manifest.items():
        assert sha(CIPHER / 'source' / name) == digest, name
    defaults = {r['page']: r for r in json.loads((HERE / 'default-manifest.json').read_text()) if 'error' not in r}
    for r in EARLY:
        r['source'] = defaults[r['page']]['path']
        r['source_sha256'] = defaults[r['page']]['sha256']
        r['source_url'] = defaults[r['page']]['url']
    later = json.loads((HERE / 'later-date-triage.json').read_text())
    report = {
        'archive_reference': 'LASA Z 44, A 9a IIa Nr. 62',
        'catalogue_url': 'https://recherche.landesarchiv.sachsen-anhalt.de/Query/detail.aspx?ID=502883',
        'manifest_url': 'https://recherche.landesarchiv.sachsen-anhalt.de/xslt/index.aspx?xml=Z_44__A_9a_IIa_Nr_62-producer.xml',
        'manifest_sha256': sha(WORK / 'enclosure-context-2026-10-28/lasa-raumer-mets.xml'),
        'manifest_scan_count': 111,
        'layout_screen': 'All 107 available thumbnails manually inspected in contact sheets; four unavailable scans cannot be visually screened.',
        'default_scan_screen': '28 complete DEFAULT scans inspected, 17 by ending_alternative and 11 by helper raumer_dates; targeted date/signature crops available.',
        'max_scan_screen': 'Two MAX scans (2,18) inspected for cover and 1673 dating.',
        'groups': groups,
        'source_files_verified_unchanged': len(source_manifest),
        'early_records': EARLY,
        'later_records': later['records'],
        'pdf_gap_record': 'raumer-screen-2026-10-29/pdf-gap/manifest.json',
        'result': 'Two different texts dated 1673 identified (15–17 left; 17 right–18 left). No positive 1672 date or enclosure B identification; no new HCP494 key value or plaintext.',
        'limits': 'Layout/date/signature triage only, not exhaustive transcription or a negative name search. A 1673 document may discuss earlier events; this screen cannot exclude that. Family catalogue association does not prove that any selected writer is the secretary in HCP494. Thumbnails cannot exclude short encrypted insertions.',
    }
    (WORK / 'raumer-screen-2026-10-29.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'verified_groups': {k:v['verified_files'] for k,v in groups.items()},
                      'source_files_unchanged': len(source_manifest),
                      'manual_date_window_positive_pages': [15,18]}))

if __name__ == '__main__':
    main()
