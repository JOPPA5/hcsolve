"""Current partial reading, with literal decoding and editorial input separate.

No OCR, automatic palaeography, or recovered 1672 word list is claimed.
Bourdeau supplied the original key match/most gloss readings; Claude supplied
the proposed n in the passage-1 margin gloss. This script records that proposal
without modifying the original ciphertext or making BB=n a global key fact.
"""
from pathlib import Path
import hashlib, json, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
rows = [s.split() for s in (ROOT/'source/bourdeau/ct.txt').read_text().splitlines()
        if s.strip() and not s.startswith('#')]
letters = 'abcdefghiklmnopqrstuwxyz'
bases = [20,22,24,26,28,21,23,25,27,29,70,72,74,76,78,71,73,75,77,79,120,122,124,126]
key = {str(base+10*r):letter for letter,base in zip(letters,bases) for r in range(5)}
key.update(dict(zip('CC DD EE FF GG HH II KK LL MM NN OO PP QQ RR SS TT UU WW XX YY ZZ AA BB'.split(), letters)))
key.update({str(n):'∅' for n in range(1,20)})
key.update({'[st]':'st','[tt]':'tt','[634]':'<Holstein: gloss>','[768]':'<Sueco: gloss>'})

# All positions are zero-based within their source row, including code tokens.
exceptions = {
 (0,16): ('n', 'provisionally preferred PP glyph reading; otherwise gloss-based restoration', 'Expanded controls favor PP provisionally: isolated Lit. B and B in Brunsvicense, Berlin and Berlino have a further lower right bow absent from the target, which resembles P in Proposition. Cipher FF/Foedus and LL/Lit. support clear-text capital comparison. Connected b/B variation remains contrary evidence; no repeated cipher PP or independent verification. If preserved BB is retained, n is still the Claude margin-based restoration. BB=z and PP=n remain unchanged. See expanded-bp-controls.json and glyph-first.json. The amm/all disagreement cautions against treating the annotator as ground truth.'),
 (1,1): ('g', 'provisionally preferred II glyph reading; otherwise gloss-based restoration', 'Expanded comparison with eight original numeral-5 controls, including initial 5 in 500/50, provisionally favors the two hooked strokes as II=g. Both comparison tables retain 55=h. Upper loops/crossbars are not secure, and German-script Ihr/Ihro is not an exact control. Numeric 55 remains live. See p2-original-controls.json. Bourdeau already proposed Gott.'),
 (1,11): ('ll', 'preferred glyph identification conflicting with gloss', 'Loop above stem and lower bar match key 255 ll; mm has the loop below the stem. The annotation above 20 [I] is amm, not all, as already recorded by Bourdeau. The preferred ll therefore disagrees with the annotation. The source placeholder [I] is not a letter I.'),
 (1,18): ('au', 'probable glyph identification with gloss', 'Loop/upper stroke are compatible with the au sign; the annotation reads au. Numeric 8 would be a null.'),
 (1,19): ('ff', 'language-driven conditional interpretation contrary to the current visual preference', 'Expanded comparison provisionally favors XX=u: separate crossed forms match passage 1 and the inverse key, whose XX also has looped upper arms. Qualification 2026-10-28: key255 ff may be two overlapping crossed components; wider spacing could remove their contact without deleting a separate connector. The st/tt controls do not directly test that mechanism. No independent same-writer ff example proves it. The literal visually preferred ending is abl au u, not an accepted reading. Bourdeau proposed ablauff but transcribes the partial gloss as a b l aut; the gloss does not prove ff. See ending-alternative-2026-10-28.json and p2-original-controls.json.'),
}
assert rows[0][16]=='BB'
assert [rows[1][i] for i in (1,11,18,19)]==['55','[I]','8','XX']
passages=[]
for p,row in enumerate(rows):
 aligned=[]
 for i,tok in enumerate(row):
  lit=key.get(tok,'?');reading=lit
  basis='comparison key' if not tok.startswith(('[634]','[768]')) else 'manuscript gloss, not key 255 word list'
  note=None
  if (p,i) in exceptions:reading,basis,note=exceptions[p,i]
  aligned.append({'index':i,'source_token':tok,'comparison_output':lit,'working_reading':reading,'basis':basis,'note':note})
 passages.append({'literal':''.join(x['comparison_output'] for x in aligned),
                  'working_reading':''.join(x['working_reading'] for x in aligned),'alignment':aligned})
assert passages[0]['working_reading']=='disgustirtundertanin<Holstein: gloss>'
assert passages[1]['working_reading']=='<Sueco: gloss>gottgebdasallwolablauff'

earlier = json.loads(subprocess.check_output([sys.executable,str(ROOT/'work/followup.py')],text=True))
occurrences=earlier['nomenclator_occurrences']
for row in occurrences:
 if row['occurrence'] in (24,25):
  row['current_assessment']={'group':['447','602'],'preferred_phrase_gloss':'Kayser',
      'allocation':'unresolved; do not assert 447 is an additional person, or that Kayser decodes 602 alone',
      'prior_individual_claim_retained_as_history':True}

manifest=json.loads((ROOT/'work/source-sha256-2026-10-23-key1236.json').read_text())
changed=[name for name,h in manifest.items() if hashlib.sha256((ROOT/'source'/name).read_bytes()).hexdigest()!=h]
if changed:raise SystemExit(f'Source preservation failure: {changed}')
result={
 'status':'PARTIAL: gloss/language-assisted candidates; terminal ff is not the current original-shape preference',
 'preferred_evidence_workflow':'Original signs and unchanged key first; black annotations secondary. See glyph_first.py for the BB/PP/66 passage-1 alternatives and all eight unaltered-key passage-2 branches.',
 'passages':passages,
 'passage2_visual_preference':{
     'initial_pair':'II (provisional)','terminal_pair':'XX (provisional)',
     'key_only_branch':'<768>gottgebdasallwolablauu',
     'limit':'Assumes preferred ll and au too; unresolved ending, not accepted grammatical plaintext. The fluent candidate above retains a separate language-driven ff hypothesis.'},
 'preferred_segmentations':['disgustirt | undertan | in | <Holstein>','<Sueco> | gott | geb | das | all | wol | ablauff'],
 'annotation_conflicts':[{'passage':2,'indices':[10,11],'source_tokens':['20','[I]'],
     'annotation':'amm','preferred_working_reading':'all',
     'evidence':'Bourdeau NOTES.md line 26 and original image 4; visible in current-p2-ll.png.',
     'interpretation':'Neighboring similar ll/mm signs make confusion plausible, but the responsible error and possession of the key are not established.',
     'consequence':'The passage-1 margin n remains proposed evidence, not authoritative plaintext overriding BB=z.',
     'feedback_credit':'Claude flagged the omission in user-supplied feedback.'}],
 'editorial_expansions':{'passage1':'Totaliter disgustirt [sind die] Undertan[en] in Holstein ...',
     'qualification':'[sind die] and [en] are editorial supplies, not recovered characters or a demonstrated abbreviation.'},
 'alliance_fragment':'eine estroite <303 alliance> zwischen <447 602: Kayser, phrase gloss; internal allocation unresolved> und <834 Rex Daniae> unter Handen',
 'nomenclator_occurrences':occurrences,
 'open_questions':['independent verification of provisionally preferred PP=n; original-capital comparisons strengthen it, but BB=z remains live','initial pair: provisionally preferred II=g versus numeric 55=h','annotation amm versus preferred all','terminal XX=u visual preference versus ff language candidate; unresolved abl au u ending','447/602 internal allocation','625 title and name reading','actual expanded nomenclator and possible differing letter cells'],
 'gloss_date':'undetermined; contemporary origin and possession of the 1672 key have not been proved',
 'credits':{'Bourdeau':'original key match and most readings, including Gott ... ablauff',
            'Claude':'proposed margin n and Undertan in interpretation; later flagged omitted amm/all disagreement',
            'Codex':'verification, explicit ll/mm comparison, II-versus-55 and BB-versus-PP original-text glyph hypotheses, bounded nomenclator-numbering audit, reconciliation of claims, phrase-level treatment of 447/602'},
 'source_preservation':{'checked':len(manifest),'changed':changed},
 'independent_review':False,
}
print(json.dumps(result,ensure_ascii=False,indent=2))
