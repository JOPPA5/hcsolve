"""Assemble the qualified working transcription; check provenance, not paleography."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
WORK = HERE.parent
CIPHER = WORK.parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
FROZEN_SHA = 'b993e9b7c02ee0a61585f0fe1ff77745f3c9cbbffcfc2aa07d27a8c7cc0d7fd7'

# Revisions after comparison are explicit and do not overwrite the frozen first pass.
REVISIONS = {
    1: ('[Ba[h?]en; Wort unaufgelöst] schicket und ⟨601⟩ seinen gebührenden', 'Cross-page brown context supplied by root; name/place not established. Helper compares target initial with brownBürger and finds B closer than HamburgH; medial ascender resemblesh. Frozen Hagen semantic candidate withdrawn as preferred reading, not disproved.'),
    2: ('respect anthut. daß ⟨576⟩ mit ⟨768?⟩ ge-', 'Daniel gives768. Original is compatible with numeric group; first pass left it unclassified. No gloss meaning adopted.'),
    4: ('druß. ⟨625⟩ wird [vielleicht?] nach verflie-', 'Independent helper proposes vielleicht. Daniel has hierauff; original remains disputed. Earlier künftig/kürzlich guesses withdrawn.'),
    5: ('ßung etlicher Wochen Zu ⟨829?⟩ [gehen/stoßen?] und das', 'Wochen/verfließung supported from brown. Daniel has gehen; helper proposed stoßen. Verb not settled.'),
    8: ('[hangen/zogen?] werde. Was die Landtags', 'Original-first read hangen, Daniel has eingezogen. Neither is forced into the frozen original.'),
    11: ('schafft 12. [Geldeinheit, Thl.?] begehret [kein/beim?] Schilling, sind', 'Fresh helper crop supports initialk-like shape, but phrase/unit unresolved. Do not repair from fiscal semantics.'),
    13: ('protestando voneinander geschieden, und wolle', 'Independent helper reading supports wolle; unobserved terminaln not inserted.'),
    14: ('es ad rigorem Executionis ankommen laß[en?].', 'Helper independently confirms es/ankommen; Daniel normalizes lassen. Final abbreviation unresolved.'),
    17: ('104. ⟨634⟩ [nun?] sowol alß in ⟨601⟩ [Adell/edell?]', 'Daniel readsAdell; original initial is compatible, punctuation/enumeration not silently normalized.'),
}

def main():
    frozen = HERE / 'original-first-pass.md'
    assert sha(frozen) == FROZEN_SHA, 'Frozen first pass changed'
    first = []
    current = []
    for number, text in re.findall(r'^(\d{2})  (.+)$', frozen.read_text(), re.M):
        n = int(number)
        first.append({'line': n, 'text': text})
        current.append({'line': n, 'text': REVISIONS.get(n, (text, None))[0]})
    assert len(first) == 30
    source_manifest = json.loads((WORK / 'source-sha256-2026-10-23-key1236.json').read_text())
    for name, digest in source_manifest.items():
        assert sha(CIPHER / 'source' / name) == digest, name
    crop_manifest = json.loads((HERE / 'crop-manifest.json').read_text())
    for r in crop_manifest['crops']:
        assert sha(WORK / r['path']) == r['sha256']
    helper = json.loads((HERE / 'helper-ending/helper-ending.json').read_text())
    result = {
        'source': crop_manifest['source'],
        'source_sha256': crop_manifest['source_sha256'],
        'source_dimensions': crop_manifest['source_dimensions'],
        'source_files_verified_unchanged': len(source_manifest),
        'frozen_original_first_pass': str(frozen.relative_to(WORK)),
        'frozen_original_first_pass_sha256': FROZEN_SHA,
        'comparison_source': 'source/bourdeau/reading.txt',
        'comparison_source_sha256': sha(CIPHER / 'source/bourdeau/reading.txt'),
        'method': 'Manual original-brown reading; first pass frozen before reopening Daniel; explicit later comparison and independent helper. No enhancement or reconstruction. Not fully blind because prior cipher/identity hypotheses were known.',
        'first_pass_body_lines': first,
        'working_body_lines': current,
        'post_freeze_revisions': [{'line': k, 'text': v[0], 'reason': v[1]} for k,v in REVISIONS.items()],
        'dateline_lines': helper['reading']['dateline_lines'],
        'subscription_lines': helper['reading']['subscription_lines'],
        'code_token_sequence_working': ['601','576','768?','601','625','829?','651?','634','601','768','427','641','303','447','602','834'],
        'code_occurrences_in_working_sequence': 16,
        'letter_cipher_signs': 38,
        'cipher_notice': 'Counts are bookkeeping under the displayed token transcription, not proof of all glyph readings. BB/PP, II/55, the8-like glyph and final crossedpair remain unresolved; no code values are expanded.',
        'crops': crop_manifest['crops'],
        'helper_evidence': 'page4-diplomatic-2026-10-29/helper-ending/helper-ending.md',
        'helper_microread': 'page4-diplomatic-2026-10-29/helper-ending/microread.json',
        'no_new_cipher_plaintext_claim': True,
    }
    (WORK / 'page4-diplomatic-2026-10-29.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    body = '\n'.join(f"{r['line']:02}  {r['text']}" for r in current)
    (HERE / 'working-body.txt').write_text(body + '\n')
    print(json.dumps({'body_lines': len(current), 'source_files_unchanged': len(source_manifest),
                      'crops_verified': len(crop_manifest['crops']), 'frozen_first_pass_verified': True}))

if __name__ == '__main__':
    main()
