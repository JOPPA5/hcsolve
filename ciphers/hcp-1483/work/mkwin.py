import subprocess, sys
P='/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3'
L=[('p1',44,73),('p2',66,90),('l01',84,117),('l02',124,155),('l03',159,193),('l04',194,226),('l05',225,264),('l06',262,296),('l07',294,330),('l08',324,358),('l09',351,391),('l10',388,424),('l11',419,451),('l12',459,489),('l13',490,525),('l14',527,558),('l15',553,586),('l16',582,608),('l17',603,629)]
for n,a,b in L:
    for i,x in enumerate([575,675,775,875]):
        subprocess.run([P,'-I','work/zoom.py',str(a),str(b),str(x),str(x+108),f'work/w/{n}_{i}.png','10'],check=True)
