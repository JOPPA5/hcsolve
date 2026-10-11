from codec import *
import hashlib
left='ASEV EREL IMIT ATIO NONT HEUS EFUL NESS OFTH ECAD ENUS ISTH ATEV ERYM ESSA GEMU STBE AMUL TIPL EOFT WENT YFIV ELET TERS LONG'.lower().split();right='SYST RETO MTAT TLUS OATL EEES FIYH EASD FNMS CHBH NEUV SNPM TOFA RENU SEIE EIEL TARL MENT IEET OGEV ESIT FAIS LTNG EEUV OWUL'.lower().split();plain=''.join(left);cipher=''.join(right);assert len(left)==len(right)==25 and all(len(x)==4 for x in left+right);assert enc(plain,'easy')==cipher and dec(cipher,'easy')==plain
# Independent index-array permutation checks for repeats and shared V/W rotations.
symbols=''.join(chr(33+i)for i in range(100));cases=[]
for key in ['aaaa','wwvv','vwvw','wvvw','xvpx','zzaz','abca']:
 assert dec(enc(symbols,key),key)==symbols
 order=sorted(range(4),key=lambda c:(key[c],c));ranks=[order.index(c)for c in range(4)];mapping=[((r-row(key[c]))%25)*4+c for r in range(25)for c in order];assert len(set(mapping))==100;assert enc(symbols,key)==''.join(symbols[i]for i in mapping);cases.append(dict(key=key,row_shifts=[row(c)for c in key],sorted_column_order=order,original_column_ranks=ranks,index_permutation_valid=True,independent_inverse_exact=True))
assert row('v')==row('w')==21 and row('x')==22 and row('y')==23 and row('z')==24
(B/'example-verification.json').write_text(json.dumps(dict(primary_example_key='easy',example_full100_encoding_exact=True,example_full100_inverse_exact=True,example_cipher_prefix=cipher[:20],rotation='down by ascending row index; original row r moves to cipher row r+shift',stable_ties='left-to-right among equal key letters',edge_cases=cases,primary_pdf_sha256=hashlib.sha256((B/'source/lesson16.pdf').read_bytes()).hexdigest()),indent=2));print('PASS primary full100 EASY example and repeated/VW permutation checks')
