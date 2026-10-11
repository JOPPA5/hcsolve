from pathlib import Path
B=Path(__file__).resolve().parent;s=(B/'path-refine.cpp').read_text();a=s.index('double profile()');z=s.index('\nvoid dfs',a)
s=s[:a]+'''int floor23(int x){return x>=0?x/23:(x-22)/23;}
int residue23(int x){return (x%23+23)%23;}
int letter(int side,int i,const array<int,23>&D){int t=i-20-side;return pin[mod(outring[texts_pair[side][i]-'a']-D[residue23(t)]-23*floor23(t))];}
double profile(){double total=0;for(int q=0;q<2;q++){array<int,23>D{};for(int j=0;j<23;j++){int off=q?path[j].second:path[j].first;int anchor=q?b0:a0;D[j]=mod(c[anchor+off]-c[anchor]+(q?kzero:0));}uint64_t code=0;for(int i=0;i<texts_pair[q].size();i++){int v=letter(q,i,D);code=code*26+v;if(i>=ng)code-=uint64_t(letter(q,i-ng,D))*pw*26;if(i>=ng-1){auto it=model.find(code);total+=it==model.end()?-ng:it->second;}}}return total;}
''' +s[z:];(B/'path-full.cpp').write_text(s)
s=(B/'run_path.py').read_text().replace("str(B/'path-refine')","str(B/'path-full')").replace("data['ciphertexts'][q][q:][:len(data['ciphertexts'][0])-1]","data['ciphertexts_full'][q]");(B/'run_full.py').write_text(s)
s=(B/'project_paths.py').read_text().replace("ct=data['ciphertexts'][q][q:][:len(data['ciphertexts'][0])-1]","ct=data['ciphertexts_full'][q]").replace("for i,c in enumerate(ct):d=coord[h[i%23]]-coord[h[0]]+(179 if h[i%23]<h[0]else 0)+179*(i//23)+(data['K'][0]if q else 0);out+=chr(97+(data['O'][ord(c)-97]-d)%26)","for i,c in enumerate(ct):\n   t=i-20-q;d=coord[h[t%23]]-coord[h[0]]+(179 if h[t%23]<h[0]else 0)+179*(t//23)+(data['K'][0]if q else 0);out+=chr(97+(data['O'][ord(c)-97]-d)%26)");(B/'project_full.py').write_text(s)
s=(B/'alternate.py').read_text().replace("'run_path.py'","'run_full.py'").replace("'project_paths.py'","'project_full.py'").replace("'check_paths.py'","'check_full_paths.py'");(B/'alternate_full.py').write_text(s)
