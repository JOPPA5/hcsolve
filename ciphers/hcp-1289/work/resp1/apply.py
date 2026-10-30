import re
p='work/ledger-opus.txt'; L=open(p,encoding='utf-8').read().split('\n')
def edit(row,old,new):
    for i,l in enumerate(L):
        if l.startswith(row+' '):
            assert l.count(old)==1,(row,old,l.count(old)); L[i]=l.replace(old,new); return
    raise SystemExit(row)
edit('02','K O:diaeresis ) Z I','K O:diaeresis ) Z O:diaeresis')
edit('04','D E A L + E','D E E? L + E')
edit('08','O J E L J E','O J? E L J E')
edit('10','T A D E )','T E D E )')
edit('18','K O Z T','K O:diaeresis Z T')
edit('27','E L O 6 6 H O G Y M I N E L E L O 6 6 6','E L O?:diaeresis 6 6 H O G Y M I N E L E L O:diaeresis 6 6 6')
edit('28','F A E F E ) M E G + O G L A K O Z','F A E F E K M E G + O G L A L K O Z')
edit('28','L E G Y ) Z E F E T E T E L','L E G? Y ) Z E F? E T E T E L')
edit('29','V A L E E D','V E L E E D')
i=[k for k,l in enumerate(L) if l.startswith('# suffix ?')][0]
L.insert(i+1,'# Revised 2026-10-30 after review 1: signs re-read from enlarged crops of work/hires (rows 2,4,8,10,18,27,28,29); see SOLUTION.md, Response to review 1.')
open(p,'w',encoding='utf-8').write('\n'.join(L))
p='work/normalized-opus.txt'; t=open(p,encoding='utf-8').read()
old='A Sándor meg ráér és meg fog[lal]kozni,'; assert old in t
open(p,'w',encoding='utf-8').write(t.replace(old,'A Sándor[ral] meg ráérek még foglalkozni,'))
