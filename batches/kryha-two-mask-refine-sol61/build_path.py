from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'kryha-two-mask-language-sol61';s=(S/'enumerate-profile.cpp').read_text();s=s.replace('#include <queue>','#include <queue>\n#include <fstream>\n#include <unordered_map>\n#include <cstdint>')
a=s.index('double profile()');z=s.index('\nvoid dfs',a)
s=s[:a]+'''int ng=6,kzero;array<int,26>pin,outring;vector<string>texts_pair;unordered_map<uint64_t,double>model;uint64_t pw=1;
double profile(){double total=0;for(int q=0;q<2;q++){array<int,23>D{};for(int j=0;j<23;j++){int off=q?path[j].second:path[j].first;int anchor=q?b0:a0;D[j]=mod(c[anchor+off]-c[anchor]+(q?kzero:0));}uint64_t code=0;for(int i=0;i<texts_pair[q].size();i++){int v=pin[mod(outring[texts_pair[q][i]-'a']-D[i%23]-23*(i/23))];code=code*26+v;if(i>=ng)code-=uint64_t(pin[mod(outring[texts_pair[q][i-ng]-'a']-D[(i-ng)%23]-23*((i-ng)/23))])*pw*26;if(i>=ng-1){auto it=model.find(code);total+=it==model.end()?-ng:it->second;}}}return total;}
''' +s[z:]
s=s.replace('int main(){','''int main(int argc,char**argv){ng=stoi(argv[1]);for(int i=0;i<ng-1;i++)pw*=26;ifstream mf(argv[2]);string word;double value;while(mf>>word>>value){uint64_t code=0;for(char ch:word)code=code*26+ch-'a';model[code]=value;}ifstream cfg(argv[3]);cfg>>kzero;for(int&x:outring)cfg>>x;for(int&x:pin)cfg>>x;texts_pair.resize(2);cfg>>texts_pair[0]>>texts_pair[1];''')
(B/'path-refine.cpp').write_text(s)
