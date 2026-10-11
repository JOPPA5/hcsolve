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
using namespace std;int H[26][26];vector<double>logs,lf;mt19937 rng(52771701);array<int,26>N{};
double score(array<int,26>counts){sort(counts.begin(),counts.end());double z=0;for(int i=0;i<26;i++)z+=counts[i]*logs[i]-lf[counts[i]];return z;}
array<int,26> pooled(const array<int,26>&O,const array<int,26>&sh,const vector<string>&texts){array<int,26>n{};for(auto&t:texts)for(int i=0;i<t.size();i++)n[(O[t[i]-'a']-23*(i/26)%26-sh[i%26]+52)%26]++;return n;}
void phasepass(array<int,26>&O,array<int,26>&sh,const vector<string>&texts,double&now){fill(&H[0][0],&H[0][0]+676,0);for(auto&t:texts)for(int i=0;i<t.size();i++)H[i%26][(O[t[i]-'a']-23*(i/26)%26+26)%26]++;vector<int>order(25);iota(order.begin(),order.end(),1);shuffle(order.begin(),order.end(),rng);for(int j:order){double top=now;int chosen=sh[j];auto bestn=N;for(int d=0;d<26;d++){auto counts=N;for(int u=0;u<26;u++)counts[u]+=H[j][(u+d)%26]-H[j][(u+sh[j])%26];double v=score(counts);if(v>top+1e-8){top=v;chosen=d;bestn=counts;}}sh[j]=chosen;N=bestn;now=top;}}
void emit(string label,double sc,const array<int,26>&o,const array<int,26>&sh){cout<<label<<'\t'<<sc<<'\t';for(int x:o)cout<<x<<',';cout<<'\t';for(int x:sh)cout<<x<<',';cout<<'\n'<<flush;}
int main(int argc,char**argv){ifstream ct(argv[1]);string s;vector<string>texts;int length=0;while(ct>>s){texts.push_back(s);length+=s.size();}ifstream mo(argv[2]);double v;while(mo>>s>>v)logs.push_back(v);sort(logs.begin(),logs.end());assert(logs.size()==26);lf.resize(length+1);for(int i=0;i<=length;i++)lf[i]=lgamma(i+1);ifstream keys(argv[3]);string line;while(getline(keys,line)){istringstream ss(line);string label,key;ss>>label>>key;replace(key.begin(),key.end(),',',' ');istringstream ks(key);array<int,26>O;for(int&i:O)ks>>i;fill(&H[0][0],&H[0][0]+676,0);for(auto&t:texts)for(int i=0;i<t.size();i++)H[i%26][(O[t[i]-'a']-23*(i/26)%26+26)%26]++;double best=-1e30;array<int,26>bs;
for(int restart=0;restart<8;restart++){array<int,26>shift;shift[0]=0;for(int j=1;j<26;j++)shift[j]=rng()%26;N.fill(0);for(int j=0;j<26;j++)for(int u=0;u<26;u++)N[u]+=H[j][(u+shift[j])%26];double now=score(N);for(int pass=0;pass<10;pass++){vector<int>order(25);iota(order.begin(),order.end(),1);shuffle(order.begin(),order.end(),rng);bool changed=false;for(int j:order){double top=now;int chosen=shift[j];array<int,26>nextN=N;for(int d=0;d<26;d++){auto counts=N;for(int u=0;u<26;u++)counts[u]+=H[j][(u+d)%26]-H[j][(u+shift[j])%26];double x=score(counts);if(x>top+1e-8){top=x;chosen=d;nextN=counts;}}if(chosen!=shift[j]){changed=true;shift[j]=chosen;N=nextN;now=top;}}if(!changed)break;}if(now>best){best=now;bs=shift;}}
emit(label+"-initial",best,O,bs);auto bo=O;auto bestsh=bs;auto sh=bs;N=pooled(O,sh,texts);double now=score(N);for(int it=0;it<5000;it++){auto oo=O;int a=rng()%26,b=rng()%26;swap(oo[a],oo[b]);auto counts=pooled(oo,sh,texts);double next=score(counts),temp=.03+1.5*(1.-(it%1000)/1000.);if(next>=now||log((rng()+1.)/4294967297.)<(next-now)/temp){O=oo;N=counts;now=next;}if(it%100==99)phasepass(O,sh,texts,now);if(now>best){best=now;bo=O;bestsh=sh;}}emit(label+"-refined",best,bo,bestsh);}}
