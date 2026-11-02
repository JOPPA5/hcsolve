p='ledger.txt'; s=open(p,encoding='utf-8').read()
R=[('# HCP1292 row ledger, Claude Opus 5.5, 2026-10-30.','# HCP1292 row ledger, Claude Opus 5.5, 2026-10-30, revised 2026-11-02 (old version: ledger-2026-10-30.txt).'),
('08 megatedésenisborbankeres','08 megátédesénisborbankeres'),
('09 [blot]amavigasztalastésmajd','09 {t}amavigasztalastésmajd'),
('20 hetemhetekmegédesemhogy','20 hetamhetekmegédesemhogy'),
('21 jelhogysen{?}ifelvasztesnak','21 jelhogyse{m}ifélvasutasnak'),
('22 {a}lanyovolnemtudokésém~~','22 {a}lanyorolnemtudokéssem~~'),
('23 [blot]nifelelanyrolmarsokzor','23 {m}ifelelanyrolmarsokzor'),
('26 marnemersemitdeigmegazt','26 marnemérsemitdeigmegazt'),
('azönbecsületszeveenel','azönbecsületszavaénel'),
('30 szorornödecsak','30 szorornodecsak'),
('S4 vabra','S4 vebra')]
for a,b in R:
    assert s.count(a)==1,a
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
