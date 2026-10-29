"""Decode original-sign alternatives under the unchanged comparison key.

No annotation-derived letter override or nomenclator expansion is applied.
This is not a blind reading: the earlier interpretations were already known.
The finite alternatives are manual glyph judgments, not recovered key cells.
"""
from pathlib import Path
import hashlib
import itertools
import json

ROOT = Path(__file__).resolve().parents[1]
ALPHABET = 'abcdefghiklmnopqrstuwxyz'
BASES = [20,22,24,26,28,21,23,25,27,29,70,72,74,76,78,71,73,75,77,79,120,122,124,126]
CAPITALS = 'CC DD EE FF GG HH II KK LL MM NN OO PP QQ RR SS TT UU WW XX YY ZZ AA BB'.split()
KEY = {str(base + 10*row):letter for letter,base in zip(ALPHABET,BASES) for row in range(5)}
KEY.update(dict(zip(CAPITALS,ALPHABET)))
KEY.update({str(n):'' for n in range(1,20)})
KEY.update({'[st]':'st','[tt]':'tt','[ll]':'ll','[mm]':'mm','[au]':'au','[ff]':'ff'})
# II names the doubled I/J-shaped homophone, not two plaintext letters.
assert KEY['II']=='g' and KEY['55']=='h' and KEY['BB']=='z' and KEY['PP']=='n'

source_rows = [line.split() for line in (ROOT/'source/bourdeau/ct.txt').read_text().splitlines()
               if line.strip() and not line.startswith('#')]
assert source_rows[1][1]=='55' and source_rows[0][16]=='BB'

def decode(tokens):
    return ''.join('<'+token[1:-1]+'>' if token in ('[634]','[768]') else KEY[token]
                   for token in tokens)

# Position 11 in row 2 is a neutral inherited placeholder, not a literal I.
base_rows = [row.copy() for row in source_rows]
base_rows[1][11]='[ll]'

decisions = [
 {'passage':2,'index':1,'source_placeholder':'55','options':['II','55'],
  'basis':'Two long hooked strokes contrast with the bends/bowls in eight numeral-5 controls, now including initial-position 5 in 500 and 50. Both comparison tables distinguish II=g and 55=h. German-script Ihr/Ihro supplies variants, not a matching standalone I/J. The target upper loops/crossbars are not securely established, and the nearby black gloss is not used to reconstruct them. See p2-original-controls.json.',
  'status':'II provisionally preferred by shape; numeric 55 remains live, no independent verification'},
 {'passage':2,'index':11,'source_placeholder':'[I]','options':['[ll]'],
  'basis':'Loop above stem and lower bar agree with key ll. Key mm has the loop below; mm is retained only as a contrary control.',
  'status':'preferred visual identification'},
 {'passage':2,'index':18,'source_placeholder':'8','options':['[au]','8'],
  'basis':'The looped stroke is compatible with the au symbol, but a reading as numeric 8 would be a null.',
  'status':'au preferred by shape/context; ambiguity retained'},
 {'passage':2,'index':19,'source_placeholder':'XX','options':['XX','[ff]'],
  'basis':'Target has two separate crossed forms resembling passage-1 XX. Inverse key 254 explicitly gives XX=u and also shows looped upper arms. Key255 ff has diagonal contacts absent from the target. Qualification 2026-10-28: those contacts may be overlapping arms of two crossed components; wider spacing could separate them without deleting an independent connector. Original st/tt do not directly test that spacing model. No independent same-writer ff control proves it. See p2-original-controls.json and ending-alternative-2026-10-28.json.',
  'status':'XX=u provisionally preferred by shape; ff remains a language-driven conditional interpretation'},
]

branches=[]
for initial, au, final in itertools.product(('II','55'),('[au]','8'),('[ff]','XX')):
    row=base_rows[1].copy()
    row[1]=initial;row[18]=au;row[19]=final
    branches.append({'glyph_choices':{'initial_pair':initial,'loop_sign':au,'final_pair':final},
                     'tokens':row,'plaintext':decode(row),'changed_key_cells':0})
assert len(branches)==8
working=branches[0]
assert working['plaintext']=='<768>gottgebdasallwolablauff'
# Keep the prior fluent candidate, but do not present it as the shape preference.
visual_working=branches[1]
assert visual_working['glyph_choices']=={'initial_pair':'II','loop_sign':'[au]','final_pair':'XX'}
assert visual_working['plaintext']=='<768>gottgebdasallwolablauu'

bb_controls=[]
for glyph in ('BB','66','PP'):
    row=base_rows[0].copy();row[16]=glyph
    bb_controls.append({'glyph':glyph,'plaintext':decode(row),
        'tokens':row,'changed_key_cells':0,
        'status':{'BB':'retained baseline transcription; BB versus PP is not adjudicated',
                  '66':'historical numeric alternative; lower preference',
                  'PP':'provisionally preferred after expanded original-capital controls: the target lacks the further lower right bow seen in Lit. B, Brunsvicense, Berlin and Berlino; not verified, and BB remains live'}[glyph]})
assert bb_controls[2]['plaintext']=='disgustirtundertanin<634>'

mm_control=working['tokens'].copy();mm_control[11]='[mm]'
same_xx=working['tokens'].copy();same_xx[19]='XX'
global_ff=base_rows[0].copy();global_ff[4]='[ff]'

manifest=json.loads((ROOT/'work/source-sha256-2026-10-23-key1236.json').read_text())
changed=[name for name,sha in manifest.items()
         if hashlib.sha256((ROOT/'source'/name).read_bytes()).hexdigest()!=sha]
if changed:raise SystemExit(f'Source preservation failure: {changed}')

result={
 'status':'PARTIAL; PP=n and initial II=g are provisionally preferred; terminal XX=u is provisionally favored by shape and leaves the ending abl au u unresolved',
 'policy':'Original signs plus unchanged comparison key first; black annotations are secondary and do not select the branches.',
 'prior_exposure':'Not blind: Bourdeau and Claude readings were known before this check.',
 'key_sources':['source/full/key255.jpg','source/full/key254.jpg'],
 'new_comparison_sheet':'work/p2-initial-numeral-controls.png',
 'passage2_original_evidence_record':'work/p2-original-controls.json',
 'preserved_source_tokens':source_rows,
 'passage1_key_output_with_BB':decode(base_rows[0]),
 'passage1_BB_controls':bb_controls,
 'passage1_glyph_decision':{
     'index':16,'preserved_source_token':'BB','options':['BB','PP','66'],
     'new_evidence':'Lit. B supplies a detached original capital on the same page. It and Brunsvicense, Berlin and Berlino have a further lower right bow/return not visible in either target sign; the target is closer to P in Proposition. The small lower stem loop alone is not diagnostic. Cipher FF/Foedus and LL/Lit. support using clear-text capital controls.',
     'qualification':'Manual feature judgments using word contexts, not blind analysis or an independent review. Connected b/B in breviat remains similar and Portrait has another P form. Script variation and simplified B cannot be excluded. No repeated unambiguous cipher PP has been found.',
     'comparison_sheet':'work/expanded-bp-capitals.png',
     'evidence_record':'work/expanded-bp-controls.json',
     'status':'PP provisionally preferred; BB/PP remains unverified'},
 'passage1_conditional_PP_reading':bb_controls[2],
 'passage1_preferred_working_reading':bb_controls[2],
 'passage2_glyph_decisions':decisions,
 'passage2_all_branches':branches,
 'passage2_conditional_working_reading':working,
 'passage2_conditional_working_reading_basis':'Prior fluent candidate, not the current shape preference: terminal ff requires an unverified glyph variant/collision or intended-text restoration.',
 'passage2_shape_preferred_branch':visual_working,
 'passage2_shape_preferred_branch_limit':'Manual provisional choices II/ll/au/XX; abl au u is a literal unresolved ending, not an accepted grammatical plaintext. Numeric 55 and terminal ff remain in the eight branches.',
 'passage2_terminal_collision_hypothesis':{
     'status':'unproved possible writing rule, not a recovered key cell',
     'description':'The ff symbol may consist of overlapping crossed components. Wider spacing could remove their contact without omitting a separate connector, producing an XX-like pair. This would allow the same visible family to carry u in passage 1 and ff in passage 2, but no independent example establishes that collision here.',
     'distinction':'A local u/ff ambiguity is different from globally replacing XX=u with ff; the global contrary control does not refute every collision model.'},
 'passage2_spacing_followup':'work/ending-alternative-2026-10-28.json; qualifies the connector argument without changing any tokens, key cells or decoded branches',
 'contrary_controls':{
     'loop_below_as_mm':decode(mm_control),
     'final_pair_as_XX_u':decode(same_xx),
     'first_passage_XX_as_ff':decode(global_ff),
     'qualification':'Controls show consequences, not proof. The final-pair-as-XX branch is now visually favored; a global XX=ff test does not exclude an unverified local u/ff graphic collision.'},
 'not_solved':['independent verification of provisionally preferred PP=n; BB=z remains a live alternative','independent verification of provisionally preferred initial II versus 55','terminal XX=u visual preference versus ff language candidate; unresolved abl au u ending',
               'actual 1672 nomenclator; codes 634 and 768 remain opaque in this key-only output'],
 'source_preservation':{'checked':len(manifest),'changed':changed},
 'independent_review':False,
}
print(json.dumps(result,ensure_ascii=False,indent=2))
