#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <sstream>
#include <vector>
using namespace std;array<int,52>coord;int H[30][26],m;vector<double>logs,lf;mt19937 rng(52770501);
vector<int> ordered(vector<int>holes,int phase){rotate(holes.begin(),holes.begin()+phase,holes.end());return holes;}
double score(const vector<int>&holes){array<int,26>N{};int start=holes[0];for(int j=0;j<m;j++){int d=(coord[holes[j]]-coord[start]+(holes[j]<start?179:0))%26;for(int z=0;z<26;z++)N[(z-d+26)%26]+=H[j][z];}sort(N.begin(),N.end());double s=0;for(int j=0;j<26;j++)s+=N[j]*logs[j]-lf[N[j]];return s;}
int main(int argc,char**argv){m=stoi(argv[5]);assert(m>=20&&m<=30);ifstream co(argv[2]);for(int&x:coord)co>>x;ifstream mo(argv[3]);string x;double v;while(mo>>x>>v)logs.push_back(v);sort(logs.begin(),logs.end());lf.resize(771);for(int i=0;i<=770;i++)lf[i]=lgamma(i+1);ifstream ct(argv[1]);vector<string>texts;while(ct>>x)texts.push_back(x);assert(texts.size()==2);ifstream keys(argv[4]);string line;int ix=0;while(getline(keys,line)){istringstream ss(line);int index,oldscore;string key;ss>>index>>oldscore>>key;replace(key.begin(),key.end(),',',' ');istringstream ks(key);array<int,26>O;for(int&z:O)ks>>z;fill(&H[0][0],&H[0][0]+780,0);for(auto&t:texts)for(int i=0;i<t.size();i++)H[i%m][(O[t[i]-'a']-23*(i/m)%26+26)%26]++;for(int restart=0;restart<8;restart++){vector<int>all(52);iota(all.begin(),all.end(),0);shuffle(all.begin(),all.end(),rng);vector<int>sel(all.begin(),all.begin()+m);sort(sel.begin(),sel.end());auto holes=ordered(sel,rng()%m);double now=score(holes),best=now;auto bh=holes;for(int it=0;it<10000;it++){auto candidate=holes;if(rng()%8==0)rotate(candidate.begin(),candidate.begin()+rng()%m,candidate.end());else{int start=candidate[0],pos=rng()%m,h;do{h=rng()%52;}while(find(candidate.begin(),candidate.end(),h)!=candidate.end());candidate[pos]=h;if(pos==0)start=h;sort(candidate.begin(),candidate.end());rotate(candidate.begin(),find(candidate.begin(),candidate.end(),start),candidate.end());}double next=score(candidate),temp=.03+4*(1.-(it%2500)/2500.);if(next>=now||log((rng()+1.)/4294967297.)<(next-now)/temp){holes=candidate;now=next;}if(now>best){best=now;bh=holes;}}cout<<index<<'\t'<<restart<<'\t'<<best<<'\t';for(int h:bh)cout<<h<<',';cout<<'\t';for(int z:O)cout<<z<<',';cout<<'\n'<<flush;}ix++;}assert(ix==32);}
