from pathlib import Path
import json
b=Path(__file__).resolve().parent
# Independently read typed Figure 1, not inferred from Figure 5.
base=[[11,3,17,8,13,4,12,21,16,2,5,20,14,6,18,9,1,19,10,15,7],[9,5,10,4,17,3,11,2,15,8,12,1,18,13,7,16,6,14],[7,16,8,22,6,15,21,5,20,14,9,17,24,1,11,4,18,3,12,10,19,13,2,23]]
printed=[[7,11,3,17,8,13,4,12,21,16,2,5,20,14,6,18,9,1,19,10,15],[7,16,6,14,9,5,10,4,17,3,11,2,15,8,12,1,18,13],[7,16,8,22,6,15,21,5,20,14,9,17,24,1,11,4,18,3,12,10,19,13,2,23]]
rows=[]
for k,want in zip(base,printed):
 assert sorted(k)==list(range(1,len(k)+1));p=k.index(7);got=k[p:]+k[:p];assert got==want;rows.append(dict(width=len(k),unaligned_primary=k,aligned_primary=want,computed=got,exact=True))
# Figure 2 is a separate XQ manual table, NOT proved to be Figure 5's daily table.
table={'1':'XUF','2':'RN','3':'YZW','4':'ED','5':'BA','6':'QCI','7':'JOP','8':'KG','9':'HVL','0':'SMT'};mapping={c:d for d,letters in table.items()for c in letters}
old_helper_indicator='JGEMU';old_helper_digits=''.join(mapping[c]for c in old_helper_indicator)
check=json.load(open(b/'collated-stage-check.json'));groups=check['computed_final_groups'];variants={}
for pos in [4,5]:
 variants[f'insert_after_{pos}_payload_groups'] = groups[:pos]+['[INDICATOR UNRESOLVED]']+groups[pos:]
(b/'alignment-and-assembly.json').write_text(json.dumps(dict(figure1_alignment=rows,figure1_widths_not_figure5_widths=True,figure2_table=table,figure5_indicator_reading='Unresolved; no new indicator proposed',old_tentative_helper_indicator=old_helper_indicator,old_helper_digits_under_separate_figure2_table=old_helper_digits,figure2_daily_table_transfer_not_established=True,article_alignment7_digits='78901',article_ip=5,figure5_arrow_observation='V-shaped arrow between HNEAU (payload group5) and NNHAS (group6), suggests after5; paper does not define before/after numerically',existing_tentative_script_insert_index=4,assembly_layouts_with_unresolved_indicator=variants,printed_header_literal='360',header_semantics_not_proved=True),indent=2)+'\n');print('Three primary physical-key rotations exact; indicator/insertion alternatives preserved.')
