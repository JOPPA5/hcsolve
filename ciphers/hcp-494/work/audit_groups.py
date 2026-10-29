"""Audit numeral grouping without changing a digit or borrowing a new key.

The period-separated reading is preferred from the image. Splitting within a
group or crossing a period is an explicitly weaker transcription hypothesis.
BB and the earlier 66 reading are separate branches. No candidate is accepted.
"""
from pathlib import Path
from functools import lru_cache
import hashlib, itertools, json

ROOT = Path(__file__).resolve().parents[1]
ALPHABET = 'abcdefghiklmnopqrstuwxyz'
BASE = [20,22,24,26,28,21,23,25,27,29,70,72,74,76,78,71,73,75,77,79,120,122,124,126]
KEY = {str(b+10*r): p for p,b in zip(ALPHABET,BASE) for r in range(5)}
NULLS = list(range(1,20)) + [121,131,141,151,161,171,123,125,127,129,133,135,137,139,143,145,147,149,153,155,157,159,163,165,167,169,173,175,177,178,179]
assert not set(KEY).intersection(map(str,NULLS))
KEY.update({str(n): '' for n in NULLS})

def partitions(groups, cross_periods):
    digits = ''.join(groups)
    observed = set(itertools.accumulate(map(len,groups))) - {len(digits)}
    @lru_cache(None)
    def walk(start):
        if start == len(digits): return [((),())]
        out=[]
        for width in (1,2,3):
            end=start+width
            if end>len(digits):continue
            token=digits[start:end]
            if token not in KEY:continue # no zero, leading-zero, or invented cells
            if not cross_periods and any(start<b<end for b in observed):continue
            for tail,cuts in walk(end):
                out.append(((token,)+tail, ((end,) if end<len(digits) else ())+cuts))
        return out
    rows={}
    for tokens,cuts in walk(0):
        plain=''.join(KEY[t] for t in tokens)
        cost=len(set(cuts)^observed)
        row=rows.setdefault(plain, {'paths':0,'minimum_boundary_edits':cost,'tokens':list(tokens)})
        row['paths']+=1
        if cost<row['minimum_boundary_edits']:
            row.update(minimum_boundary_edits=cost,tokens=list(tokens))
    return rows

before=['119','74','26','28','83','117','20']
after=['37','104']
families=[]
for relaxed in (False,True):
    left=partitions(before,relaxed);right=partitions(after,relaxed)
    for glyph in ('BB','66'):
        middle={'z':{'paths':1,'minimum_boundary_edits':0,'tokens':['BB']}} if glyph=='BB' else partitions(['66'],relaxed)
        combined={}
        for (a,ra),(b,rb),(c,rc) in itertools.product(left.items(),middle.items(),right.items()):
            plain=a+b+c;cost=sum(r['minimum_boundary_edits'] for r in (ra,rb,rc))
            row=combined.setdefault(plain, {'plaintext':plain,'paths':0,'minimum_boundary_edits':cost,'tokens':ra['tokens']+rb['tokens']+rc['tokens']})
            row['paths']+=ra['paths']*rb['paths']*rc['paths']
            if cost<row['minimum_boundary_edits']:
                row.update(minimum_boundary_edits=cost,tokens=ra['tokens']+rb['tokens']+rc['tokens'])
        if glyph=='BB' and not relaxed:
            assert all('az' in s for s in combined)
        families.append({'cross_periods':relaxed,'glyph_branch':glyph,
                         'distinct_strings':len(combined),'segmentation_paths':sum(r['paths'] for r in combined.values()),
                         'all_contain_az':all('az' in s for s in combined),
                         'candidates':sorted(combined.values(),key=lambda r:(r['minimum_boundary_edits'],r['plaintext']))})
result={'accepted':None,'literal_suffix':'undertazin','digit_changes_allowed':False,
        'zero_and_leading_zero_allowed':False,'code20':'a, following the alphabet cells; not silently treated as a null',
        'families':families,'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'source/full/0004.jpg',ROOT/'source/full/key255.jpg',ROOT/'source/bourdeau/ct.txt']},
        'limits':'Only the known alphabet/nulls are used, with no expanded nomenclator entries. Crossing visible periods is unsupported by the preferred image transcription. This is a grouping diagnostic, not a decipherment.'}
(ROOT/'work/group-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
for f in families:
    print(json.dumps({k:v for k,v in f.items() if k!='candidates'}))
    print('LOWEST COST:', [(r['plaintext'],r['minimum_boundary_edits']) for r in f['candidates'][:15]])
