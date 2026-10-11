from pathlib import Path
P=Path(__file__).resolve().parent
s=(P.parent/'quagmire3-keyword-sol61/search.cpp').read_text().replace('int T;','int T;int kind;')
s=s.replace("x.lookup[c][r]=x.slots[(x.A[c]-r+26)%26]-'a';","x.lookup[c][r]=kind==1?x.slots[(c-r+26)%26]-'a':(x.A[c]-r+26)%26;")
s=s.replace('string models=argv[1];','kind=stoi(argv[6]);string models=argv[1];')
(P/'search.cpp').write_text(s)
