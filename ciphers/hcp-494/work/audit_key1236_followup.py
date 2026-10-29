"""Record a bounded, manual image comparison and verify acquired sources.

The observations are human/model-entered readings, not OCR or an independent
decipherment. Gloss-based target meanings remain secondary comparisons.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
observations = [
    {'key_ids':[256,259,260,264], 'new_pages':[3,8,9,11,22],
     'finding':'Encoding/decoding copies of a shared word list, not independent candidate keys.',
     'samples':{'Allianz':['236','440'], '601':'le Pretendant', '576':'Bremen',
                '602':'Mr. Martine', '625':'Vestung'},
     'sample_sources':{'Allianz':'full/key1236-0009.jpg',
                       '601,576,602,625':'full/key1236-0022.jpg'},
     'comparison':'These do not agree with the annotation-assisted Denmark/France readings in HCP 494. The black target annotations are not assumed infallible. No matching expanded list is established.'},
    {'key_ids':[257], 'new_pages':[5],
     'finding':'Continuation/copy of the addition table: Dresden, Hanau, Muentzenberg, Warschau, der, die, das, dass, und.',
     'samples':{'Dresden':['1020','2000','2080'], 'und':['2240','2340']},
     'comparison':'Four-digit additions; does not supply the target three-digit nomenclator.'},
    {'key_ids':[258,265], 'new_pages':[7,23],
     'finding':'Two copies of a different numeric alphabet headed Chiffre pour M. le B. de M.',
     'samples':{'a':'10-15', 'h':'53-57', 'g':'47-52', 'k':'65-67'},
     'comparison':'This is not the 20/30/40/50/60=a alphabet used for the current target comparison. It supplies no doubled-letter or syllable sign clarification.'},
    {'key_ids':[261], 'new_pages':[13],
     'finding':'Four-digit dignities, places, persons and word additions; a note corrects entries in the large key.',
     'comparison':'Does not supply the missing target word list or a new rendering of the disputed graphic signs. No exhaustive transcription of this dense page is claimed.'},
    {'key_ids':[262], 'new_pages':[15],
     'finding':'Place list in a progression ending in 6, plus four-digit persons/people entries.',
     'samples':{'Hollande':'256','Holstein':'266','Hambourg':'176'},
     'comparison':'Holstein=266 conflicts with the auxiliary target 634 gloss; the list does not establish the target nomenclator.'},
    {'key_ids':[263], 'new_pages':[17],
     'finding':'Dense continuation of the German syllable/word table through M-Z, including much four-digit material.',
     'comparison':'Continues the already different scheme on page 16. No exact target table identified; this is a visual screening, not a full transcription or proof that no reusable entry exists.'},
]
jobs=json.loads((ROOT/'work/key1236-followup-downloads.json').read_text())
old=json.loads((ROOT/'work/source-sha256-2026-10-23-gloss.json').read_text())
preserved=all(hashlib.sha256((ROOT/'source'/name).read_bytes()).hexdigest()==sha
              for name,sha in old.items())
assert preserved
for job in jobs:
    body=(ROOT/'source'/job['source_file']).read_bytes()
    assert body[:2]==b'\xff\xd8'
    job['bytes']=len(body)
    job['sha256']=hashlib.sha256(body).hexdigest()
assert sorted(j['page'] for j in jobs)==[3,5,7,8,9,11,13,15,17,22,23]

result={
 'status':'No new accepted plaintext or recovered target key',
 'scope':'All image attachments represented by catalogue keys 256-265 are now acquired and visually screened across this and the preceding pass. This is not all archival pages of HStAM 4 d 1236.',
 'new_images':len(jobs), 'new_metadata_files':10,
 'metadata_provenance':'Public dbourdeau/cyphersolver GitHub files, fetched through the GitHub connector. No HC Portal data endpoint was queried.',
 'downloads':jobs, 'manual_observations':observations,
 'original_glyph_followup':{
    'initial_pair':'II versus 55 remains unresolved. The 1677 auxiliary numeric 55 has compact angular numeral heads, but a five-year separation and an unestablished same hand prevent treating it as decisive.',
    'BB':'No new original-sign evidence for PP=n; keep BB=z as preferred key output.',
    'final_pair':'Target resembles both the ff double-cross form and XX=u. No new secure connecting stroke was recovered; retain both branches.',
    'black_ink':'No stroke hidden by black annotations was reconstructed or inferred as observed.',
    'new_accepted_glyph_identifications':[]},
 'source_preservation':{'previous_sources_checked':len(old),'previous_sources_unchanged':preserved},
 'limitations':'Manual visual comparison with prior exposure to the published readings. Negative key screening is not decipherment, an exhaustive archive search, or an independent review.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
