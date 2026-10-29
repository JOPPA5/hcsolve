#!/usr/bin/env python3
"""Reproduce finite date-screen crops and input integrity checks, not OCR."""
import hashlib
import json
from pathlib import Path
from PIL import Image

BASE = Path(__file__).resolve().parent
ROWS = [
    {"page": 63, "folio_visible": "57/1", "date_reading": "Breslau le 12/22 Jul. 1691", "year": 1691, "place": "Breslau", "signature": "Raumer; initials unresolved", "uncertainty": "Day pair and abbreviated month are probable; year is legible.", "crop": [230,760,745,865]},
    {"page": 67, "folio_visible": "61", "date_reading": "Breslau le 30 Jul. 1691", "year": 1691, "place": "Breslau", "signature": "Raumer; initials unresolved", "uncertainty": "Month abbreviation read Jul.; no expansion from catalogue used.", "crop": [760,730,1265,885]},
    {"page": 74, "folio_visible": None, "date_reading": "[place unresolved] [stacked 30/20?] August 1691", "year": 1691, "place": None, "signature": "Probable Raumer; initials unresolved", "uncertainty": "Do not normalize the stacked day numbers: their order is uncertain. Place not established.", "crop": [745,755,1258,875]},
    {"page": 78, "folio_visible": "71 (70 crossed out)", "date_reading": "Dessau d. 17? Octobr. 1692", "year": 1692, "place": "Dessau", "signature": "Raumer; initials unresolved", "uncertainty": "Day 17 tentative. Right leaf explicitly headed P.S.; this is not an identified enclosure B.", "crop": [245,810,755,910]},
    {"page": 83, "folio_visible": "76", "date_reading": "Dessau d. 9 Junii 1693", "year": 1693, "place": "Dessau", "signature": "Probable Raumer; right edge of subscription is close to page edge", "uncertainty": "No initials expanded.", "crop": [755,800,1315,925]},
    {"page": 87, "folio_visible": "80", "date_reading": "Left: 20 May 1693. Right: 19 Feb. 1692?", "year": [1693,1692], "place": None, "signature": "No full signature established; headings identify Raumer as addressee", "uncertainty": "Two separate texts. Right final year digit read 2 tentatively. No place securely established.", "crop": [285,580,1280,895]},
    {"page": 93, "folio_visible": None, "date_reading": "Dessaviae d. 7 Junij 1693", "year": 1693, "place": "Dessaviae (Dessau)", "signature": "Raumer; elaborate preceding initials unresolved", "uncertainty": "Month read Junij; spelling not normalized in diplomatic reading.", "crop": [265,645,755,780]},
    {"page": 98, "folio_visible": "90", "date_reading": "Left: Dessau d. 27 May 1693. Right: [stacked 29/19?] Jun. 1693?", "year": [1693,1693], "place": "Dessau on left; no place established on right", "signature": "Left signed Raumer; initials unresolved", "uncertainty": "Two separate texts. Right small date is tentative: stacked day pair and final year digit are not firm.", "crop": [195,700,1250,885]},
    {"page": 103, "folio_visible": "95 on right insert", "date_reading": "Dessau d. 5 [month unresolved] 1693", "year": 1693, "place": "Dessau", "signature": "Raumer; initials unresolved", "uncertainty": "Month abbreviation could be misread; deliberately left unresolved. French right insert has no date established in this screen.", "crop": [180,795,755,905]},
    {"page": 107, "folio_visible": None, "date_reading": "1676? in heading", "year": 1676, "place": None, "signature": "No signature established in visible page", "uncertainty": "Heading year is probably 1676; not a complete dateline. No month or day established.", "crop": [790,220,1165,345]},
    {"page": 109, "folio_visible": "100", "date_reading": "Heidelbergae 1667. D. 14? Octob.", "year": 1667, "place": "Heidelbergae (Heidelberg)", "signature": "Ephraim Jonathan Raumer", "uncertainty": "Day read 14 tentatively; year 1667 and place are legible.", "crop": [770,785,1265,890]},
]

def main():
    manifest = {row['page']: row for row in json.loads((BASE/'default-manifest.json').read_text()) if 'sha256' in row}
    out = BASE/'later-date-crops'
    out.mkdir(exist_ok=True)
    records=[]
    for row in ROWS:
        src=BASE/'default'/f"{row['page']:03}.jpg"
        digest=hashlib.sha256(src.read_bytes()).hexdigest()
        assert digest == manifest[row['page']]['sha256'], src
        im=Image.open(src).crop(row['crop'])
        dest=out/f"{row['page']:03}.png"
        im.resize((im.width*2,im.height*2),Image.Resampling.NEAREST).save(dest)
        records.append({**row, 'source': str(src.relative_to(BASE)), 'source_sha256': digest, 'source_url': manifest[row['page']]['url'], 'crop_file': str(dest.relative_to(BASE)), 'target_date_positive': False, 'target_names_or_enclosure_B_positive': False})
    result={'task': 'Finite original-scan date/place/signature triage', 'archive_reference': 'LASA Z 44 A 9a IIa Nr. 62', 'checked_pages': len(records), 'method': 'Manual inspection of 11 complete default-resolution scans, followed by enlarged unmodified-pixel date/subscription crops. Stored readings are human-style visual assessments, not computed OCR.', 'limits': 'No exhaustive transcription or negative name search. No positive date in 1669–1673 and no positive Hamburg/Lincker/Vultejus/enclosure B identification in inspected material. This does not establish their absence elsewhere in the file, unread text, or uninspected pages.', 'input_hashes_verified': len(records), 'records': records}
    (BASE/'later-date-triage.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checked_pages':len(records),'input_hashes_verified':len(records),'target_date_positives':0}))

if __name__=='__main__':
    main()
